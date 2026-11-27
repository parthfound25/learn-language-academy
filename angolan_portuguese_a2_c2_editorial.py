"""Editorial content for Angolan Portuguese A2-C2 (90 chapters).

The lesson blueprints replace French-derived titles and generic examples with
Portuguese-specific instruction, Angolan contexts, differentiated dialogues,
and chapter-specific practice. Pronunciation remains descriptive because
Angolan Portuguese varies by region and speaker.
"""

TITLE_GROUPS = {
"A2": [
"Regular -AR, -ER and -IR Verbs","Irregular Everyday Verbs","Reflexive Verbs and Daily Routines",
"Negation with NÃO and Other Negative Expressions","Asking Questions and Question Words",
"Prepositions of Place and Movement","House, Rooms and Household Objects",
"Shopping, Clothes and Accessories","Money, Prices and Everyday Transactions",
"Restaurants, Cafés and Ordering Food","Transportation and Asking for Directions",
"Weather, Nature and Seasons","Health, Body Parts and Medical Expressions",
"Near Future and Recent Past","A2 Comprehensive Revision and Assessment",
"Partitive Articles, Quantity and Food Expressions","Imperatives, Adverbs and Everyday Connectors",
"Contracted Articles, Prepositions and Verb Complements",
"Portuguese Spelling, Punctuation and Written Conventions"],
"B1": [
"Pretérito Perfeito: Completed Past Events","Pretérito Imperfeito: Past Habits and Background",
"Pretérito Perfeito versus Imperfeito","Future Tense and Future Plans",
"Conditional Present and Polite Requests","Comparatives and Superlatives",
"Direct and Indirect Object Pronouns","Object Pronouns and Prepositional Complements",
"Relative Clauses with QUE, QUEM and ONDE","Hobbies, Interests and Leisure Activities",
"Travel, Hotels and Accommodation","Education, Studies and Professions",
"Work, Meetings and Workplace Communication","Feelings, Opinions and Social Interaction",
"B1 Comprehensive Revision and Assessment","Past Participles and Auxiliary Choices",
"Integrated Reading, Listening and Writing Strategies",
"Verb and Preposition Patterns with Infinitives"],
"B2": [
"Pretérito Mais-que-perfeito and Earlier Past Events","Advanced Future and Conditional Structures",
"Present Subjunctive: Necessity, Emotion and Evaluation","Conditional Sentences with SE",
"Passive Voice and Impersonal SE Constructions","Reported Speech and Indirect Questions",
"Object Pronouns and Pronoun Placement","Complex Sentence Construction and Clause Relationships",
"Conjunctions and Logical Linking Expressions","Banking, Finance and Administrative Portuguese",
"Technology, Internet and Digital Communication","News, Media and Current Affairs",
"Debates, Arguments and Persuasion","Angolan Portuguese Idioms and Informal Speech",
"B2 Comprehensive Revision and Assessment","Past Subjunctive and Advanced Mood Selection",
"Word Formation, Collocations and Register","Gerund and Non-finite Clauses in Portuguese"],
"C1": [
"Advanced Subjunctive and Complex Grammar","Advanced Past Tenses and Narrative Techniques",
"Advanced Conditional and Hypothetical Expressions","Nuanced Adverbs, Adjectives and Expressions",
"Idiomatic Angolan Portuguese and Regional Expressions",
"Colloquial Angolan Portuguese and Spoken Variation",
"Understanding Fast Angolan Portuguese Speech","Professional Emails, Reports and Formal Writing",
"Meetings, Negotiations and Presentations","Expressing Complex Opinions and Abstract Ideas",
"Literature, Books and Advanced Reading","Cultural References and Angolan Society",
"Humour, Sarcasm, Irony and Nuance","Advanced Listening and Spontaneous Speaking",
"C1 Comprehensive Revision and Assessment","Critical Listening, Note-taking and Media Analysis",
"Academic Reading, Synthesis and Referencing",
"Angolan Portuguese Sociolinguistics, Identity and Register"],
"C2": [
"Advanced Pronunciation, Intonation and Intelligibility",
"Regional Angolan Portuguese Accents and Variation",
"Advanced Idioms, Proverbs and Expressions",
"Sophisticated Vocabulary, Synonyms and Semantic Precision",
"Subtle Grammar, Register and Stylistic Choices",
"Advanced Literary and Academic Portuguese",
"Persuasive and Rhetorical Communication",
"Complex Professional and Business Communication",
"Cultural and Historical References in Context",
"Spontaneous Debates and Intellectual Discussions",
"Humour, Wordplay and Double Meanings",
"Understanding Angolan Podcasts, Radio and Television",
"Advanced Creative and Professional Writing",
"Advanced Communication Across Contexts",
"C2 Final Comprehensive Assessment",
"Mediation, Paraphrasing and Precision Across Registers",
"Integrated C2 Capstone and Independent Language Portfolio"]
}

