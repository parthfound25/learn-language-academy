import ast
import pathlib
import unittest

from a1_lessons import A1_LESSONS
from a2_lessons import A2_LESSONS
from b1_lessons import B1_LESSONS
from b2_lessons import B2_LESSONS
from c1_lessons import C1_LESSONS
from c2_lessons import C2_LESSONS
from curriculum_extensions import EXTENSION_LESSONS


BANKS = (A1_LESSONS, A2_LESSONS, B1_LESSONS, B2_LESSONS, C1_LESSONS, C2_LESSONS)
REQUIRED_FIELDS = (
    "title", "goal", "vocabulary", "grammar", "expressions", "examples",
    "conversations", "exercises", "speaking", "summary", "assessment",
)


class CourseCurriculumTests(unittest.TestCase):
    def test_original_lesson_ids_are_all_present(self):
        original_ids = set()
        for bank in BANKS:
            original_ids.update(bank.keys())
        self.assertEqual(original_ids, set(range(2, 91)))

    def test_extension_ids_are_complete(self):
        self.assertEqual(set(EXTENSION_LESSONS), set(range(91, 103)))

    def test_total_course_count_is_102(self):
        # Lesson 1 is authored in app.py; 2-90 are the six original content banks.
        self.assertEqual(1 + sum(len(bank) for bank in BANKS) + len(EXTENSION_LESSONS), 102)

    def test_every_authored_lesson_has_the_shared_content_contract(self):
        all_lessons = {}
        for bank in BANKS:
            all_lessons.update(bank)
        all_lessons.update(EXTENSION_LESSONS)
        for lesson_id, lesson in all_lessons.items():
            with self.subTest(lesson_id=lesson_id):
                for field in REQUIRED_FIELDS:
                    self.assertIn(field, lesson)
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["goal"].strip())
                self.assertGreaterEqual(len(lesson["vocabulary"]), 5)
                self.assertGreaterEqual(len(lesson["grammar"]), 3)
                self.assertGreaterEqual(len(lesson["examples"]), 3)
                self.assertGreaterEqual(len(lesson["conversations"]), 1)
                self.assertGreaterEqual(len(lesson["exercises"]), 5)
                self.assertGreaterEqual(len(lesson["assessment"]), 5)
                self.assertGreaterEqual(len(lesson["speaking"]), 2)
                self.assertGreaterEqual(len(lesson["summary"]), 2)

    def test_all_question_answer_indexes_are_valid(self):
        all_lessons = {}
        for bank in BANKS:
            all_lessons.update(bank)
        all_lessons.update(EXTENSION_LESSONS)
        for lesson_id, lesson in all_lessons.items():
            for section in ("exercises", "assessment"):
                for question, options, answer, explanation in lesson[section]:
                    with self.subTest(lesson_id=lesson_id, section=section, question=question):
                        self.assertGreaterEqual(len(options), 2)
                        self.assertGreaterEqual(answer, 0)
                        self.assertLess(answer, len(options))
                        self.assertTrue(explanation.strip())

    def test_extensions_include_objectives_pronunciation_and_homework(self):
        for lesson_id, lesson in EXTENSION_LESSONS.items():
            with self.subTest(lesson_id=lesson_id):
                for field in ("objectives", "pronunciation", "homework"):
                    self.assertGreaterEqual(len(lesson[field]), 3)

    def test_app_is_valid_python_and_contains_the_sequence_integration(self):
        app_path = pathlib.Path(__file__).resolve().parents[1] / "app.py"
        source = app_path.read_text(encoding="utf-8")
        ast.parse(source)
        self.assertIn("EXTENSION_INSERT_AFTER", source)
        self.assertIn("COURSE_TOTAL = len(ALL_LESSONS)", source)
        self.assertIn("def render_unified_lesson", source)
        self.assertIn("def lesson_is_unlocked", source)
        self.assertIn("render_unified_lesson(st.session_state.active_lesson)", source)


if __name__ == "__main__":
    unittest.main()
