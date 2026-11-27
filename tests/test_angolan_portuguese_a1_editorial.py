import unittest

from angolan_portuguese_lessons import PORTUGUESE_LESSONS


class AngolanPortugueseA1EditorialTests(unittest.TestCase):
    def test_first_five_a1_lessons_are_individually_authored(self):
        expected_titles = {
            1: "Portuguese Alphabet, Sounds and Pronunciation",
            2: "Greetings and Basic Introductions",
            3: "Personal Information and Introducing Yourself",
            4: "Basic Sentence Patterns, Word Order and Negation",
            5: "Numbers, Counting and Basic Mathematics",
        }
        for lesson_id, title in expected_titles.items():
            with self.subTest(lesson_id=lesson_id):
                lesson = PORTUGUESE_LESSONS[lesson_id]
                self.assertEqual(lesson["title"], title)
                self.assertGreaterEqual(len(lesson["objectives"]), 4)
                self.assertGreaterEqual(len(lesson["vocabulary"]), 8)
                self.assertGreaterEqual(len(lesson["grammar"]), 4)
                self.assertGreaterEqual(len(lesson["examples"]), 5)
                self.assertGreaterEqual(len(lesson["conversations"]), 2)
                self.assertGreaterEqual(len(lesson["exercises"]), 6)
                self.assertGreaterEqual(len(lesson["assessment"]), 6)
                self.assertGreaterEqual(len(lesson["speaking"]), 4)
                self.assertGreaterEqual(len(lesson["homework"]), 3)

    def test_practice_and_assessment_are_distinct(self):
        for lesson_id in range(1, 6):
            lesson = PORTUGUESE_LESSONS[lesson_id]
            practice_prompts = {item[0] for item in lesson["exercises"]}
            assessment_prompts = {item[0] for item in lesson["assessment"]}
            self.assertFalse(practice_prompts & assessment_prompts)
            for question in lesson["exercises"] + lesson["assessment"]:
                prompt, options, answer_index, explanation = question
                self.assertTrue(prompt)
                self.assertEqual(len(options), 4)
                self.assertEqual(len(set(options)), 4)
                self.assertGreaterEqual(answer_index, 0)
                self.assertLess(answer_index, len(options))
                self.assertTrue(explanation)

    def test_angolan_context_and_portuguese_specific_grammar(self):
        lesson_5 = PORTUGUESE_LESSONS[5]
        vocab = {entry[0] for entry in lesson_5["vocabulary"]}
        self.assertIn("o preço", vocab)
        self.assertTrue(any("kwanza" in example[0].lower() for example in lesson_5["examples"]))
        lesson_3 = PORTUGUESE_LESSONS[3]
        grammar_text = " ".join(text for _, text in lesson_3["grammar"]).lower()
        self.assertIn("ter", grammar_text)
        self.assertIn("age", grammar_text)
        lesson_4 = PORTUGUESE_LESSONS[4]
        grammar_text = " ".join(text for _, text in lesson_4["grammar"]).lower()
        self.assertIn("não", grammar_text)


if __name__ == "__main__":
    unittest.main()
