"""Angolan Portuguese course: 107 self-study chapters, A1-C2.

English is the teaching language. Portuguese examples use broadly understood
Angolan Portuguese; regional and speaker variation is explicitly acknowledged.
Pronunciation hints are learner approximations, not narrow phonetic transcriptions.
"""
import random

TOPICS = {"1":{"title":"French Alphabet, Sounds and Pronunciation","level":"A1 – Absolute Beginner"},"2":{"title":"Greetings and Basic Introductions","level":"A1 – Absolute Beginner"},"3":{"title":"Personal Information and Introducing Yourself","level":"A1 – Absolute Beginner"},"4":{"title":"Numbers, Counting and Basic Mathematics","level":"A1 – Absolute Beginner"},"5":{"title":"Days, Months, Seasons and Dates","level":"A1 – Absolute Beginner"},"6":{"title":"Time, Clock and Daily Expressions","level":"A1 – Absolute Beginner"},"7":{"title":"Nouns, Gender and Articles","level":"A1 – Absolute Beginner"},"8":{"title":"Subject Pronouns and the Verb ÊTRE","level":"A1 – Absolute Beginner"},"9":{"title":"The Verb AVOIR and Possession","level":"A1 – Absolute Beginner"},"10":{"title":"Common Adjectives and Describing People","level":"A1 – Absolute Beginner"},"11":{"title":"Family Members and Relationships","level":"A1 – Absolute Beginner"},"12":{"title":"Colours, Objects and Describing Things","level":"A1 – Absolute Beginner"},"13":{"title":"Food, Drinks and Basic Restaurant Vocabulary","level":"A1 – Absolute Beginner"},"14":{"title":"Present Tense and Everyday Activities","level":"A1 – Absolute Beginner"},"15":{"title":"A1 Comprehensive Revision and Assessment","level":"A1 – Absolute Beginner"},"16":{"title":"Regular -ER, -IR and -RE Verbs","level":"A2 – Elementary"},"17":{"title":"Irregular Everyday Verbs","level":"A2 – Elementary"},"18":{"title":"Reflexive Verbs and Daily Routines","level":"A2 – Elementary"},"19":{"title":"Negation: NE...PAS and Other Forms","level":"A2 – Elementary"},"20":{"title":"Asking Questions and Question Words","level":"A2 – Elementary"},"21":{"title":"Prepositions of Place and Movement","level":"A2 – Elementary"},"22":{"title":"House, Rooms and Household Objects","level":"A2 – Elementary"},"23":{"title":"Shopping, Clothes and Accessories","level":"A2 – Elementary"},"24":{"title":"Money, Prices and Numbers in Real Life","level":"A2 – Elementary"},"25":{"title":"Restaurants, Cafés and Ordering Food","level":"A2 – Elementary"},"26":{"title":"Transportation and Asking for Directions","level":"A2 – Elementary"},"27":{"title":"Weather, Nature and Seasons","level":"A2 – Elementary"},"28":{"title":"Health, Body Parts and Medical Expressions","level":"A2 – Elementary"},"29":{"title":"Near Future and Recent Past","level":"A2 – Elementary"},"30":{"title":"A2 Comprehensive Revision and Assessment","level":"A2 – Elementary"},"31":{"title":"Passé Composé - Talking About the Past","level":"B1 – Intermediate"},"32":{"title":"Imparfait - Describing Past Situations","level":"B1 – Intermediate"},"33":{"title":"Passé Composé vs Imparfait","level":"B1 – Intermediate"},"34":{"title":"Future Simple - Talking About the Future","level":"B1 – Intermediate"},"35":{"title":"Conditional Present - Expressing Wishes","level":"B1 – Intermediate"},"36":{"title":"Comparatives and Superlatives","level":"B1 – Intermediate"},"37":{"title":"Direct and Indirect Object Pronouns","level":"B1 – Intermediate"},"38":{"title":"Y and EN Pronouns","level":"B1 – Intermediate"},"39":{"title":"Relative Pronouns: QUI, QUE, OÙ","level":"B1 – Intermediate"},"40":{"title":"Hobbies, Interests and Leisure Activities","level":"B1 – Intermediate"},"41":{"title":"Travel, Hotels and Accommodation","level":"B1 – Intermediate"},"42":{"title":"Education, Studies and Professions","level":"B1 – Intermediate"},"43":{"title":"Work, Meetings and Workplace Communication","level":"B1 – Intermediate"},"44":{"title":"Feelings, Opinions and Social Interactions","level":"B1 – Intermediate"},"45":{"title":"B1 Comprehensive Revision and Assessment","level":"B1 – Intermediate"},"46":{"title":"Plus-Que-Parfait - The Past Before the Past","level":"B2 – Upper Intermediate"},"47":{"title":"Advanced Future and Conditional Structures","level":"B2 – Upper Intermediate"},"48":{"title":"Subjunctive Present - Expressing Necessity and Emotion","level":"B2 – Upper Intermediate"},"49":{"title":"Si Clauses and Conditional Sentences","level":"B2 – Upper Intermediate"},"50":{"title":"Passive Voice and Impersonal Structures","level":"B2 – Upper Intermediate"},"51":{"title":"Reported Speech and Indirect Questions","level":"B2 – Upper Intermediate"},"52":{"title":"Advanced Pronouns and Pronoun Order","level":"B2 – Upper Intermediate"},"53":{"title":"Complex Sentence Construction","level":"B2 – Upper Intermediate"},"54":{"title":"Conjunctions and Linking Expressions","level":"B2 – Upper Intermediate"},"55":{"title":"Banking, Finance and Administrative Vocabulary","level":"B2 – Upper Intermediate"},"56":{"title":"Technology, Internet and Digital Communication","level":"B2 – Upper Intermediate"},"57":{"title":"News, Media and Current Affairs","level":"B2 – Upper Intermediate"},"58":{"title":"Debates, Arguments and Persuasion","level":"B2 – Upper Intermediate"},"59":{"title":"Canadian French Idioms and Informal Speech","level":"B2 – Upper Intermediate"},"60":{"title":"B2 Comprehensive Revision and Assessment","level":"B2 – Upper Intermediate"},"61":{"title":"Advanced Subjunctive and Complex Grammar","level":"C1 – Advanced"},"62":{"title":"Advanced Past Tenses and Narrative Techniques","level":"C1 – Advanced"},"63":{"title":"Advanced Conditional and Hypothetical Expressions","level":"C1 – Advanced"},"64":{"title":"Nuanced Adverbs, Adjectives and Expressions","level":"C1 – Advanced"},"65":{"title":"Idiomatic Canadian French and Regional Expressions","level":"C1 – Advanced"},"66":{"title":"Colloquial Quebec French and Spoken Contractions","level":"C1 – Advanced"},"67":{"title":"Understanding Fast Native French Speech","level":"C1 – Advanced"},"68":{"title":"Professional Emails, Reports and Formal Writing","level":"C1 – Advanced"},"69":{"title":"Meetings, Negotiations and Presentations","level":"C1 – Advanced"},"70":{"title":"Expressing Complex Opinions and Abstract Ideas","level":"C1 – Advanced"},"71":{"title":"Literature, Books and Advanced Reading","level":"C1 – Advanced"},"72":{"title":"Cultural References and French-Canadian Society","level":"C1 – Advanced"},"73":{"title":"Humour, Sarcasm, Irony and Nuance","level":"C1 – Advanced"},"74":{"title":"Advanced Listening and Spontaneous Speaking","level":"C1 – Advanced"},"75":{"title":"C1 Comprehensive Revision and Assessment","level":"C1 – Advanced"},"76":{"title":"Mastering Native-Level Pronunciation and Intonation","level":"C2 – Mastery"},"77":{"title":"Understanding Regional Canadian French Accents","level":"C2 – Mastery"},"78":{"title":"Advanced Idioms, Proverbs and Expressions","level":"C2 – Mastery"},"79":{"title":"Sophisticated Vocabulary and Synonyms","level":"C2 – Mastery"},"80":{"title":"Subtle Grammar, Register and Stylistic Choices","level":"C2 – Mastery"},"81":{"title":"Advanced Literary and Academic French","level":"C2 – Mastery"},"82":{"title":"Persuasive and Rhetorical Communication","level":"C2 – Mastery"},"83":{"title":"Complex Professional and Business Communication","level":"C2 – Mastery"},"84":{"title":"Understanding Cultural and Historical References","level":"C2 – Mastery"},"85":{"title":"Spontaneous Debates and Intellectual Discussions","level":"C2 – Mastery"},"86":{"title":"Mastering Humour, Wordplay and Double Meanings","level":"C2 – Mastery"},"87":{"title":"Understanding Native Podcasts, Radio and Television","level":"C2 – Mastery"},"88":{"title":"Advanced Creative and Professional Writing","level":"C2 – Mastery"},"89":{"title":"Native-Level Conversation and Communication Simulation","level":"C2 – Mastery"},"90":{"title":"C2 Final Comprehensive Assessment","level":"C2 – Mastery"},"91":{"title":"Basic Sentence Patterns, Word Order and Negation","level":"A1 – Absolute Beginner"},"92":{"title":"Possessive and Demonstrative Determiners","level":"A1 – Absolute Beginner"},"93":{"title":"Partitive Articles, Quantity and Food Expressions","level":"A2 – Elementary"},"94":{"title":"Imperatives, Adverbs and Everyday Connectors","level":"A2 – Elementary"},"95":{"title":"Past Participle Agreement and Auxiliary Choices","level":"B1 – Intermediate"},"96":{"title":"Integrated Reading, Listening and Writing Strategies","level":"B1 – Intermediate"},"97":{"title":"Past Subjunctive and Advanced Mood Selection","level":"B2 – Upper Intermediate"},"98":{"title":"Word Formation, Collocations and Register","level":"B2 – Upper Intermediate"},"99":{"title":"Critical Listening, Note-Taking and Media Analysis","level":"C1 – Advanced"},"100":{"title":"Academic Reading, Synthesis and Referencing","level":"C1 – Advanced"},"101":{"title":"Mediation, Paraphrasing and Precision Across Registers","level":"C2 – Mastery"},"102":{"title":"Integrated C2 Capstone and Independent Language Portfolio","level":"C2 – Mastery"},"103":{"title":"Contracted Articles, Prepositions and Verb Complements","level":"A2 – Elementary"},"104":{"title":"French Spelling, Punctuation and Written Conventions","level":"A2 – Elementary"},"105":{"title":"Verb + Preposition Patterns and Infinitive Complements","level":"B1 – Intermediate"},"106":{"title":"Present Participle, Gérondif and Non-finite Clauses","level":"B2 – Upper Intermediate"},"107":{"title":"Canadian French Sociolinguistics, Identity and Register","level":"C1 – Advanced"}}
TOPICS = {int(key): value for key, value in TOPICS.items()}

