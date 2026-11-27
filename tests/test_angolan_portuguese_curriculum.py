import ast
import pathlib
import unittest

from angolan_portuguese_lessons import PORTUGUESE_LESSONS, TOPICS

REQUIRED_FIELDS = (
    "title", "goal", "objectives", "vocabulary", "grammar", "expressions",
    "examples", "conversations", "pronunciation", "exercises", "assessment",
    "speaking", "summary", "homework",
)


class AngolanPortugueseCurriculumTests(unittest.TestCase):
    def test_course_contains_all_107_chapters(self):
        self.assertEqual(len(TOPICS), 107)
        self.assertEqual(set(TOPICS), set(range(1, 108)))
        self.assertEqual(set(PORTUGUESE_LESSONS), set(range(1, 108)))

    def test_cefr_level_distribution_matches_shared_course_path(self):
        expected = {
            "A1 – Absolute Beginner": 17,
            "A2 – Elementary": 19,
            "B1 – Intermediate": 18,
            "B2 – Upper Intermediate": 18,
            "C1 – Advanced": 18,
            "C2 – Mastery": 17,
        }
        actual = {}
        for topic in TOPICS.values():
            actual[topic["level"]] = actual.get(topic["level"], 0) + 1
        self.assertEqual(actual, expected)

    def test_every_chapter_has_the_complete_self_study_structure(self):
        for lesson_id, lesson in PORTUGUESE_LESSONS.items():
            with self.subTest(lesson_id=lesson_id):
                for field in REQUIRED_FIELDS:
                    self.assertIn(field, lesson)
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["goal"].strip())
                self.assertGreaterEqual(len(lesson["objectives"]), 3)
                self.assertGreaterEqual(len(lesson["vocabulary"]), 5)
                self.assertGreaterEqual(len(lesson["grammar"]), 3)
                self.assertGreaterEqual(len(lesson["expressions"]), 3)
                self.assertGreaterEqual(len(lesson["examples"]), 3)
                self.assertGreaterEqual(len(lesson["conversations"]), 1)
                self.assertGreaterEqual(len(lesson["pronunciation"]), 3)
                self.assertGreaterEqual(len(lesson["exercises"]), 5)
                self.assertGreaterEqual(len(lesson["assessment"]), 5)
                self.assertGreaterEqual(len(lesson["speaking"]), 2)
                self.assertGreaterEqual(len(lesson["summary"]), 2)
                self.assertGreaterEqual(len(lesson["homework"]), 2)

    def test_vocabulary_entries_have_valid_shape_and_unique_headwords(self):
        for lesson_id, lesson in PORTUGUESE_LESSONS.items():
            entries = lesson["vocabulary"]
            headwords = [entry[0].strip().casefold() for entry in entries]
            with self.subTest(lesson_id=lesson_id):
                self.assertEqual(len(headwords), len(set(headwords)))
                for entry in entries:
                    self.assertEqual(len(entry), 5)
                    self.assertTrue(entry[0].strip())
                    self.assertTrue(entry[1].strip())
                    self.assertTrue(entry[2].strip())

    def test_exercises_and_assessments_have_distinct_questions(self):
        for lesson_id, lesson in PORTUGUESE_LESSONS.items():
            exercises = {(q, tuple(opts), answer) for q, opts, answer, _ in lesson["exercises"]}
            assessments = {(q, tuple(opts), answer) for q, opts, answer, _ in lesson["assessment"]}
            with self.subTest(lesson_id=lesson_id):
                self.assertFalse(exercises.intersection(assessments))

    def test_all_questions_have_four_distinct_options_and_valid_answers(self):
        for lesson_id, lesson in PORTUGUESE_LESSONS.items():
            for section in ("exercises", "assessment"):
                for question, options, answer, explanation in lesson[section]:
                    with self.subTest(lesson_id=lesson_id, section=section, question=question):
                        self.assertEqual(len(options), 4)
                        self.assertEqual(len(set(options)), 4)
                        self.assertGreaterEqual(answer, 0)
                        self.assertLess(answer, len(options))
                        self.assertTrue(explanation.strip())

    def test_first_chapter_teaches_portuguese_alphabet_and_pronunciation(self):
        lesson = PORTUGUESE_LESSONS[1]
        grammar_titles = " ".join(title for title, _ in lesson["grammar"]).lower()
        self.assertIn("alphabet", grammar_titles)
        self.assertIn("nasal", grammar_titles)
        self.assertIn("accent", grammar_titles)
        self.assertIn("filho", " ".join(example[0] for example in lesson["examples"]).lower())
        self.assertIn("nh", " ".join(q[0] for q in lesson["exercises"]).lower())

    def test_angolan_context_and_regional_pronunciation_are_explicit(self):
        funge = [entry for lesson in PORTUGUESE_LESSONS.values() for entry in lesson["vocabulary"] if entry[0] == "o funge"]
        candongueiro = [entry for lesson in PORTUGUESE_LESSONS.values() for entry in lesson["vocabulary"] if entry[0] == "o candongueiro"]
        self.assertTrue(funge)
        self.assertTrue(candongueiro)
        for lesson in PORTUGUESE_LESSONS.values():
            self.assertTrue(any("Angola" in note or "Angolan" in note or "var" in note.lower() for note in lesson["pronunciation"]))

    def test_app_routes_portuguese_and_keeps_language_progress_separate(self):
        app_source = (pathlib.Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
        ast.parse(app_source)
        self.assertIn('return PORTUGUESE_LESSONS.get(lesson_id)', app_source)
        self.assertIn('def language_progress_prefix(username, language):', app_source)
        self.assertIn('"angolan_portuguese"', app_source)
        self.assertIn('display_lesson_title(item)', app_source)


if __name__ == "__main__":
    unittest.main()
