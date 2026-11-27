"""Durable learner activity and administrator reporting.

Uses the Supabase service-role key only on the Streamlit server. Never expose it
to browser code or ordinary learner sessions.
"""
from datetime import datetime, timezone, timedelta
from uuid import uuid4

import streamlit as st
from supabase import create_client


@st.cache_resource(show_spinner=False)
def _cached_client(url: str, service_role_key: str):
    return create_client(url, service_role_key)


def _client():
    try:
        settings = st.secrets["supabase"]
        url = str(settings["url"])
        key = str(settings["service_role_key"])
        if not url or not key:
            return None
        return _cached_client(url, key)
    except Exception:
        return None


def tracking_available() -> bool:
    return _client() is not None


def _now():
    return datetime.now(timezone.utc)


def _iso(value):
    return value.isoformat() if hasattr(value, "isoformat") else value


def start_session(username: str):
    client = _client()
    if client is None:
        return None
    now = _now()
    session_id = str(uuid4())
    try:
        client.table("learner_sessions").insert({
            "session_id": session_id,
            "username": username,
            "login_at": now.isoformat(),
            "last_seen_at": now.isoformat(),
            "duration_seconds": 0,
            "status": "active",
        }).execute()
        return {"session_id": session_id, "started_at": now.isoformat()}
    except Exception:
        return None


def heartbeat_session(session_id: str, started_at: str):
    client = _client()
    if client is None or not session_id:
        return
    now = _now()
    try:
        started = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
        duration = max(0, int((now - started).total_seconds()))
    except Exception:
        duration = 0
    try:
        client.table("learner_sessions").update({
            "last_seen_at": now.isoformat(),
            "duration_seconds": duration,
            "status": "active",
        }).eq("session_id", session_id).is_("logout_at", "null").execute()
    except Exception:
        return


def end_session(session_id: str, started_at: str):
    client = _client()
    if client is None or not session_id:
        return
    now = _now()
    try:
        started = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
        duration = max(0, int((now - started).total_seconds()))
    except Exception:
        duration = 0
    try:
        client.table("learner_sessions").update({
            "last_seen_at": now.isoformat(),
            "logout_at": now.isoformat(),
            "duration_seconds": duration,
            "status": "logged_out",
        }).eq("session_id", session_id).execute()
    except Exception:
        return


def log_activity_event(username: str, language: str, event_type: str,
                       lesson_id=None, metadata=None):
    client = _client()
    if client is None:
        return
    try:
        client.table("learner_activity_events").insert({
            "username": username,
            "language": language or "",
            "event_type": event_type,
            "lesson_id": lesson_id,
            "metadata": metadata or {},
        }).execute()
    except Exception:
        return


def save_progress_snapshot(username: str, language: str, progress: dict):
    client = _client()
    if client is None or not language:
        return
    payload = {
        "username": username,
        "language": language,
        "xp": int(progress.get("xp", 0)),
        "completed_lessons": progress.get("completed", []),
        "active_lesson": int(progress.get("active_lesson", 1)),
        "practice_rounds": int(progress.get("practice_rounds", 0)),
        "practice_correct": int(progress.get("practice_correct", 0)),
        "practice_total": int(progress.get("practice_total", 0)),
        "achievements": progress.get("earned_achievements", []),
        "updated_at": _now().isoformat(),
    }
    try:
        client.table("learner_progress").upsert(
            payload, on_conflict="username,language"
        ).execute()
    except Exception:
        return


def load_progress_snapshot(username: str, language: str):
    client = _client()
    if client is None or not language:
        return None
    try:
        response = (
            client.table("learner_progress")
            .select("*")
            .eq("username", username)
            .eq("language", language)
            .limit(1)
            .execute()
        )
        return response.data[0] if response.data else None
    except Exception:
        return None


def latest_language_for_user(username: str):
    client = _client()
    if client is None:
        return ""
    try:
        response = (
            client.table("learner_progress")
            .select("language,updated_at")
            .eq("username", username)
            .order("updated_at", desc=True)
            .limit(1)
            .execute()
        )
        return response.data[0]["language"] if response.data else ""
    except Exception:
        return ""


def get_admin_activity_data():
    client = _client()
    if client is None:
        return None
    try:
        # A missing heartbeat for three minutes means the tab was closed or the
        # browser went away without an explicit sign-out.
        stale_before = (_now() - timedelta(minutes=3)).isoformat()
        stale = client.table("learner_sessions").select("session_id,last_seen_at").eq(
            "status", "active"
        ).lt("last_seen_at", stale_before).execute().data
        for row in stale:
            client.table("learner_sessions").update({
                "status": "timed_out",
                "logout_at": row["last_seen_at"],
            }).eq("session_id", row["session_id"]).execute()
        progress = client.table("learner_progress").select("*").order(
            "updated_at", desc=True
        ).limit(5000).execute().data
        sessions = client.table("learner_sessions").select("*").order(
            "login_at", desc=True
        ).limit(5000).execute().data
        events = client.table("learner_activity_events").select("*").order(
            "created_at", desc=True
        ).limit(1000).execute().data
        return {"progress": progress, "sessions": sessions, "events": events}
    except Exception:
        return None