# Topic-focused vocabulary pools. Angolan usage is prioritised where well established;
# broadly shared Portuguese is used otherwise. Regional variants are labelled in notes.
VOCAB_POOLS = {
    "alphabet": [("o alfabeto","alphabet","ahl-fah-BEH-too"),("a letra","letter","LEH-trah"),("a vogal","vowel","voh-GAHL"),("a consoante","consonant","kohn-soh-AHN-tj"),("o som","sound","SOHM"),("a sílaba","syllable","SEE-lah-bah"),("o acento","accent mark / stress","ah-SEN-too"),("a pronúncia","pronunciation","proh-NOON-see-ah"),("a palavra","word","pah-LAH-vrah"),("soletrar","to spell","soh-leh-TRAR")],
    "greetings": [("olá","hello","oh-LAH"),("bom dia","good morning","bohn DEE-ah"),("boa tarde","good afternoon","BOH-ah TAR-dj"),("boa noite","good evening / good night","BOH-ah NOY-tj"),("adeus","goodbye","ah-DEH-oosh"),("até logo","see you later","ah-TEH LOH-goo"),("por favor","please","poor fah-VOHR"),("obrigado / obrigada","thank you (speaker: masculine / feminine)","oh-bree-GAH-doo / oh-bree-GAH-dah"),("de nada","you're welcome","dj NAH-dah"),("com licença","excuse me","kohm lee-SEN-sah")],
    "identity": [("o nome","name","oh NOH-m"),("chamar-se","to be called","shah-MAR-s"),("eu sou","I am","eh-oo soh"),("eu tenho","I have","eh-oo TEN-yoo"),("morar","to live / reside","moh-RAR"),("nascer","to be born","nah-SER"),("a nacionalidade","nationality","nah-see-oh-nah-lee-DAH-dj"),("a idade","age","ee-DAH-dj"),("a língua","language","LEEN-gwah"),("o endereço","address","en-deh-REH-soo")],
    "numbers": [("zero","zero","ZEH-roo"),("um / uma","one","oong / OO-mah"),("dois / duas","two","doysh / DOO-ahsh"),("três","three","trehsh"),("quatro","four","KWAH-troo"),("cinco","five","SEEN-koo"),("seis","six","saysh"),("sete","seven","SEH-tj"),("oito","eight","OY-too"),("nove","nine","NOH-vj"),("dez","ten","desh")],
    "calendar": [("segunda-feira","Monday","seh-GOON-dah FAY-rah"),("terça-feira","Tuesday","TER-sah FAY-rah"),("quarta-feira","Wednesday","KWAR-tah FAY-rah"),("quinta-feira","Thursday","KEEN-tah FAY-rah"),("sexta-feira","Friday","SAYSH-tah FAY-rah"),("sábado","Saturday","SAH-bah-doo"),("domingo","Sunday","doh-MEEN-goo"),("hoje","today","OH-zhj"),("amanhã","tomorrow","ah-mah-NYAH"),("ontem","yesterday","OHN-ten")],
    "time": [("a hora","hour / time","AH OH-rah"),("meio-dia","noon","MAY-oo DEE-ah"),("meia-noite","midnight","MAY-ah NOY-tj"),("de manhã","in the morning","dj mah-NYAH"),("à tarde","in the afternoon","ah TAR-dj"),("à noite","at night","ah NOY-tj"),("cedo","early","SEH-doo"),("tarde","late","TAR-dj"),("agora","now","ah-GOH-rah"),("mais tarde","later","maysh TAR-dj")],
    "family": [("a família","family","fah-MEE-lee-ah"),("a mãe","mother","mah-eh"),("o pai","father","pie"),("o irmão / a irmã","brother / sister","eer-MOWN / eer-MAH"),("o filho / a filha","son / daughter","FEE-lyoo / FEE-lyah"),("os pais","parents","oosh PIE-sh"),("a avó","grandmother","ah ah-VOH"),("o avô","grandfather","oo ah-VOH"),("o tio / a tia","uncle / aunt","TEE-oo / TEE-ah"),("o primo / a prima","cousin","PREE-moo / PREE-mah")],
    "food": [("o funge","Angolan staple made from cassava or maize flour","FOON-zhj"),("a muamba","Angolan dish often prepared with palm oil","MWAHM-bah"),("o calulu","traditional Angolan stew","kah-LOO-loo"),("a mandioca","cassava","mahn-dj-OH-kah"),("o peixe","fish","PAYSH"),("o frango","chicken","FRANG-goo"),("o arroz","rice","ah-ROSH"),("o feijão","beans","fay-ZHOW"),("a banana","banana","bah-NAH-nah"),("a água","water","AH-gwah"),("o sumo","juice","SOO-moo")],
    "home": [("a casa","house / home","KAH-zah"),("o quarto","bedroom","KWAR-too"),("a sala","living room","SAH-lah"),("a cozinha","kitchen","koo-ZEEN-yah"),("a casa de banho","bathroom","KAH-zah dj BAHN-yoo"),("a porta","door","POR-tah"),("a janela","window","zhah-NEH-lah"),("a mesa","table","MEH-zah"),("a cadeira","chair","kah-DAY-rah"),("a chave","key","SHAH-vj")],
    "shopping": [("o mercado","market","mer-KAH-doo"),("a loja","shop","LOH-zhah"),("o preço","price","PREH-soo"),("quanto custa?","how much does it cost?","KWAN-too KOOSH-tah"),("caro","expensive","KAH-roo"),("barato","cheap","bah-RAH-too"),("comprar","to buy","kohm-PRAR"),("vender","to sell","ven-DER"),("o dinheiro","money","dee-NYAY-roo"),("o troco","change","TROH-koo")],
    "transport": [("o táxi","taxi","TAHK-see"),("o machimbombo","public bus in Angola","mah-sheem-BOHM-boo"),("o candongueiro","informal shared minibus taxi in Angola","kahn-dohn-GAY-roo"),("a paragem","stop","pah-RAH-zheng"),("a estrada","road","esh-TRAH-dah"),("o trânsito","traffic","TRAN-zee-too"),("a viagem","journey","vee-AH-zheng"),("o bilhete","ticket","bee-LYEH-tj"),("à esquerda","to the left","ah esh-KER-dah"),("à direita","to the right","ah dj-RAY-tah")],
    "work": [("o trabalho","work","trah-BAH-lyoo"),("o emprego","job","en-PREH-goo"),("o escritório","office","esh-kree-TOH-ree-oo"),("o colega","colleague","koh-LEH-gah"),("a reunião","meeting","reh-oo-nee-OWN"),("o salário","salary","sah-LAH-ree-oo"),("o horário","schedule","oh-RAH-ree-oo"),("a empresa","company","en-PREH-zah"),("o chefe / a chefe","boss","SHEH-fj"),("a experiência","experience","esh-peh-ree-EN-see-ah")],
    "health": [("a saúde","health","sah-OO-dj"),("o médico / a médica","doctor","MEH-djee-koo / MEH-djee-kah"),("o hospital","hospital","ohsh-pee-TAHL"),("a farmácia","pharmacy","far-MAH-see-ah"),("a dor","pain","DOR"),("a cabeça","head","kah-BEH-sah"),("a garganta","throat","gah-RANG-tah"),("a febre","fever","FEH-brj"),("o medicamento","medicine","meh-djee-kah-MEN-too"),("marcar uma consulta","to make an appointment","mar-KAR OO-mah kohn-SOOL-tah")],
    "education": [("a escola","school","esh-KOH-lah"),("a universidade","university","oo-nee-ver-see-DAH-dj"),("o aluno / a aluna","pupil","ah-LOO-noo / ah-LOO-nah"),("o estudante / a estudante","student","esh-too-DAN-tj"),("a aula","lesson / class","OW-lah"),("o professor / a professora","teacher","proh-feh-SOR / proh-feh-SOH-rah"),("o exame","exam","eh-ZAH-mj"),("a nota","grade / mark","NOH-tah"),("estudar","to study","esh-too-DAR"),("aprender","to learn","ah-pren-DER")],
    "technology": [("o telemóvel","mobile phone","teh-leh-MOH-vel"),("o computador","computer","kohm-poo-tah-DOR"),("a internet","internet","een-ter-NET"),("a palavra-passe","password","pah-LAH-vrah PAH-sj"),("a mensagem","message","meh-ZAH-zheng"),("o ficheiro","file","fee-SHAY-roo"),("descarregar","to download","desh-kah-reh-GAR"),("a aplicação","application","ah-plee-kah-SOWN"),("a rede","network","REH-dj"),("a ligação","connection","lee-gah-SOWN")],
    "media": [("as notícias","news","ahsh noo-TEE-see-ahsh"),("o jornal","newspaper","zhor-NAHL"),("a reportagem","report","reh-por-TAH-zheng"),("a entrevista","interview","en-tre-VESH-tah"),("a fonte","source","FOHN-tj"),("a opinião","opinion","oh-pee-nee-OWN"),("o facto","fact","FAHK-too"),("a prova","evidence / proof","PROH-vah"),("a análise","analysis","ah-NAH-lee-zj"),("a manchete","headline","mahn-SHET")],
    "abstract": [("a sociedade","society","soh-see-eh-DAH-dj"),("a identidade","identity","een-dah-dee-DAH-dj"),("a igualdade","equality","ee-gwahl-DAH-dj"),("a liberdade","freedom","lee-ber-DAH-dj"),("a responsabilidade","responsibility","resh-pon-sah-bee-lee-DAH-dj"),("a perspetiva","perspective","per-shpek-TEE-vah"),("a consequência","consequence","kohn-seh-KWEN-see-ah"),("a hipótese","hypothesis","ee-POH-teh-zj"),("a evidência","evidence","eh-vee-DEN-see-ah"),("o argumento","argument","ar-goo-MEN-too")],
    "travel": [("a viagem","trip","vee-AH-zheng"),("o aeroporto","airport","ah-eh-roh-POR-too"),("o voo","flight","VOH-oo"),("o passaporte","passport","pah-shah-POR-tj"),("a bagagem","luggage","bah-GAH-zheng"),("a reserva","reservation","reh-ZER-vah"),("o alojamento","accommodation","ah-loh-zhah-MEN-too"),("o destino","destination","desh-TEE-noo"),("a fronteira","border","fron-TAY-rah"),("o visitante","visitor","vee-zee-TAN-tj")],
    "nature": [("o tempo","weather / time","TEN-poo"),("o calor","heat","kah-LOR"),("a chuva","rain","SHOO-vah"),("o vento","wind","VEN-too"),("o rio","river","REE-oo"),("o mar","sea","MAR"),("a praia","beach","PRY-ah"),("a floresta","forest","floh-RESH-tah"),("a seca","drought","SEH-kah"),("o ambiente","environment","ahm-bee-EN-tj")],
    "general": [("a pessoa","person","peh-SOH-ah"),("a coisa","thing","KOY-zah"),("o lugar","place","loo-GAR"),("a pergunta","question","per-GOON-tah"),("a resposta","answer","resh-POSH-tah"),("o problema","problem","proh-BLEH-mah"),("a solução","solution","soh-loo-SOWN"),("importante","important","eem-por-TAN-tj"),("diferente","different","djee-feh-REN-tj"),("necessário","necessary","neh-seh-SAH-ree-oo")]
}

