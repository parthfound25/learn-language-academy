import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ActivityTrackingTests(unittest.TestCase):
    def test_activity_tracking_uses_server_side_service_role_only(self):
        module = (ROOT / "activity_tracking.py").read_text(encoding="utf-8")
        migration = (ROOT / "supabase" / "activity_tracking.sql").read_text(encoding="utf-8")
        self.assertIn('settings["service_role_key"]', module)
        self.assertIn("learner_sessions", migration)
        self.assertIn("learner_progress", migration)
        self.assertIn("learner_activity_events", migration)
        self.assertIn("revoke all", migration.lower())
        self.assertIn("authenticated", migration.lower())

    def test_activity_tracking_captures_sessions_progress_and_practice(self):
        module = (ROOT / "activity_tracking.py").read_text(encoding="utf-8")
        for token in (
            "start_session", "heartbeat_session", "end_session",
            "save_progress_snapshot", "load_progress_snapshot",
            "practice_rounds", "practice_correct", "practice_total",
            "get_admin_activity_data", "reset_learner_data", "session_is_active",
        ):
            with self.subTest(token=token):
                self.assertIn(token, module)

    def test_admin_can_reset_selected_learner_progress_and_time_in_one_click(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        module = (ROOT / "activity_tracking.py").read_text(encoding="utf-8")
        self.assertIn("Reset {selected_learner}'s progress and time spent", app)
        self.assertIn("reset_learner_data(selected_learner, invalidate_active_sessions=True)", app)
        self.assertIn('"duration_seconds": 0', module)
        self.assertIn('"completed_lessons": []', module)
        self.assertIn('for language in ("Canadian French", "Angolan Portuguese")', module)
        self.assertIn('on_conflict="username,language"', module)
        self.assertIn('"status": "logged_out", "logout_at": now', module)
        self.assertIn("session_is_active(st.session_state.activity_session_id)", app)

    def test_invalidated_learner_session_is_forced_to_login(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn("not session_is_active(st.session_state.activity_session_id)", app)
        self.assertIn('st.session_state.pop("active_user", None)', app)
        self.assertIn("Your session was reset by the administrator", app)

    def test_admin_dashboard_uses_dedicated_admin_username_and_shows_learner_metrics(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn('ADMIN_USERNAME = "Admin"', app)
        self.assertIn('st.session_state.active_user.casefold() == ADMIN_USERNAME.casefold()', app)
        self.assertIn('st.session_state.active_user.casefold() != ADMIN_USERNAME.casefold()', app)
        self.assertIn('st.session_state.page = "Admin Dashboard"', app)
        self.assertIn('if is_admin_user:', app)
        self.assertIn('st.radio("ADMINISTRATION", ["Admin Dashboard"]', app)
        self.assertIn('st.session_state.selected_language = ""', app)
        self.assertIn('preferred_language not in AVAILABLE_LEARNING_LANGUAGES', app)
        self.assertIn('Choose your learning language', app)
        self.assertIn('load_language_progress(st.session_state.active_user, chosen_language)', app)
        self.assertIn('if not is_admin_user:', app)
        self.assertNotIn('page_options.append("Admin Dashboard")', app)
        self.assertIn('name.casefold() != ADMIN_USERNAME.casefold()', app)
        self.assertIn('"Parth Sharma" = "YOUR_LEARNER_PASSWORD"', app)
        for label in (
            "Login and logout history", "Lessons cleared", "Practice rounds",
            "Practice accuracy", "Total recorded learning time", "Recent learning activity",
        ):
            with self.subTest(label=label):
                self.assertIn(label, app)
        self.assertIn("log_activity_event(", app)
        self.assertIn('@st.fragment(run_every="60s")', app)


if __name__ == "__main__":
    unittest.main()