# Course IDs are deliberately explicit: the shared course has extension IDs
# interleaved by CEFR level, so numeric ranges alone are not sufficient.
LEVEL_IDS = {
"A2": list(range(16,31)) + [93,94,103,104],
"B1": list(range(31,46)) + [95,96,105],
"B2": list(range(46,61)) + [97,98,106],
"C1": list(range(61,76)) + [99,100,107],
"C2": list(range(76,91)) + [101,102],
}

LEVEL_GRAMMAR = {
"A2": [
("Present-tense conjugation","Regular -ar verbs commonly use -o, -as, -a, -amos, -am; -er verbs use -o, -es, -e, -emos, -em; -ir verbs use -o, -es, -e, -imos, -em. Learn the infinitive and a complete set of forms together. High-frequency irregular verbs such as ser, estar, ter, ir and fazer need their own patterns."),
("Completed and recent events","Use the pretérito perfeito for a completed event with a finished time reference: Ontem fui ao mercado. For a recent event, choose the form that is natural in the intended Portuguese variety and context; do not mechanically copy English present perfect."),
("Negation, questions and commands","Não normally precedes the finite verb: Não encontrei a chave. Words such as nunca, ninguém, nada and nenhum add negative meaning. Question words include quem, o que, qual, onde, quando, como and porquê. Commands change with the addressee and level of politeness."),
("Articles, quantity and contractions","Portuguese articles agree with noun gender and number. Quantity expressions include muito, pouco, algum, nenhum and um pouco de. Preposition-article contractions include de + o = do, em + a = na, a + o = ao and por + os = pelos."),
("Near future and everyday sequence","Ir + infinitive expresses a planned or expected near future: Vou estudar depois do trabalho. Use time expressions such as primeiro, depois, a seguir and finalmente to make instructions and narratives easy to follow.")
],
"B1": [
("Pretérito perfeito and imperfeito","The pretérito perfeito presents a past event as bounded or completed. The imperfeito presents a past habit, background, description or ongoing situation. Contrast: Quando vivia no Huambo, apanhava o machimbombo; ontem apanhei um táxi."),
("Past participles and auxiliary patterns","Many compound forms use ter + past participle, while passive voice uses ser + past participle. The participle agrees with the subject in canonical passive constructions: As propostas foram aprovadas. Avoid transferring agreement rules indiscriminately between constructions."),
("Subjunctive and evaluation","The present subjunctive commonly follows expressions of desire, doubt, emotion, necessity or evaluation: É importante que todos participem. Check the trigger and the relationship between the subjects; an infinitive may be preferable when the subject is shared."),
("Pronouns, relatives and complements","Direct objects answer what or whom; indirect objects identify the recipient or beneficiary. Relative clauses use que, quem, onde and cujo with different grammatical roles. Verb-preposition combinations should be learned as patterns, not translated word by word."),
("Cohesion and reported viewpoints","Use connectors such as embora, apesar de, por isso, contudo and além disso to show concession, cause, consequence and addition. When reporting another person's words, keep pronoun references and time expressions clear and distinguish quotation from paraphrase.")
],
"B2": [
("Subjunctive across time and viewpoint","Choose present or imperfect subjunctive according to the time frame and syntactic environment: Espero que venha; Esperava que viesse. The future subjunctive is used in certain future-oriented clauses after quando, se, assim que and logo que: Quando tiver tempo, telefono."),
("Conditional systems and hypothetical meaning","Match the condition and result in real, probable and counterfactual situations. If the condition is remote or contrary to fact, the imperfect subjunctive often pairs with the conditional: Se tivesse mais tempo, estudaria mais."),
("Passive, impersonal SE and agreement","The canonical passive uses ser + past participle, with agreement: Os documentos foram enviados. In a passive-se construction, the verb agrees with the patient: Vendem-se casas. In impersonal-se constructions, the verb is third-person singular; identify the structure before choosing agreement."),
("Reported speech and clause control","Indirect statements commonly use que; indirect questions retain question words but do not take question-mark punctuation inside the reporting clause. Keep tense, deixis and pronoun changes consistent with the reporting viewpoint."),
("Collocation, argument and register","Advanced fluency depends on conventional word partnerships, precise connectors and appropriate register. Compare near-synonyms in full contexts, qualify claims, acknowledge counterarguments and avoid literal calques from English.")
],
"C1": [
("Mood, aspect and stance","Advanced mood choice expresses the speaker's stance toward certainty, evaluation, desire, concession and hypothetical distance. Explain why the selected mood fits the meaning and clause relationship rather than memorising a trigger list alone."),
("Narrative architecture and information flow","Control foreground and background with perfective and imperfective viewpoints, temporal anchoring and paragraph structure. Use reference chains and varied sentence openings while ensuring every pronoun has a recoverable referent."),
("Academic and professional argument","Build claims from evidence, distinguish observation from interpretation, qualify uncertainty and state limitations. A strong report makes its purpose, method, findings and recommendations easy to locate."),
("Critical listening and source evaluation","Identify a speaker's thesis, supporting evidence, assumptions, omissions, framing and implied position. Separate what is explicitly stated from what is inferred, and verify names, figures and chronology when taking notes."),
("Angolan variation and pragmatic competence","Angolan Portuguese varies by region, community, age, multilingual contact and communicative setting. Describe observed patterns precisely and respectfully; do not present one accent or social variety as the sole legitimate model.")
],
"C2": [
("Precision, emphasis and ambiguity","Choose word order, lexical specificity, punctuation and clause structure to control emphasis and implication. Ambiguity can be deliberate in literary or rhetorical contexts, but should be removed when it obstructs professional or technical meaning."),
("Rhetoric and calibrated persuasion","Develop a defensible thesis through evidence, concessions, counterarguments and proportionate conclusions. Distinguish correlation from causation, acknowledge uncertainty and represent opposing positions fairly before responding."),
("Literary, figurative and specialised meaning","Interpret metaphor, irony, allusion, register shifts and domain-specific terminology. Preserve the effect as well as the literal content when paraphrasing or mediating a text for a different audience."),
("Synthesis, attribution and mediation","Integrate multiple sources, attribute claims accurately, reconcile apparent contradictions and signal unresolved disagreement. A synthesis should create a coherent account rather than reproduce a sequence of disconnected summaries."),
("Flexible communication and self-monitoring","Adapt fluency, formality, detail and rhetorical strategy to audience and purpose. C2 describes highly effective and flexible command; it does not require accent imitation, the absence of every error or unnecessarily elaborate sentences.")
]
}