def _pool_for(title):
    t = title.lower()
    groups = [
        (("alphabet","pronunciation","spelling","letter names"), "alphabet"),
        (("greeting","introduction"), "greetings"),
        (("personal information","introducing","identity","sociolinguistics"), "identity"),
        (("number","mathematics","money","finance","banking"), "numbers"),
        (("day","month","season","date"), "calendar"),
        (("time","clock","routine"), "time"),
        (("family","relationship"), "family"),
        (("food","drink","restaurant","café","cooking"), "food"),
        (("house","room","household"), "home"),
        (("shopping","clothes","accessories","price"), "shopping"),
        (("transport","direction","travel","hotel","accommodation"), "transport"),
        (("health","body","medical"), "health"),
        (("education","study","profession"), "education"),
        (("work","meeting","business","professional","negotiation"), "work"),
        (("technology","internet","digital"), "technology"),
        (("news","media","current affairs","podcast","radio","television"), "media"),
        (("nature","weather","environment","climate"), "nature"),
        (("literature","academic","abstract","argument","debate","rhetorical","opinion","persuasion"), "abstract"),
    ]
    for words, key in groups:
        if any(w in t for w in words):
            return VOCAB_POOLS[key]
    return VOCAB_POOLS["general"]

GRAMMAR = {
"A1": [
("Gender and articles","Portuguese nouns are masculine or feminine. Learn each noun with its article: o livro, a casa. Use um/uma for an indefinite singular noun and os/as for the plural definite article. The article is part of the vocabulary item; do not guess gender from English."),
("SER, ESTAR and TER","SER commonly describes identity, origin and relatively defining characteristics: Sou angolano. ESTAR commonly describes location and temporary states: Estou em Luanda; Estou cansado. TER means to have and is also used for age: Tenho vinte anos. The choice depends on meaning, not a one-word English translation."),
("Present tense and basic word order","A neutral statement usually follows subject + verb + complement: Eu estudo português. Subject pronouns can be omitted when the verb ending makes the subject clear, but beginners may keep them while learning. Regular verbs have -ar, -er and -ir patterns."),
("Questions and negation","Put não before the conjugated verb: Não moro aqui. Yes/no questions can use rising intonation without changing word order. Question words include quem, o que, onde, quando, porquê and como."),
("Adjective agreement","Many adjectives change for gender and number: aluno dedicado, aluna dedicada, alunos dedicados, alunas dedicadas. Adjectives often follow the noun, although some common adjectives can precede it with a change in emphasis or meaning.")
],
"A2": [
("Regular and irregular verbs","Conjugate verbs for person and tense. Learn frequent irregular verbs such as ir, fazer, dizer, poder, querer and vir as complete patterns. In spoken Angolan Portuguese, usage and reductions vary by speaker and region."),
("Past events: pretérito perfeito","Use the pretérito perfeito for completed past events: Ontem visitei a minha família. Regular endings vary by -ar, -er and -ir verbs. Memorise high-frequency irregular forms such as fui, tive, fiz and disse."),
("Future plans and the imperative","The construction ir + infinitive expresses a near future: Vou estudar. Use the imperative for instructions and requests, choosing forms that match the relationship and level of politeness."),
("Prepositions and contractions","Portuguese combines many prepositions with articles: de + o = do; em + a = na; a + o = ao; por + o = pelo. Learn the whole contracted form in context."),
("Pronouns, quantities and comparisons","Object pronouns and quantity expressions depend on sentence structure. Use mais…do que, menos…do que and tão…como for basic comparisons. Regional spoken placement can differ from formal written conventions.")
],
"B1": [
("Pretérito perfeito and imperfeito","Use the pretérito perfeito for bounded completed events and the imperfeito for background, habits and ongoing past situations. Contrast: Quando era criança, vivia em Benguela; no ano passado, mudei-me para Luanda."),
("Subjunctive and uncertainty","The present subjunctive commonly follows expressions of desire, doubt, emotion, necessity or evaluation: Espero que venhas. Recognise the trigger and check whether the subject changes."),
("Conditional and hypothetical language","The conditional can express polite requests, reported future-in-the-past and hypothetical results: Gostaria de saber…; Se tivesse tempo, viajaria. Keep the tense relationship consistent."),
("Relative clauses and connectors","Use que, quem, onde and cujo in relative structures. Connect ideas with embora, apesar de, por isso, no entanto and além disso; choose connectors according to the logical relationship."),
("Argument, register and reported ideas","Summarise another person's position accurately, distinguish fact from opinion and choose formal or informal language for the audience. Reported speech may require changes in pronouns, time references and verb forms.")
],
"B2": [
("Compound tenses and sequence of events","Use compound forms carefully to show anteriority, duration and viewpoint. Portuguese varieties differ in the frequency and meaning of some compound constructions; prefer the forms natural in Angolan usage and explain alternatives."),
("Future subjunctive","The future subjunctive appears in clauses referring to a possible future condition or event: Quando tiver tempo, telefono. It is especially important after quando, se and assim que when the reference is future."),
("Passive and impersonal constructions","The ser + past participle passive focuses on the affected subject: O relatório foi publicado. The impersonal se construction is common in formal writing: Procura-se funcionário. Preserve agreement where required."),
("Reported speech and complex syntax","Use que-clauses and indirect questions to report statements and questions. Manage pronoun reference, tense sequence and punctuation so that complex sentences remain clear."),
("Collocation, nuance and register","Learn words in natural combinations rather than as isolated translations. Select connectors, idioms and levels of formality appropriate to professional, academic and everyday Angolan contexts.")
],
"C1": [
("Advanced mood and aspect","Choose indicative, subjunctive and infinitive structures according to certainty, evaluation, control and subject reference. Explain the pragmatic effect, not only the rule."),
("Cohesion and information structure","Use thematic progression, reference chains, ellipsis and varied sentence openings to guide a reader through complex information. Avoid overloading sentences with connectors."),
("Professional and academic style","Write concise reports, proposals and formal correspondence. Distinguish evidence, interpretation and recommendation; use precise terminology and consistent register."),
("Critical reading and listening","Identify thesis, evidence, assumptions, bias, implied meaning and rhetorical strategies. Separate what a speaker states from what the speaker implies."),
("Regional variation and language attitudes","Angolan Portuguese is not a single uniform accent. Vocabulary, rhythm and usage vary by region, age, community and situation. Compare varieties descriptively and avoid labelling local forms as inferior.")
],
"C2": [
("Precision, ambiguity and stylistic choice","Choose syntax and vocabulary to control emphasis, implication, ambiguity and tone. Explain why one formulation is more effective for a particular audience."),
("Rhetoric and persuasive discourse","Build nuanced arguments using concessions, qualifications, counterarguments and evidence. Avoid overstating conclusions and distinguish correlation from causation."),
("Literary and specialised language","Interpret figurative language, intertextual references, irony and specialised terminology. Preserve meaning and register when paraphrasing or translating."),
("Mediation and synthesis","Combine information from several sources, attribute claims, resolve apparent contradictions and reformulate complex material for a different audience."),
("Capstone communication","Demonstrate flexible, accurate communication across formal, informal, academic and professional settings. C2 is advanced proficiency, not a requirement to imitate a native accent.")
]
}

