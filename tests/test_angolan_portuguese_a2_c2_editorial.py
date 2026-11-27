import unittest

from angolan_portuguese_lessons import PORTUGUESE_LESSONS, TOPICS


LEVEL_IDS = {
    "A2": list(range(16, 31)) + [93, 94, 103, 104],
    "B1": list(range(31, 46)) + [95, 96, 105],
    "B2": list(range(46, 61)) + [97, 98, 106],
    "C1": list(range(61, 76)) + [99, 100, 107],
    "C2": list(range(76, 91)) + [101, 102],
}


class AngolanPortugueseA2C2EditorialTests(unittest.TestCase):
    def test_all_remaining_chapters_have_portuguese_specific_titles(self):
        self.assertEqual(sum(map(len, LEVEL_IDS.values())), 90)
        for level, ids in LEVEL_IDS.items():
            for lesson_id in ids:
                with self.subTest(level=level, lesson_id=lesson_id):
                    title = PORTUGUESE_LESSONS[lesson_id]["title"]
                    self.assertTrue(title)
                    self.assertNotIn("french", title.casefold())
                    self.assertNotIn("québec", title.casefold())
                    self.assertEqual(TOPICS[lesson_id]["title"], title)

    def test_all_remaining_lessons_have_expanded_self_study_content(self):
        for level, ids in LEVEL_IDS.items():
            for lesson_id in ids:
                lesson = PORTUGUESE_LESSONS[lesson_id]
                with self.subTest(level=level, lesson_id=lesson_id):
                    self.assertGreaterEqual(len(lesson["objectives"]), 4)
                    self.assertGreaterEqual(len(lesson["vocabulary"]), 8)
                    self.assertGreaterEqual(len(lesson["grammar"]), 5)
                    self.assertGreaterEqual(len(lesson["expressions"]), 5)
                    self.assertGreaterEqual(len(lesson["examples"]), 5)
                    self.assertGreaterEqual(len(lesson["conversations"]), 2)
                    self.assertGreaterEqual(len(lesson["pronunciation"]), 4)
                    self.assertEqual(len(lesson["exercises"]), 6)
                    self.assertEqual(len(lesson["assessment"]), 6)
                    self.assertGreaterEqual(len(lesson["speaking"]), 4)
                    self.assertGreaterEqual(len(lesson["summary"]), 4)
                    self.assertGreaterEqual(len(lesson["homework"]), 3)

    def test_practice_and_assessment_are_distinct_and_valid(self):
        for level, ids in LEVEL_IDS.items():
            for lesson_id in ids:
                lesson = PORTUGUESE_LESSONS[lesson_id]
                practice = {q[0] for q in lesson["exercises"]}
                assessment = {q[0] for q in lesson["assessment"]}
                with self.subTest(level=level, lesson_id=lesson_id):
                    self.assertFalse(practice & assessment)
                    for question in lesson["exercises"] + lesson["assessment"]:
                        prompt, options, answer, explanation = question
                        self.assertTrue(prompt.strip())
                        self.assertEqual(len(options), 4)
                        self.assertEqual(len(set(options)), 4)
                        self.assertGreaterEqual(answer, 0)
                        self.assertLess(answer, 4)
                        self.assertTrue(explanation.strip())

    def test_angolan_regional_and_language_specific_guidance_is_present(self):
        for level, ids in LEVEL_IDS.items():
            for lesson_id in ids:
                lesson = PORTUGUESE_LESSONS[lesson_id]
                with self.subTest(level=level, lesson_id=lesson_id):
                    self.assertTrue(any("Angola" in note or "Angolan" in note for note in lesson["pronunciation"]))
                    self.assertTrue(any("Angolan" in item[3] for item in lesson["vocabulary"]))
                    self.assertTrue(any("Angolan" in item[1] or "Portuguese" in item[1] for item in lesson["grammar"]))

    def test_revision_chapters_and_extension_ids_stay_on_their_roadmap_positions(self):
        expected = {
            30: "A2 Comprehensive Revision and Assessment",
            45: "B1 Comprehensive Revision and Assessment",
            60: "B2 Comprehensive Revision and Assessment",
            75: "C1 Comprehensive Revision and Assessment",
            90: "C2 Final Comprehensive Assessment",
            93: "Partitive Articles, Quantity and Food Expressions",
            94: "Imperatives, Adverbs and Everyday Connectors",
            95: "Past Participles and Auxiliary Choices",
            96: "Integrated Reading, Listening and Writing Strategies",
            97: "Past Subjunctive and Advanced Mood Selection",
            98: "Word Formation, Collocations and Register",
            99: "Critical Listening, Note-taking and Media Analysis",
            100: "Academic Reading, Synthesis and Referencing",
            101: "Mediation, Paraphrasing and Precision Across Registers",
            102: "Integrated C2 Capstone and Independent Language Portfolio",
            103: "Contracted Articles, Prepositions and Verb Complements",
            104: "Portuguese Spelling, Punctuation and Written Conventions",
            105: "Verb and Preposition Patterns with Infinitives",
            106: "Gerund and Non-finite Clauses in Portuguese",
            107: "Angolan Portuguese Sociolinguistics, Identity and Register",
        }
        for lesson_id, title in expected.items():
            with self.subTest(lesson_id=lesson_id):
                self.assertEqual(PORTUGUESE_LESSONS[lesson_id]["title"], title)
                self.assertEqual(TOPICS[lesson_id]["title"], title)

    def test_level_specific_grammar_is_not_replaced_by_french_terminology(self):
        expected = {
            "A2": "pretérito perfeito",
            "B1": "pretérito perfeito",
            "B2": "future subjunctive",
            "C1": "mood",
            "C2": "precision",
        }
        for level, ids in LEVEL_IDS.items():
            grammar = " ".join(part for lesson_id in ids for pair in PORTUGUESE_LESSONS[lesson_id]["grammar"] for part in pair).casefold()
            self.assertIn(expected[level], grammar)

    def test_portuguese_examples_do_not_embed_english_scenario_text(self):
        from angolan_portuguese_a2_c2_editorial import SCENARIO_PT, SCENARIOS
        for level, ids in LEVEL_IDS.items():
            self.assertEqual(len(SCENARIO_PT[level]), len(SCENARIOS[level]))
            for lesson_id in ids:
                lesson = PORTUGUESE_LESSONS[lesson_id]
                with self.subTest(level=level, lesson_id=lesson_id):
                    vocabulary_examples = [entry[4] for entry in lesson["vocabulary"]]
                    example_sentences = [entry[0] for entry in lesson["examples"]]
                    self.assertTrue(all("A expressão «" in item for item in vocabulary_examples))
                    self.assertIn("Em contextos como ", example_sentences[0])
                    for english_scenario in SCENARIOS[level]:
                        self.assertFalse(any(english_scenario in item for item in vocabulary_examples + example_sentences))

    def test_a2_dialogues_and_expressions_are_elementary_not_advanced_discourse(self):
        for lesson_id in LEVEL_IDS["A2"]:
            lesson = PORTUGUESE_LESSONS[lesson_id]
            with self.subTest(lesson_id=lesson_id):
                phrases = " ".join(item[0] for item in lesson["expressions"])
                dialogue = " ".join(line for _, turns, _ in lesson["conversations"] for _, line in turns)
                self.assertIn("Quanto custa?", phrases)
                self.assertIn("Pode ajudar-me", phrases)
                self.assertIn("Bom dia.", dialogue)
                self.assertNotIn("delimitar o objectivo", dialogue)


if __name__ == "__main__":
    unittest.main()
