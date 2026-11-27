"""AI lesson-audio generation and durable Supabase Storage caching.

Audio is generated only when a learner requests it, then reused by every learner.
Configure four target-language voice IDs in Streamlit Secrets. The selected voice
must be reviewed for the intended regional accent; Portuguese support alone does
not certify an Angolan accent.
"""
from __future__ import annotations

import hashlib
import json
import re
from urllib.parse import quote

import requests

BUCKET = "lesson-audio"
MODEL_ID = "eleven_multilingual_v2"
API_BASE = "https://api.elevenlabs.io/v1"


class AudioConfigurationError(RuntimeError):
    """Raised when required TTS or storage credentials are not configured."""


def _slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", str(value)).strip("-").lower()
    return value or "clip"


def _target_language(language: str) -> str:
    if language == "Canadian French":
        return "fr"
    if language == "Angolan Portuguese":
        return "pt"
    raise ValueError(f"Unsupported lesson language: {language}")


def build_lesson_audio_segments(lesson: dict, lesson_id: int, language: str) -> list[dict]:
    """Create stable, de-duplicated clips for every teachable lesson section."""
    lang = _target_language(language)
    segments: list[dict] = []

    def add(section: str, label: str, text: str, voice_role: str = "female", speech_language: str | None = None):
        spoken = " ".join(str(text).split()).strip()
        if not spoken:
            return
        digest = hashlib.sha256(spoken.encode("utf-8")).hexdigest()[:12]
        segments.append({
            "id": f"{_slug(section)}-{_slug(label)}-{digest}",
            "section": section,
            "label": label,
            "text": spoken,
            "language": speech_language or lang,
            "voice_role": voice_role,
        })

    add("lesson", "learning-goal", lesson.get("goal", ""), speech_language="en")
    for index, item in enumerate(lesson.get("objectives", []) or [], 1):
        add("objectives", f"objective-{index}", item, speech_language="en")

    vocabulary = lesson.get("vocabulary", lesson.get("vocab", [])) or []
    for index, item in enumerate(vocabulary, 1):
        if len(item) >= 1:
            add("vocabulary", f"word-{index}", item[0])
        if len(item) >= 2:
            add("vocabulary-meanings", f"meaning-{index}", item[1], speech_language="en")
        if len(item) >= 5:
            example = str(item[4]).split(" — ", 1)[0].strip()
            add("vocabulary-examples", f"example-{index}", example)

    for index, item in enumerate(lesson.get("grammar", []) or [], 1):
        if len(item) >= 2:
            add("grammar", f"topic-{index}", item[0], speech_language="en")
            add("grammar-explanations", f"explanation-{index}", item[1], speech_language="en")

    for index, item in enumerate(lesson.get("expressions", []) or [], 1):
        if len(item) >= 1:
            add("expressions", f"phrase-{index}", item[0])
        if len(item) >= 2:
            add("expression-meanings", f"meaning-{index}", item[1], speech_language="en")
        if len(item) >= 3:
            add("expression-notes", f"note-{index}", item[2], speech_language="en")

    for index, item in enumerate(lesson.get("examples", []) or [], 1):
        if len(item) >= 1:
            add("examples", f"sentence-{index}", item[0])
        if len(item) >= 2:
            add("example-translations", f"translation-{index}", item[1], speech_language="en")
        if len(item) >= 3:
            add("example-notes", f"note-{index}", item[2], speech_language="en")

    for dialogue_index, item in enumerate(lesson.get("conversations", []) or [], 1):
        if len(item) < 2:
            continue
        title, dialogue = item[0], item[1]
        add("dialogues", f"dialogue-{dialogue_index}-title", title, speech_language="en")
        if len(item) >= 3:
            add("dialogue-translations", f"dialogue-{dialogue_index}-translation", item[2], speech_language="en")
        for line_index, line in enumerate(dialogue, 1):
            if len(line) < 2:
                continue
            # Dialogue roles alternate male/female to make turn-taking audible.
            role = "female" if line_index % 2 else "male"
            add("dialogues", f"dialogue-{dialogue_index}-line-{line_index}", line[1], role)

    for section, field in (
        ("pronunciation-guidance", "pronunciation"),
        ("speaking-practice", "speaking"),
        ("lesson-summary", "summary"),
        ("homework", "homework"),
    ):
        for index, text in enumerate(lesson.get(field, []) or [], 1):
            add(section, f"item-{index}", text, speech_language="en")

    for section in ("exercises", "assessment"):
        for question_index, question in enumerate(lesson.get(section, []) or [], 1):
            if len(question) < 4:
                continue
            add(section, f"question-{question_index}", question[0], speech_language="en")
            for option_index, option in enumerate(question[1], 1):
                add(section + "-options", f"question-{question_index}-option-{option_index}", option, speech_language="en")
            add(section + "-feedback", f"question-{question_index}-explanation", question[3], speech_language="en")

    # Stable order and IDs let a regenerated lesson reuse unchanged clips.
    unique = {}
    for segment in segments:
        unique.setdefault(segment["id"], segment)
    return list(unique.values())