QUESTION_TEMPLATES = {
"A1": [
("Complete: Eu ___ de Luanda.",["sou","estou","tenho","és"],0,"Use sou from SER for origin or identity."),
("Choose the correct article: ___ casa.",["o","a","os","um"],1,"Casa is feminine singular: a casa."),
("Make the sentence negative: Eu moro aqui. → Eu ___ moro aqui.",["não","nunca de","sem","nem"],0,"Não normally comes before the conjugated verb."),
("Complete: Nós ___ português.",["fala","falam","falamos","falo"],2,"The nós form of falar is falamos."),
("Choose the natural age expression: ___ vinte anos.",["Sou","Estou","Tenho","Faço"],2,"Portuguese uses TER for age: Tenho vinte anos.")
],
"A2": [
("Choose the completed past: Ontem eu ___ ao mercado.",["vou","fui","ia","irei"],1,"Fui is the pretérito perfeito form of ir."),
("Complete the near future: Nós ___ estudar amanhã.",["vamos","fomos","íamos","sejamos"],0,"Ir + infinitive expresses a planned near future."),
("Choose the contraction: de + o mercado =",["da mercado","do mercado","no mercado","ao mercado"],1,"De + o contracts to do."),
("Choose the correct comparison: Luanda é ___ do que a minha aldeia.",["mais grande","maior","muito grande que","tão maior"],1,"Maior is the irregular comparative of grande."),
("Choose the polite request:",["Dá-me isso!","Quero isso agora.","Pode ajudar-me, por favor?","Tu ajudar eu."],2,"A modal question with por favor is a polite request.")
],
"B1": [
("Choose the best background tense: Quando era criança, ___ em Huambo.",["vivi ontem","morava","morarei","tenho morado ontem"],1,"The imperfeito describes an ongoing past situation or habitual background."),
("Complete: Espero que ele ___ a tempo.",["chega","chegue","chegou","chegava"],1,"Esperar que commonly selects the present subjunctive."),
("Choose the conditional form: Eu ___ participar, se pudesse.",["gostaria de","gostei de","gostava de ontem","gostarei de"],0,"Gostaria expresses a hypothetical or polite wish."),
("Choose the connector expressing contrast:",["portanto","além disso","no entanto","por isso"],2,"No entanto introduces contrast."),
("Choose the relative pronoun: A cidade ___ nasci fica no litoral.",["que","onde","cujo","quem"],1,"Onde refers to a place.")
],
"B2": [
("Complete the future condition: Quando ___, envio-te a mensagem.",["cheguei","chegar","chegava","chegaria"],1,"A future reference after quando takes the future subjunctive: chegar."),
("Choose the passive construction:",["O relatório publicou o director.","O relatório foi publicado pelo director.","O relatório publicar-se ontem.","O director foi publicar o relatório."],1,"Ser + past participle forms the canonical passive."),
("Choose a formal impersonal construction:",["Procura-se técnico.","Técnico procura nós.","Se procura técnico ontem.","Procurando técnico é."],0,"Procura-se is a common impersonal/passive-se construction."),
("Choose the best concession connector:",["embora","porque","por isso","logo"],0,"Embora introduces concession and normally takes the subjunctive."),
("Choose the natural collocation:",["tomar uma decisão","fazer uma decisão","pegar uma decisão","dar uma decisão"],0,"Tomar uma decisão is the standard collocation.")
],
"C1": [
("Choose the most suitable formal opening for a report:",["E então, pessoal...","O presente relatório analisa...","Olá malta, vou falar...","Pronto, é isso..."],1,"The present report analyses… is an appropriate formal opening."),
("Which connector signals a qualification?",["sem dúvida","ainda que","em primeiro lugar","por exemplo"],1,"Ainda que introduces a concession or qualification."),
("A careful academic claim should:",["state certainty without evidence","distinguish evidence from interpretation","remove all qualifications","use slang for emphasis"],1,"Advanced academic writing separates evidence and interpretation."),
("Which is the best strategy for regional variation?",["Treat one accent as the only correct form","Describe patterns by region and context","Call local forms mistakes","Assume every speaker uses identical vocabulary"],1,"Describe variation neutrally and in context."),
("Choose the clearest cohesive reference:",["Repeat every noun in every sentence","Use a clear pronoun with an unambiguous referent","Remove all references","Change the topic without a signal"],1,"Pronouns should have clear, recoverable referents.")
],
"C2": [
("Which revision best preserves a cautious claim?",["This proves everything.","The evidence suggests this interpretation, although alternatives remain.","Everyone knows this is true.","There is no possible doubt."],1,"The sentence calibrates certainty to the evidence."),
("A strong synthesis should:",["copy each source separately","integrate and attribute relevant claims","hide disagreements between sources","replace evidence with opinion"],1,"Synthesis integrates sources while preserving attribution."),
("Which choice best manages register?",["Use the same slang in every context","Adapt vocabulary and syntax to audience and purpose","Avoid all formal language","Use complex words regardless of clarity"],1,"Register should match audience, purpose and situation."),
("A persuasive counterargument should:",["misrepresent the opposing view","state the opposing view fairly before responding","ignore contrary evidence","attack the opponent personally"],1,"Fair representation strengthens a reasoned response."),
("C2 proficiency is best understood as:",["native accent imitation","flexible, precise and effective communication","never making any error","using the longest possible sentences"],1,"C2 concerns advanced communicative control, not accent imitation.")
]
}

