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
            "get_admin_activity_data",
        ):
            with self.subTest(token=token):
                self.assertIn(token, module)

    def test_admin_dashboard_uses_dedicated_admin_username_and_shows_learner_metrics(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn('ADMIN_USERNAME = "Admin"', app)
        self.assertIn('st.session_state.active_user.casefold() == ADMIN_USERNAME.casefold()', app)
        self.assertIn('st.session_state.active_user.casefold() != ADMIN_USERNAME.casefold()', app)
        self.assertIn('name.casefold() != ADMIN_USERNAME.casefold()', app)
        self.assertIn('"Parth Sharma" = "YOUR_LEARNER_PASSWORD"', app)
        self.assertIn('page_options.append("Admin Dashboard")', app)
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