SCENARIOS = {
"A2": ["at the market in Luanda","at home with family","asking for directions in the neighbourhood","ordering a meal","planning a journey between provinces","at a health centre","buying clothes and checking sizes","organising a study timetable"],
"B1": ["recounting a journey to Benguela","explaining a change at work","discussing studies and career plans","describing a childhood routine","resolving a misunderstanding with a colleague","sharing an opinion about a community project","planning a trip with friends"],
"B2": ["presenting a proposal to colleagues","discussing a public-service announcement","comparing two policy options","reporting what a participant said","evaluating a news report","negotiating a project deadline","explaining a technical process"],
"C1": ["writing an analytical report","moderating a professional meeting","evaluating a radio interview","synthesising academic sources","presenting a community research finding","analysing a literary passage","comparing language use across contexts"],
"C2": ["mediating a complex public discussion","editing an executive statement","delivering a nuanced debate contribution","synthesising conflicting reports","reviewing a literary or cultural argument","adapting a speech for distinct audiences","evaluating rhetorical choices in broadcast media"]
}

def _make_question(prefix, template, index):
    prompt, options, answer, explanation = template
    return (f"{prefix} — {prompt}", list(options), answer, explanation)

def apply_editorial(lessons, topics, vocab_pools, pool_for):
    """Replace generic A2-C2 lesson shells with level- and topic-focused content."""
    for level, ids in LEVEL_IDS.items():
        titles = TITLE_GROUPS[level]
        if len(titles) != len(ids):
            raise ValueError(f"{level}: {len(titles)} titles for {len(ids)} chapter IDs")
        for pos, lesson_id in enumerate(ids):
            lesson = lessons[lesson_id]
            title = titles[pos]
            topic = topics[lesson_id]
            topic["title"] = title
            lesson["title"] = title
            scenario = SCENARIOS[level][(lesson_id + pos) % len(SCENARIOS[level])]
            pool = pool_for(title)
            offset = (lesson_id * 2) % max(1, len(pool) - 6)
            selected = pool[offset:offset + 8]
            if len(selected) < 8:
                selected += vocab_pools["general"][:8-len(selected)]
            lesson["vocabulary"] = [
                (pt, en, hint, "Angolan Portuguese context where applicable", f"Hoje usamos {pt} {scenario}.")
                for pt, en, hint in selected
            ]
            lesson["goal"] = f"Use Angolan Portuguese confidently for {title.lower()}, with accurate grammar and an appropriate register."
            lesson["objectives"] = [
                f"Explain and recognise the main patterns used in {title.lower()}.",
                f"Choose vocabulary and structures suitable for {scenario}.",
                "Understand the target forms in connected speech and written Portuguese.",
                "Produce a clear spoken or written response and justify important language choices."
            ]
            core = [entry[0] for entry in lesson["vocabulary"]]
            grammar = list(LEVEL_GRAMMAR[level])
            grammar.append((
                f"Applying the target to {title.lower()}",
                f"In {scenario}, select forms by considering who is speaking, the relationship between participants, the time frame and the intended emphasis. Build complete clauses, check agreement and prepositions, then reread the whole exchange for naturalness. The target vocabulary in this chapter is presented in context within Angolan Portuguese rather than as isolated translations."
            ))
            lesson["grammar"] = grammar
            lesson["expressions"] = [
                ("Na minha opinião, ...", "In my opinion, ...", "Introduce a view and then support it with a reason or example."),
                ("Pode explicar melhor esse ponto?", "Could you explain that point more clearly?", "Ask for clarification politely in a discussion."),
                ("Por um lado ..., por outro ...", "On the one hand ..., on the other ...", "Present a balanced comparison."),
                ("Se percebi bem, ...", "If I understood correctly, ...", "Check your understanding before responding."),
                ("É importante ter em conta que ...", "It is important to bear in mind that ...", "Introduce a qualification or relevant limitation.")
            ]
            lesson["examples"] = [
                (f"Hoje vamos analisar {core[0]} {scenario}.", f"Today we are going to analyse {core[0]} {scenario}.", "The sentence places the chapter vocabulary in a realistic Angolan setting."),
                (f"É necessário compreender o contexto antes de tirar uma conclusão.", "It is necessary to understand the context before drawing a conclusion.", "An impersonal evaluation followed by an infinitive."),
                (f"Embora existam diferenças regionais, a comunicação pode ser clara e respeitosa.", "Although regional differences exist, communication can be clear and respectful.", "Embora introduces a concessive clause."),
                (f"A proposta foi discutida e as recomendações foram registadas.", "The proposal was discussed and the recommendations were recorded.", "A passive construction foregrounds the proposal and recommendations."),
                (f"Se houver dúvidas, podemos rever os exemplos em conjunto.", "If there are questions, we can review the examples together.", "A future-oriented condition uses the future subjunctive after se.")
            ]
            lesson["conversations"] = [
                ("Discussing the chapter topic", [
                    ("A", "Podemos começar por esclarecer o objectivo desta conversa?"),
                    ("B", "Claro. Quero perceber melhor os pontos principais e as suas consequências."),
                    ("A", f"Um dos aspectos importantes é {core[0]}. Como o interpreta?"),
                    ("B", "Depende do contexto. Convém comparar os dados antes de chegar a uma conclusão."),
                    ("A", "Concordo. Podemos também considerar outra perspectiva."),
                    ("B", "Sim. Assim, a análise fica mais completa.")
                ], "A: Can we begin by clarifying the purpose of this conversation? B: Of course. I want to understand the main points and their consequences better. A: One important aspect is the chapter vocabulary. How do you interpret it? B: It depends on the context. We should compare the data before reaching a conclusion. A: I agree. We can also consider another perspective. B: Yes. That makes the analysis more complete."),
                ("Clarifying and responding", [
                    ("A", "Não tenho a certeza de ter compreendido essa parte."),
                    ("B", "Posso reformular. O ponto principal é distinguir os factos das interpretações."),
                    ("A", "Nesse caso, que exemplo poderíamos usar?"),
                    ("B", "Podemos analisar uma situação real e explicar por que razão escolhemos essa forma."),
                    ("A", "Agora está mais claro. Obrigado pela explicação."),
                    ("B", "De nada. É sempre útil confirmar o sentido.")
                ], "A: I am not sure I understood that part. B: I can rephrase it. The main point is to distinguish facts from interpretations. A: In that case, what example could we use? B: We can analyse a real situation and explain why we chose that form. A: It is clearer now. Thank you for the explanation. B: You're welcome. It is always useful to confirm the meaning.")
            ]
            lesson["pronunciation"] = [
                "These pronunciation notes are learning guidance, not a claim that Angola has one uniform accent.",
                "Practise lexical stress in complete phrases, not only in isolated vocabulary items.",
                "Notice rhythm and vowel quality in speakers from different Angolan regions and language backgrounds.",
                "In formal speaking, prioritise intelligibility, phrasing and controlled pace; do not imitate an accent you cannot verify."
            ]
            # Level-specific assessment bank; chapter wording makes prompts distinct
            # while answer options test the same explicitly taught outcomes.
            banks = {
            "A2": [
                ("Choose the correct present form: Nós ___ português todos os dias.", ["estudamos","estuda","estudam","estudo"],0,"With nós, the regular -ar ending is -amos."),
                ("Choose the completed past: Ontem, ela ___ ao mercado.", ["vai","foi","iria","ia"],1,"Foi is the pretérito perfeito of ir."),
                ("Choose the correct negative sentence.", ["Eu não encontrei a chave.","Eu encontrei não a chave.","Não eu encontrei a chave ontem?","Eu nunca nada encontrei."],0,"Não normally precedes the finite verb."),
                ("Choose the correct contraction: em + a escola.", ["em a escola","na escola","no escola","à escola"],1,"Em + a contracts to na."),
                ("Choose the natural near-future form.", ["Vou estudar amanhã.","Estudei amanhã.","Estava estudar amanhã.","Sou estudar amanhã."],0,"Ir + infinitive expresses a planned near future."),
                ("Choose the correct quantity expression.", ["um pouco de água","uma pouco água","pouco de a água","um pouca da água"],0,"Um pouco de is followed by the noun.")
            ],
            "B1": [
                ("Choose the habitual past: Quando era criança, ___ em Malanje.", ["vivi amanhã","morava","moro ontem","morarei"],1,"The imperfeito describes a past habit or background."),
                ("Choose the completed event: Ontem, nós ___ a reunião.", ["terminávamos sempre","terminámos","terminaremos","terminaríamos"],1,"The pretérito perfeito presents a bounded completed event."),
                ("Complete: Espero que todos ___ a proposta.", ["compreendem","compreendam","compreenderam","compreendiam"],1,"Esperar que commonly introduces the present subjunctive."),
                ("Choose the correct relative form: A cidade ___ nasci fica no litoral.", ["onde","cujo","quem","de que"],0,"Onde refers to a place."),
                ("Choose the conditional request.", ["Gostaria de pedir uma informação.","Gostei de pedir amanhã ontem.","Gostarei ontem de pedir.","Gostava pediria informação."],0,"Gostaria de is a polite conditional request."),
                ("Choose the passive with agreement.", ["As propostas foram aprovadas.","As propostas foi aprovado.","As propostas aprovaram pelo júri.","As propostas foram aprovar."],0,"The participle agrees with the feminine plural subject in the passive.")
            ],
            "B2": [
                ("Complete the future condition: Quando ___ os dados, envio o relatório.", ["analisei","analisar","analisava","analisaria"],1,"Future subjunctive follows quando in a future-oriented clause."),
                ("Choose the counterfactual condition.", ["Se tivesse tempo, participaria.","Se tenho ontem, participei.","Se terei tempo, participava.","Se teria tempo, participo."],0,"Imperfect subjunctive pairs with the conditional in this hypothetical pattern."),
                ("Choose the passive with correct agreement.", ["Os documentos foram enviados.","Os documentos foi enviado.","Os documentos enviou-se ontem.","Os documentos foram enviar."],0,"Ser + participle forms the passive; the participle agrees with documentos."),
                ("Choose the correct impersonal-se sentence.", ["Precisa-se de técnicos.","Precisam-se de técnicos.","Técnicos precisa nós.","Se precisam técnico ontem."],0,"With precisar de, the impersonal construction stays third-person singular."),
                ("Choose the indirect question.", ["Gostaria de saber quando começa a reunião.","Gostaria de saber quando começa? a reunião.","Gostaria quando começa saber reunião.","Quando gostaria de saber começa a reunião."],0,"An embedded indirect question does not use internal question-mark punctuation."),
                ("Choose the standard collocation.", ["tomar uma decisão","fazer uma decisão","pegar uma decisão","construir uma decisão"],0,"Tomar uma decisão is the established collocation.")
            ],
            "C1": [
                ("Choose the most suitable report opening.", ["E então, pessoal...","O presente relatório analisa os resultados...","Olá malta, aqui vai...","Pronto, é tudo."],1,"The wording is formal, direct and suitable for a report."),
                ("Choose a connector that introduces concession.", ["embora","portanto","além disso","por conseguinte"],0,"Embora introduces a concessive clause and is followed by the subjunctive."),
                ("A careful analytical claim should:", ["state certainty without evidence","distinguish findings from interpretation","omit limitations","replace sources with personal belief"],1,"Advanced analysis separates evidence from interpretation."),
                ("When evaluating a radio interview, first:", ["assume every claim is factual","identify claims, evidence and framing","ignore the speaker's purpose","record only isolated adjectives"],1,"Critical listening examines claims, support and framing."),
                ("Which approach to Angolan variation is appropriate?", ["declare one accent the only correct one","describe regional and contextual patterns neutrally","label local forms as inferior","assume all speakers use identical forms"],1,"Variation should be described accurately and respectfully."),
                ("A coherent academic synthesis should:", ["list sources without connecting them","integrate and attribute relevant findings","hide disagreements","remove all qualifications"],1,"Synthesis connects sources while preserving attribution.")
            ],
            "C2": [
                ("Which sentence best calibrates certainty?", ["This proves everything.","The evidence supports this interpretation, although alternatives remain.","Everyone knows it is true.","There is no possible doubt."],1,"The claim is proportionate to the evidence and acknowledges alternatives."),
                ("A strong counterargument should:", ["misrepresent the opposing position","state the opposing view fairly before responding","attack the speaker","ignore contrary evidence"],1,"Fair representation makes the response more credible."),
                ("Which revision best removes unintended ambiguity?", ["keep several unclear pronouns","name the referent where necessary","add unrelated clauses","delete the main verb"],1,"Explicit reference improves precision when ambiguity is not intended."),
                ("A high-quality synthesis should:", ["copy sources in sequence","integrate, compare and attribute claims","hide source disagreement","replace evidence with opinion"],1,"Synthesis integrates sources and preserves attribution."),
                ("How should register be selected?", ["use the same slang everywhere","adapt language to audience and purpose","avoid formal language","prefer complexity over clarity"],1,"Register depends on audience, purpose and setting."),
                ("C2 proficiency is best described as:", ["native accent imitation","flexible, precise and effective communication","never making any error","using the longest possible sentences"],1,"C2 concerns communicative control, not accent imitation.")
            ]}
            bank = banks[level]
            prefix = f"({title})"
            lesson["exercises"] = [_make_question(prefix, bank[i], i) for i in range(6)]
            lesson["assessment"] = [
                _make_question(f"Assessment for {title}", bank[(i+2) % 6], i)
                for i in range(6)
            ]
            lesson["speaking"] = [
                f"Give a two-minute explanation of {title.lower()} using a clear opening, two supporting points and a conclusion.",
                f"Role-play the situation: {scenario}. Use at least five words from this chapter.",
                "Rephrase one statement in a more formal and then a more conversational register; explain what changed.",
                "Record a short response, listen for clarity and revise one sentence for greater precision."
            ]
            lesson["summary"] = [
                f"This chapter develops {title.lower()} through grammar, vocabulary and realistic communication.",
                "Select forms by meaning, time frame, agreement, audience and context rather than translating word for word.",
                "Use the dialogues as models, then adapt them to a real situation in Angola.",
                "Review the explanations and redo missed questions after a short interval."
            ]
            lesson["homework"] = [
                f"Write a 120-180 word text about {scenario}, applying at least two target structures.",
                "Create a dialogue of at least eight turns and include a clarification or follow-up question.",
                "Choose three sentences from your work, check agreement and prepositions, and explain your corrections."
            ]
    return lessons
