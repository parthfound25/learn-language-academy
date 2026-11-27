import unittest

from angolan_portuguese_lessons import PORTUGUESE_LESSONS


class AngolanPortugueseA1EditorialTests(unittest.TestCase):
    def test_first_five_a1_lessons_are_individually_authored(self):
        expected_titles = {
            1: "Portuguese Alphabet, Sounds and Pronunciation",
            2: "Greetings and Basic Introductions",
            3: "Personal Information and Introducing Yourself",
            4: "Numbers, Counting and Basic Mathematics",
            5: "Days, Months, Seasons and Dates",
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
        for lesson_id in (1, 2, 3, 4, 5):
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
        lesson_4 = PORTUGUESE_LESSONS[4]
        vocab = {entry[0] for entry in lesson_4["vocabulary"]}
        self.assertIn("o preço", vocab)
        self.assertTrue(any("kwanza" in example[0].lower() for example in lesson_4["examples"]))
        lesson_3 = PORTUGUESE_LESSONS[3]
        grammar_text = " ".join(text for _, text in lesson_3["grammar"]).lower()
        self.assertIn("ter", grammar_text)
        self.assertIn("age", grammar_text)
        lesson_4 = PORTUGUESE_LESSONS[4]
        grammar_text = " ".join(text for _, text in lesson_4["grammar"]).lower()
        self.assertIn("não", grammar_text)


class AngolanPortugueseA1NextBatchTests(unittest.TestCase):
    def test_a1_roadmap_ids_and_lesson_depth(self):
        expected = {
            4: "Numbers, Counting and Basic Mathematics",
            5: "Days, Months, Seasons and Dates",
            6: "Time, Clock and Daily Expressions",
            7: "Nouns, Gender and Articles",
            8: "Subject Pronouns and the Verb SER",
            9: "The Verb TER and Possession",
            10: "Common Adjectives and Describing People",
            11: "Family Members and Relationships",
            12: "Colours, Objects and Describing Things",
            13: "Food, Drinks and Basic Restaurant Vocabulary",
            14: "Present Tense and Everyday Activities",
            15: "A1 Comprehensive Revision and Assessment",
            91: "Basic Sentence Patterns, Word Order and Negation",
            92: "Possessive and Demonstrative Determiners",
        }
        for lesson_id, title in expected.items():
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

    def test_next_batch_has_distinct_practice_and_assessment(self):
        for lesson_id in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 91, 92):
            lesson = PORTUGUESE_LESSONS[lesson_id]
            practice = {q[0] for q in lesson["exercises"]}
            assessment = {q[0] for q in lesson["assessment"]}
            self.assertFalse(practice & assessment)
            for question in lesson["exercises"] + lesson["assessment"]:
                prompt, options, answer_index, explanation = question
                self.assertTrue(prompt)
                self.assertEqual(len(options), 4)
                self.assertEqual(len(set(options)), 4)
                self.assertGreaterEqual(answer_index, 0)
                self.assertLess(answer_index, 4)
                self.assertTrue(explanation)

    def test_angolan_context_and_language_specific_grammar(self):
        food = PORTUGUESE_LESSONS[13]
        words = {entry[0] for entry in food["vocabulary"]}
        self.assertIn("o funge", words)
        self.assertIn("a muamba", words)
        self.assertTrue(any("kwanza" in ex[0].lower() for ex in PORTUGUESE_LESSONS[4]["examples"]))
        ter_text = " ".join(x[1] for x in PORTUGUESE_LESSONS[9]["grammar"]).lower()
        self.assertIn("age", ter_text)
        self.assertIn("tenho", ter_text)
        article_text = " ".join(x[1] for x in PORTUGUESE_LESSONS[7]["grammar"]).lower()
        self.assertIn("gender", article_text)
        self.assertIn("plural", article_text)


if __name__ == "__main__":
    unittest.main()