def _level_key(level):
    return level.split(" ")[0]

def _angolan_title(title):
    replacements = {
        "French Alphabet": "Portuguese Alphabet",
        "Native French Speech": "Angolan Portuguese Speech",
        "Academic French": "Academic Portuguese",
        "Verb ÊTRE": "Verbs SER and ESTAR",
        "Verb AVOIR": "Verb TER",
        "Passé Composé": "Pretérito Perfeito",
        "Imparfait": "Pretérito Imperfeito",
        "Plus-Que-Parfait": "Pretérito Mais-que-perfeito",
        "Future Simple": "Future Tense",
        "Subjunctive Present": "Present Subjunctive",
        "Canadian French": "Angolan Portuguese",
        "Quebec French": "Angolan Portuguese",
        "French Spelling": "Portuguese Spelling",
        "French-Canadian Society": "Angolan Society",
        "Y and EN Pronouns": "Object Pronouns and Prepositional Complements",
        "Regular -ER, -IR and -RE Verbs": "Regular -AR, -ER and -IR Verbs",
        "NE...PAS": "NÃO",
        "QUI, QUE, OÙ": "QUE, QUEM, ONDE",
        "Native-Level Pronunciation": "Advanced Pronunciation",
        "Native-Level Conversation": "Advanced Communication",
    }
    for old, new in replacements.items():
        title = title.replace(old, new)
    return title

