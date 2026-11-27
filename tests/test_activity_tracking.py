from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_activity_tracking_uses_server_side_service_role_only():
    module = (ROOT / "activity_tracking.py").read_text(encoding="utf-8")
    migration = (ROOT / "supabase" / "activity_tracking.sql").read_text(encoding="utf-8")
    assert 'settings["service_role_key"]' in module
    assert "learner_sessions" in migration
    assert "learner_progress" in migration
    assert "learner_activity_events" in migration
    assert "revoke all" in migration.lower()
    assert "authenticated" in migration.lower()


def test_activity_tracking_captures_sessions_progress_and_practice():
    module = (ROOT / "activity_tracking.py").read_text(encoding="utf-8")
    for token in (
        "start_session", "heartbeat_session", "end_session",
        "save_progress_snapshot", "load_progress_snapshot",
        "practice_rounds", "practice_correct", "practice_total",
        "get_admin_activity_data",
    ):
        assert token in module
