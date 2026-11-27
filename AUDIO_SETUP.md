# Lesson audio setup

The lesson player supports all 107 lessons in Canadian French and all 107 lessons in Angolan Portuguese. Audio is generated on demand the first time a learner selects **Generate complete lesson audio** for a lesson. MP3 files and a JSON manifest are then saved in Supabase Storage and reused; opening the lesson does not call the paid TTS API.

## 1. Create the storage bucket

Run `supabase/lesson_audio_storage.sql` in the Supabase SQL Editor. It creates a public-read `lesson-audio` bucket for generated MP3 clips and manifests. The bucket contains lesson content only, never learner records or credentials. Uploads use the Supabase service-role key from the server.

## 2. Configure the TTS provider

Create an ElevenLabs API key and choose six voice IDs in the ElevenLabs voice library. Add them to Streamlit Community Cloud → App settings → Secrets, alongside your existing `[users]` and `[supabase]` sections. Do not commit these values to GitHub or share them in chat.

```toml
[audio]
elevenlabs_api_key = "YOUR_ELEVENLABS_API_KEY"

# Select voices that you have listened to and approved.
fr_ca_female_voice_id = "YOUR_CANADIAN_FRENCH_FEMALE_VOICE_ID"
fr_ca_male_voice_id = "YOUR_CANADIAN_FRENCH_MALE_VOICE_ID"
pt_ao_female_voice_id = "YOUR_ANGOLAN_PORTUGUESE_FEMALE_VOICE_ID"
pt_ao_male_voice_id = "YOUR_ANGOLAN_PORTUGUESE_MALE_VOICE_ID"

# English narration for explanations, instructions and study notes.
en_female_voice_id = "YOUR_ENGLISH_FEMALE_VOICE_ID"
en_male_voice_id = "YOUR_ENGLISH_MALE_VOICE_ID"
```

Keep your existing `[users]` and `[supabase]` secrets. Add this as another section; do not replace them or create duplicate TOML section names.

## 3. Regional accent quality gate

- Canadian French clips are requested as French (`fr`); choose voice IDs whose actual accent has been reviewed as Canadian French.
- Angolan Portuguese clips are requested as Portuguese (`pt`); choose voice IDs whose actual accent has been reviewed by an Angolan Portuguese speaker.
- A Portuguese-capable voice is not automatically an Angolan voice. Do not use a Brazilian or European Portuguese voice as an Angolan substitute. If the selected TTS account does not provide an authentic Angolan voice, do not configure that voice ID until an appropriate reviewed voice is available.
- The app uses the female voice for individual items and alternates female/male voices for dialogue turns.

The app cannot verify a voice's accent from its ID. Test a few representative clips in each course with a qualified speaker before using the generated audio as a pronunciation model.

## 4. Generate audio in the app

1. Sign in as a learner and open an unlocked lesson.
2. Open the **0 · Audio** tab.
3. Select **Generate complete lesson audio**.
4. Wait for the first generation to finish. The app creates clips for vocabulary, vocabulary examples, grammar titles and explanations, expressions, examples, dialogue titles and lines, pronunciation guidance, speaking practice, summaries, homework, objectives and the lesson goal.
5. Play the saved clips in their section groups. Reopening the lesson reuses the saved manifest and MP3s.

Generation is per lesson, not a background bulk job. This prevents an unexpected large TTS bill and lets you review quality as you work through the 214 lessons. Unchanged clips are reused when a lesson is regenerated.

## 5. Cost, privacy and operations

- Audio generation is an explicit learner action; no TTS request is made merely by opening a lesson.
- The ElevenLabs API key and Supabase service-role key stay in Streamlit Secrets.
- MP3 files are stored once in Supabase Storage and shared by all learners.
- Audio generation does not change XP, lesson completion, assessment answers, session tracking or reset behavior.
- The public bucket is intended only for non-personal lesson audio. Never store learner recordings or private information in it.
- The current pipeline generates standard-speed MP3s. Playback speed can be changed in the browser's native audio controls where supported.