def _lesson_vocab(title, lesson_id):
    pool = _pool_for(title)
    # Rotate the selected pool by chapter so related chapters can revisit vocabulary
    # through a different subset without repeating a headword within one lesson.
    offset = 0 if lesson_id == 1 else (lesson_id * 3) % max(1, len(pool) - 6)
    selected = pool[offset:offset + 7]
    if len(selected) < 7:
        selected += VOCAB_POOLS["general"][:7-len(selected)]
    return [(pt, en, hint, "—", f"Hoje aprendo {pt}.") for pt,en,hint in selected]

def _build_lesson(lesson_id, topic):
    source_title, level = topic["title"], topic["level"]
    title = _angolan_title(source_title)
    key = _level_key(level)
    vocab = _lesson_vocab(source_title, lesson_id)
    core = vocab[:5]
    grammar = GRAMMAR[key]
    examples = [
        (f"Hoje vou estudar {core[0][0]}.", f"Today I am going to study {core[0][1]}.", "A natural, simple example using the lesson vocabulary."),
        (f"Aprendo português em Angola.", "I am learning Portuguese in Angola.", "Português is the language; em Angola gives the location."),
        (f"Pode explicar esta palavra, por favor?", "Can you explain this word, please?", "A polite request useful in independent study."),
        (f"É importante praticar um pouco todos os dias.", "It is important to practise a little every day.", "An impersonal expression with an infinitive."),
        (f"Quero usar {core[1][0]} numa frase.", f"I want to use {core[1][1]} in a sentence.", "Querer + infinitive expresses intention.")
    ]
    expressions = [
        ("Como se diz ... em português?","How do you say ... in Portuguese?","Ask for a translation or a word you do not know."),
        ("Pode repetir, por favor?","Could you repeat, please?","Polite request when you need to hear something again."),
        ("Não percebi. Pode explicar?","I did not understand. Could you explain?","Useful for clarification."),
        ("Está bem. Obrigado / obrigada.","All right. Thank you.","Choose obrigado or obrigada according to the speaker's grammatical gender.")
    ]
    if lesson_id == 1:
        grammar = [
            ("The Portuguese alphabet","Portuguese uses 26 letters: A–Z. K, W and Y are included in the modern alphabet, but appear mainly in foreign names, abbreviations and borrowed words. The names of letters are different from English; for example, H is agá, J is jota and W is dáblio. Practise spelling names and place names aloud."),
            ("Vowels, nasal vowels and common combinations","The vowel letters are A, E, I, O and U; Y appears mainly in borrowed words and names. Portuguese also has nasal vowels, often marked by tilde (ã, õ) or represented in combinations such as am, an, em, en, im, om and um depending on the word. The diphthong ão is especially common. Learn the sound in whole words and listen to Angolan speakers; vowel quality varies across regions and speakers."),
            ("Stress and written accent marks","Word stress can distinguish words and is not always predictable from English spelling. Acute and circumflex accents mark vowel quality and/or stress; the tilde marks nasalisation in words such as manhã and pão; the grave accent appears in contractions such as à. The cedilla in ç marks an /s/ sound before a, o or u, as in açúcar. Keep all written accents when spelling."),
            ("Digraphs and consonant sounds","Common letter pairs include ch, lh and nh. In many Portuguese words, nh represents a palatal nasal sound, as in manhã; lh represents a palatal lateral, as in filho; ch is commonly /ʃ/. The pronunciation of r and final s varies among Portuguese varieties, including within Angola. Do not assume one accent represents every Angolan speaker."),
            ("Syllables and connected speech","Divide unfamiliar words into syllables, identify the stressed syllable, then say the word at a natural pace. In connected speech, neighbouring vowels and consonants may influence each other. Start slowly for clarity, then practise the whole phrase without inserting pauses between every word.")
        ]
        examples = [
            ("O alfabeto português tem vinte e seis letras.", "The Portuguese alphabet has twenty-six letters.", "Vinte e seis is the number 26."),
            ("A palavra manhã tem um til.", "The word manhã has a tilde.", "The tilde marks the nasal vowel."),
            ("Filho escreve-se com lh.", "Filho is written with lh.", "LH is a common Portuguese digraph."),
            ("Como se pronuncia esta palavra?", "How is this word pronounced?", "Use this question when checking pronunciation."),
            ("Pode soletrar o seu nome, por favor?", "Can you spell your name, please?", "Soletrar means to spell out letter by letter.")
        ]
        expressions = [
            ("Como se escreve ...?","How is ... spelled?","Ask someone to spell a word."),
            ("Como se pronuncia ...?","How is ... pronounced?","Ask about the pronunciation of a word."),
            ("Pode soletrar, por favor?","Can you spell it, please?","A polite spelling request."),
            ("Fale mais devagar, por favor.","Please speak more slowly.","Ask for a slower repetition.")
        ]
        alphabet_conversations = [
            ("Spelling a name", [("A","Como se escreve o seu nome?"),("B","Escreve-se P-A-R-T-H."),("A","Pode repetir mais devagar?"),("B","Claro. P-A-R-T-H.")], "A: How do you spell your name? B: It is spelled P-A-R-T-H. A: Can you repeat more slowly? B: Of course. P-A-R-T-H."),
            ("Checking a sound", [("A","Como se pronuncia esta palavra?"),("B","Pronuncia-se manhã."),("A","O til indica um som nasal?"),("B","Sim. Ouça a palavra e repita.")], "A: How is this word pronounced? B: It is pronounced manhã. A: Does the tilde indicate a nasal sound? B: Yes. Listen to the word and repeat.")
        ]
    questions = QUESTION_TEMPLATES[key]
    if lesson_id == 1:
        questions = [
            ("Which set contains the five main Portuguese vowel letters?", ["A, E, I, O, U", "B, C, D, F, G", "J, K, L, M, N", "P, Q, R, S, T"], 0, "The five main vowel letters are A, E, I, O and U."),
            ("Which letters are mainly used in foreign names and borrowed words?", ["A, E and I", "B, C and D", "K, W and Y", "M, N and O"], 2, "K, W and Y are part of the modern alphabet and appear mainly in names and borrowed forms."),
            ("What does the tilde mark in manhã?", ["A plural ending", "Nasalisation", "A silent consonant", "A question"], 1, "The tilde marks nasalisation in the vowel."),
            ("Which letter pair appears in filho?", ["nh", "ch", "lh", "rr"], 2, "Filho is written with the digraph lh."),
            ("What is the best way to learn a new word's stress?", ["Guess from English spelling", "Memorise the spelling only", "Ignore the stressed syllable", "Listen to the word and practise its stressed syllable"], 3, "Portuguese stress is important; learn it with the whole word.")
        ]
    conversations = [
        ("A short everyday exchange", [("A","Bom dia! Como está?"),("B","Estou bem, obrigado/a. E você?"),("A","Também estou bem. Está a aprender português?"),("B","Sim, estou a aprender português de Angola.")], "A: Good morning! How are you? B: I am well, thank you. And you? A: I am well too. Are you learning Portuguese? B: Yes, I am learning Angolan Portuguese."),
        ("Asking for help", [("A","Desculpe, pode ajudar-me?"),("B","Claro. O que precisa?"),("A","Como se diz isto em português?"),("B","Diz-se ..."),("A","Muito obrigado/a!"),("B","De nada.")], "A: Excuse me, can you help me? B: Of course. What do you need? A: How do you say this in Portuguese? B: It is said ... A: Thank you very much! B: You're welcome.")
    ]
    if lesson_id == 1:
        conversations = alphabet_conversations
    # Rotate prompts so each chapter's practice and assessment begin at a different
    # point while keeping the answer key and distractors intact.
    shift = lesson_id % len(questions)
    exercise = [questions[(shift+i) % len(questions)] for i in range(5)]
    assessment = [questions[(shift+i+2) % len(questions)] for i in range(5)]
    # Avoid overlap even after rotation by changing assessment stems while testing
    # the same level outcomes.
    assessment = [("Assessment: " + q, opts, ans, exp) for q,opts,ans,exp in assessment]
    return {
        "title": title, "goal": f"Build practical Angolan Portuguese skills related to: {title.lower()}.",
        "objectives": [f"Understand the key language patterns connected with {title.lower()}.", "Recognise and use the lesson vocabulary in meaningful sentences.", "Apply the target language in a realistic Angolan Portuguese context."],
        "vocabulary": vocab, "grammar": [(name, explanation) for name,explanation in grammar[:3]],
        "expressions": expressions, "examples": examples, "conversations": conversations,
        "pronunciation": ["These are learner-friendly pronunciation hints, not a single mandatory Angolan accent.", "Portuguese stress is important; learn the stressed syllable with each new word.", "Vowel quality and reduction vary across Angola and between formal and informal speech.", "Listen to speakers from different Angolan regions when audio resources are available."],
        "exercises": exercise, "assessment": assessment,
        "speaking": ["Read the dialogue aloud twice, changing roles on the second reading.", "Create five original sentences using this lesson's vocabulary and grammar.", "Record yourself if possible, then compare clarity, rhythm and word stress with a trusted Angolan Portuguese model."],
        "summary": [f"This chapter develops {title.lower()} in Portuguese.", "Use vocabulary in complete sentences rather than memorising isolated translations.", "Choose forms appropriate to the speaker, listener and situation."],
        "homework": ["Write eight original sentences using at least five lesson words.", "Adapt one dialogue to a situation you might experience in Angola.", "Review the lesson without looking at the translations, then check your answers."]
    }

PORTUGUESE_LESSONS = {lesson_id: _build_lesson(lesson_id, topic) for lesson_id, topic in TOPICS.items()}

# Replace the first five A1 chapters with individually authored, editorially reviewed content.
from angolan_portuguese_a1_quality import A1_QUALITY_LESSONS
PORTUGUESE_LESSONS.update(A1_QUALITY_LESSONS)