def _voice_id(secrets, language: str, role: str) -> str:
    audio = secrets.get("audio", {})
    locale = "fr_ca" if language == "fr" else "pt_ao" if language == "pt" else "en"
    key = f"{locale}_{role}_voice_id"
    voice_id = str(audio.get(key, "")).strip()
    if not voice_id:
        raise AudioConfigurationError(
            f"Missing [audio].{key}. Add a reviewed ElevenLabs voice ID in Streamlit Secrets."
        )
    return voice_id


def _storage_config(secrets):
    supabase = secrets.get("supabase", {})
    url = str(supabase.get("url", "")).rstrip("/")
    key = str(supabase.get("service_role_key", "")).strip()
    if not url or not key:
        raise AudioConfigurationError("Supabase URL and service_role_key are required for persistent lesson audio.")
    return url, key


def _headers(key: str) -> dict:
    return {"apikey": key, "Authorization": f"Bearer {key}"}


def _object_url(url: str, path: str) -> str:
    return f"{url}/storage/v1/object/{BUCKET}/{quote(path, safe='/')}"


def _public_url(url: str, path: str) -> str:
    return f"{url}/storage/v1/object/public/{BUCKET}/{quote(path, safe='/')}"


def _download_object(url: str, key: str, path: str):
    response = requests.get(_object_url(url, path), headers=_headers(key), timeout=30)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.content


def _object_exists(url: str, key: str, path: str) -> bool:
    response = requests.head(_object_url(url, path), headers=_headers(key), timeout=30)
    if response.status_code == 404:
        return False
    response.raise_for_status()
    return True


def _upload_object(url: str, key: str, path: str, data: bytes, content_type: str):
    headers = _headers(key)
    headers.update({"Content-Type": content_type, "x-upsert": "true"})
    response = requests.post(_object_url(url, path), headers=headers, data=data, timeout=90)
    response.raise_for_status()


def _synthesize(text: str, voice_id: str, api_key: str, language_code: str) -> bytes:
    headers = {"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "audio/mpeg"}
    payload = {
        "text": text,
        "model_id": MODEL_ID,
        "language_code": language_code,
        "voice_settings": {"stability": 0.48, "similarity_boost": 0.78, "style": 0.18, "use_speaker_boost": True},
    }
    response = requests.post(f"{API_BASE}/text-to-speech/{quote(voice_id, safe='')}", headers=headers, json=payload, timeout=120)
    response.raise_for_status()
    return response.content


def generate_lesson_audio(lesson: dict, lesson_id: int, language: str, secrets) -> dict:
    """Generate all lesson clips once, store MP3s and a manifest in Supabase."""
    audio = secrets.get("audio", {})
    api_key = str(audio.get("elevenlabs_api_key", "")).strip()
    if not api_key:
        raise AudioConfigurationError("Missing [audio].elevenlabs_api_key in Streamlit Secrets.")
    storage_url, storage_key = _storage_config(secrets)
    segments = build_lesson_audio_segments(lesson, lesson_id, language)
    if not segments:
        raise ValueError("This lesson has no speakable content.")

    prefix = f"{_slug(language)}/lesson-{int(lesson_id)}"
    manifest_path = f"{prefix}/manifest.json"
    existing_bytes = _download_object(storage_url, storage_key, manifest_path)
    existing = {}
    if existing_bytes:
        try:
            existing = {item["id"]: item for item in json.loads(existing_bytes.decode("utf-8")).get("clips", [])}
        except (ValueError, KeyError, TypeError):
            existing = {}

    clips = []
    generated = 0
    for segment in segments:
        previous = existing.get(segment["id"], {})
        path = previous.get("path") or f"{prefix}/{segment['id']}.mp3"
        # Reuse the object if it still exists; otherwise synthesize it.
        cached = _object_exists(storage_url, storage_key, path)
        if not cached:
            role = segment["voice_role"]
            voice_id = _voice_id(secrets, segment["language"], role)
            audio_bytes = _synthesize(segment["text"], voice_id, api_key, segment["language"])
            _upload_object(storage_url, storage_key, path, audio_bytes, "audio/mpeg")
            generated += 1
        clips.append({
            "id": segment["id"],
            "section": segment["section"],
            "label": segment["label"],
            "text": segment["text"],
            "voice_role": segment["voice_role"],
            "language": segment["language"],
            "path": path,
            "url": _public_url(storage_url, path),
        })

    manifest = {
        "version": 1,
        "language": language,
        "lesson_id": int(lesson_id),
        "provider": "ElevenLabs",
        "model": MODEL_ID,
        "clip_count": len(clips),
        "clips": clips,
    }
    _upload_object(storage_url, storage_key, manifest_path, json.dumps(manifest, ensure_ascii=False).encode("utf-8"), "application/json")
    return {"manifest": manifest, "generated": generated, "reused": len(clips) - generated}


def load_lesson_audio(lesson_id: int, language: str, secrets) -> dict | None:
    """Load an existing manifest without triggering paid synthesis."""
    storage_url, storage_key = _storage_config(secrets)
    path = f"{_slug(language)}/lesson-{int(lesson_id)}/manifest.json"
    raw = _download_object(storage_url, storage_key, path)
    if not raw:
        return None
    return json.loads(raw.decode("utf-8"))
