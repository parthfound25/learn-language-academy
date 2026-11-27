import unittest

from lesson_audio import build_lesson_audio_segments
from a1_lessons import A1_LESSONS
from a2_lessons import A2_LESSONS
from b1_lessons import B1_LESSONS
from b2_lessons import B2_LESSONS
from c1_lessons import C1_LESSONS
from c2_lessons import C2_LESSONS
from curriculum_extensions import EXTENSION_LESSONS
from angolan_portuguese_lessons import PORTUGUESE_LESSONS


class LessonAudioTests(unittest.TestCase):
    def test_all_107_french_lessons_have_audio_content(self):
        lessons = {}
        for bank in (A1_LESSONS, A2_LESSONS, B1_LESSONS, B2_LESSONS, C1_LESSONS, C2_LESSONS, EXTENSION_LESSONS):
            lessons.update(bank)
        self.assertEqual(len(lessons) + 1, 107)  # Lesson 1 is authored in app.py.
        for lesson_id, lesson in lessons.items():
            with self.subTest(lesson_id=lesson_id):
                clips = build_lesson_audio_segments(lesson, lesson_id, "Canadian French")
                self.assertGreater(len(clips), 0)
                self.assertTrue(any(clip["section"] == "vocabulary" for clip in clips))
                self.assertTrue(any(clip["section"] == "grammar" for clip in clips))
                self.assertTrue(any(clip["section"] == "dialogues" for clip in clips))

    def test_all_107_angolan_portuguese_lessons_have_audio_content(self):
        self.assertEqual(set(PORTUGUESE_LESSONS), set(range(1, 108)))
        for lesson_id, lesson in PORTUGUESE_LESSONS.items():
            with self.subTest(lesson_id=lesson_id):
                clips = build_lesson_audio_segments(lesson, lesson_id, "Angolan Portuguese")
                self.assertGreater(len(clips), 0)
                self.assertTrue(any(clip["section"] == "vocabulary" for clip in clips))
                self.assertTrue(any(clip["section"] == "grammar-explanations" for clip in clips))
                self.assertTrue(any(clip["section"] == "dialogues" for clip in clips))

    def test_dialogue_roles_alternate_female_and_male(self):
        lesson = {
            "conversations": [
                ("At the market", [("A", "Bom dia."), ("B", "Como está?"), ("A", "Estou bem."), ("B", "Obrigado.")], "")
            ]
        }
        clips = build_lesson_audio_segments(lesson, 1, "Angolan Portuguese")
        dialogue_lines = [clip for clip in clips if clip["section"] == "dialogues" and "-line-" in clip["id"]]
        self.assertEqual([clip["voice_role"] for clip in dialogue_lines], ["female", "male", "female", "male"])

    def test_explanations_and_study_instructions_use_english_narration(self):
        lesson = {
            "goal": "Understand the present tense.",
            "grammar": [("Present tense", "Use it for current actions.")],
            "pronunciation": ["Listen carefully."],
            "speaking": ["Describe your routine."],
            "summary": ["The present tense describes current actions."],
            "homework": ["Write five sentences."],
        }
        clips = build_lesson_audio_segments(lesson, 1, "Canadian French")
        english_sections = {"lesson", "grammar", "grammar-explanations", "pronunciation-guidance", "speaking-practice", "lesson-summary", "homework"}
        self.assertTrue(clips)
        self.assertTrue(all(clip["language"] == "en" for clip in clips if clip["section"] in english_sections))

    def test_vocabulary_examples_only_speak_the_target_language_side(self):
        lesson = {"vocabulary": [("bonjour", "hello", "bon-zhoor", "/bɔ̃.ʒuʁ/", "Bonjour ! — Hello!")]}
        clips = build_lesson_audio_segments(lesson, 1, "Canadian French")
        example = next(clip for clip in clips if clip["section"] == "vocabulary-examples")
        self.assertEqual(example["text"], "Bonjour !")
        self.assertEqual(example["language"], "fr")

    def test_clip_ids_are_stable_unique_and_content_sensitive(self):
        lesson = {"examples": [("Je suis prêt.", "I am ready.", "Example.")]}
        first = build_lesson_audio_segments(lesson, 8, "Canadian French")
        second = build_lesson_audio_segments(lesson, 8, "Canadian French")
        changed = build_lesson_audio_segments({"examples": [("Je suis ici.", "I am here.", "Example.")]}, 8, "Canadian French")
        self.assertEqual([x["id"] for x in first], [x["id"] for x in second])
        self.assertNotEqual(first[0]["id"], changed[0]["id"])
        self.assertEqual(len({x["id"] for x in first}), len(first))

    def test_unknown_language_is_rejected(self):
        with self.assertRaises(ValueError):
            build_lesson_audio_segments({}, 1, "Spanish")


if __name__ == "__main__":
    unittest.main()
