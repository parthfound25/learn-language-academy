import hmac
import random
import streamlit as st
from a1_lessons import A1_LESSONS

st.set_page_config(
    page_title="Learn Language Academy by Parth",
    page_icon="🇫🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------
# Authentication: usernames and passwords are managed in Streamlit Secrets.
# No email, registration, or create-account flow.
# ---------------------------------------------------------------------
try:
    configured_users = dict(st.secrets["users"])
except Exception:
    configured_users = {}

if not configured_users:
    st.title("🍀 Learn Language Academy by Parth")
    st.error("No learner accounts are configured.")
    st.markdown("Add learner accounts in Streamlit → App settings → Secrets:")
    st.code('[users]\n"Parth Sharma" = "YOUR_PASSWORD"\n"User 2" = "ANOTHER_PASSWORD"', language="toml")
    st.stop()

if not st.session_state.get("active_user"):
    st.title("🍀 Learn Language Academy by Parth")
    st.caption("Your personal language-learning journey starts here.")
    with st.form("username_login_form"):
        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")
        login_submit = st.form_submit_button("Sign in", type="primary", use_container_width=True)
    if login_submit:
        expected_password = configured_users.get(login_username.strip())
        if expected_password is not None and hmac.compare_digest(str(expected_password), login_password):
            username = login_username.strip()
            st.session_state.active_user = username
            st.session_state.xp = st.session_state.get(f"learner_{username}_xp", 0)
            st.session_state.completed = st.session_state.get(f"learner_{username}_completed", [])
            st.session_state.active_lesson = st.session_state.get(f"learner_{username}_active_lesson", 1)
            st.session_state.practice_rounds = st.session_state.get(f"learner_{username}_practice_rounds", 0)
            st.session_state.practice_correct = st.session_state.get(f"learner_{username}_practice_correct", 0)
            st.session_state.practice_total = st.session_state.get(f"learner_{username}_practice_total", 0)
            st.session_state.earned_achievements = st.session_state.get(f"learner_{username}_earned_achievements", [])
            st.session_state.selected_language = st.session_state.get(f"learner_{username}_selected_language", "")
            for transient_key in ("practice_questions", "practice_submitted", "practice_round_score", "practice_lesson_active"):
                st.session_state.pop(transient_key, None)
            st.session_state.page = "Home"
            st.rerun()
        else:
            st.error("Incorrect username or password.")
    st.stop()

# ---------------------------------------------------------------------
# Course roadmap: preserve the exact 90 lesson titles and numbering.
# Lesson content is added progressively, one complete lesson at a time.
# ---------------------------------------------------------------------
LEVELS = {
    "A1 – Absolute Beginner": [
        "French Alphabet, Sounds and Pronunciation",
        "Greetings and Basic Introductions",
        "Personal Information and Introducing Yourself",
        "Numbers, Counting and Basic Mathematics",
        "Days, Months, Seasons and Dates",
        "Time, Clock and Daily Expressions",
        "Nouns, Gender and Articles",
        "Subject Pronouns and the Verb ÊTRE",
        "The Verb AVOIR and Possession",
        "Common Adjectives and Describing People",
        "Family Members and Relationships",
        "Colours, Objects and Describing Things",
        "Food, Drinks and Basic Restaurant Vocabulary",
        "Present Tense and Everyday Activities",
        "A1 Comprehensive Revision and Assessment",
    ],
    "A2 – Elementary": [
        "Regular -ER, -IR and -RE Verbs",
        "Irregular Everyday Verbs",
        "Reflexive Verbs and Daily Routines",
        "Negation: NE...PAS and Other Forms",
        "Asking Questions and Question Words",
        "Prepositions of Place and Movement",
        "House, Rooms and Household Objects",
        "Shopping, Clothes and Accessories",
        "Money, Prices and Numbers in Real Life",
        "Restaurants, Cafés and Ordering Food",
        "Transportation and Asking for Directions",
        "Weather, Nature and Seasons",
        "Health, Body Parts and Medical Expressions",
        "Near Future and Recent Past",
        "A2 Comprehensive Revision and Assessment",
    ],
    "B1 – Intermediate": [
        "Passé Composé - Talking About the Past",
        "Imparfait - Describing Past Situations",
        "Passé Composé vs Imparfait",
        "Future Simple - Talking About the Future",
        "Conditional Present - Expressing Wishes",
        "Comparatives and Superlatives",
        "Direct and Indirect Object Pronouns",
        "Y and EN Pronouns",
        "Relative Pronouns: QUI, QUE, OÙ",
        "Hobbies, Interests and Leisure Activities",
        "Travel, Hotels and Accommodation",
        "Education, Studies and Professions",
        "Work, Meetings and Workplace Communication",
        "Feelings, Opinions and Social Interactions",
        "B1 Comprehensive Revision and Assessment",
    ],
    "B2 – Upper Intermediate": [
        "Plus-Que-Parfait - The Past Before the Past",
        "Advanced Future and Conditional Structures",
        "Subjunctive Present - Expressing Necessity and Emotion",
        "Si Clauses and Conditional Sentences",
        "Passive Voice and Impersonal Structures",
        "Reported Speech and Indirect Questions",
        "Advanced Pronouns and Pronoun Order",
        "Complex Sentence Construction",
        "Conjunctions and Linking Expressions",
        "Banking, Finance and Administrative Vocabulary",
        "Technology, Internet and Digital Communication",
        "News, Media and Current Affairs",
        "Debates, Arguments and Persuasion",
        "Canadian French Idioms and Informal Speech",
        "B2 Comprehensive Revision and Assessment",
    ],
    "C1 – Advanced": [
        "Advanced Subjunctive and Complex Grammar",
        "Advanced Past Tenses and Narrative Techniques",
        "Advanced Conditional and Hypothetical Expressions",
        "Nuanced Adverbs, Adjectives and Expressions",
        "Idiomatic Canadian French and Regional Expressions",
        "Colloquial Quebec French and Spoken Contractions",
        "Understanding Fast Native French Speech",
        "Professional Emails, Reports and Formal Writing",
        "Meetings, Negotiations and Presentations",
        "Expressing Complex Opinions and Abstract Ideas",
        "Literature, Books and Advanced Reading",
        "Cultural References and French-Canadian Society",
        "Humour, Sarcasm, Irony and Nuance",
        "Advanced Listening and Spontaneous Speaking",
        "C1 Comprehensive Revision and Assessment",
    ],
    "C2 – Mastery": [
        "Mastering Native-Level Pronunciation and Intonation",
        "Understanding Regional Canadian French Accents",
        "Advanced Idioms, Proverbs and Expressions",
        "Sophisticated Vocabulary and Synonyms",
        "Subtle Grammar, Register and Stylistic Choices",
        "Advanced Literary and Academic French",
        "Persuasive and Rhetorical Communication",
        "Complex Professional and Business Communication",
        "Understanding Cultural and Historical References",
        "Spontaneous Debates and Intellectual Discussions",
        "Mastering Humour, Wordplay and Double Meanings",
        "Understanding Native Podcasts, Radio and Television",
        "Advanced Creative and Professional Writing",
        "Native-Level Conversation and Communication Simulation",
        "C2 Final Comprehensive Assessment",
    ],
}

ALL_LESSONS = []
lesson_number = 1
for level_name, titles in LEVELS.items():
    for title in titles:
        ALL_LESSONS.append({
            "id": lesson_number,
            "title": title,
            "level": level_name,
            "xp": 25 if lesson_number == 1 else 30,
        })
        lesson_number += 1

# ---------------------------------------------------------------------
# Complete Lesson 1 content. Teaching language: simple English.
# Canadian French notes are labelled; broad standard pronunciation first.
# ---------------------------------------------------------------------
LESSON_1 = {
    "vocabulary": [
        ("bonjour", "hello; good morning", "bohn-zhoor", "/bɔ̃.ʒuʁ/", "Bonjour, tout le monde ! — Hello, everyone!"),
        ("salut", "hi; bye (informal)", "sah-lü", "/sa.ly/", "Salut, Marie ! — Hi, Marie!"),
        ("bonsoir", "good evening", "bohn-swahr", "/bɔ̃.swaʁ/", "Bonsoir, monsieur. — Good evening, sir."),
        ("au revoir", "goodbye", "oh ruh-vwahr", "/o ʁə.vwaʁ/", "Au revoir et à demain. — Goodbye and see you tomorrow."),
        ("merci", "thank you", "mehr-see", "/mɛʁ.si/", "Merci beaucoup. — Thank you very much."),
        ("français", "French; French language", "frahn-say", "/fʁɑ̃.sɛ/", "J'apprends le français. — I am learning French."),
        ("café", "coffee; café", "kah-fay", "/ka.fe/", "Un café, s'il vous plaît. — A coffee, please."),
        ("maison", "house; home", "may-zohn", "/mɛ.zɔ̃/", "La maison est grande. — The house is big."),
        ("chat", "cat", "shah", "/ʃa/", "Le chat dort. — The cat is sleeping."),
        ("rouge", "red", "roozh", "/ʁuʒ/", "Le livre est rouge. — The book is red."),
        ("trois", "three", "trwah", "/tʁwa/", "J'ai trois livres. — I have three books."),
        ("téléphone", "telephone; phone", "tay-lay-fohn", "/te.le.fɔn/", "Mon téléphone est ici. — My phone is here."),
        ("montagne", "mountain", "mohn-tahn-yuh", "/mɔ̃.taɲ/", "La montagne est belle. — The mountain is beautiful."),
        ("ami / amie", "friend (masculine / feminine)", "ah-mee", "/a.mi/", "C'est mon amie. — She is my friend."),
        ("enfant", "child", "ahn-fahn", "/ɑ̃.fɑ̃/", "L'enfant joue. — The child is playing."),
    ],
    "grammar": [
        ("The alphabet and letter names",
         "French uses the same 26 basic letters as English, but the letter names are different. For example, A is approximately “ah”, B is “bay”, C is “say”, and J is “zhee”. Letter names are useful when spelling your name or an unfamiliar word. The French R is made toward the back of the throat; the French U is a rounded front vowel and is not the same as English “oo”."),
        ("Vowels and vowel combinations",
         "The main vowel letters are A, E, I, O, U and Y. Their sounds depend on the word and surrounding letters. Common combinations include OU, usually /u/ as in vous; OI, usually /wa/ as in moi; CH, usually /ʃ/ as in chat; PH, usually /f/ as in photo; and GN, often /ɲ/ as in montagne. Learn these as useful patterns, not unbreakable rules."),
        ("French nasal vowels",
         "In combinations such as AN, EN, ON, IN and AIN, the vowel can become nasal. Air flows through the nose as well as the mouth. In many words the N or M is not pronounced as a separate final consonant. Examples: enfant, bon and pain. Regional pronunciation varies, including across Canada."),
        ("Written accents",
         "É (accent aigu) usually marks a closed /e/ sound, as in café. È and Ê often mark a more open /ɛ/ sound, as in père and fête. Ë (tréma) indicates that a vowel is pronounced separately from the preceding vowel, as in Noël. Ç (cédille) makes C sound like S before A, O or U, as in français. Accents are part of correct spelling."),
        ("Silent final consonants",
         "Many French words have a final consonant that is not pronounced: petit (final T), grand (final D), vous (final S), and nez (final Z). This is a common pattern, not a universal rule. Some final consonants are pronounced, and liaison can make a normally silent consonant audible before a following vowel sound."),
        ("The French U and OU distinction",
         "For U /y/, round your lips as if saying “oo”, but position your tongue as if saying “ee”. For OU /u/, use the familiar English “oo” tongue position. Compare tu /ty/ (you) with tout /tu/ (everything), and rue /ʁy/ (street) with roue /ʁu/ (wheel). This distinction can change a word's meaning."),
    ],
    "expressions": [
        ("Bonjour !", "Hello! / Good morning!", "Polite, standard greeting; suitable in shops and most everyday situations."),
        ("Salut !", "Hi! / Bye!", "Informal; use with friends, family and people you know well."),
        ("Bonsoir !", "Good evening!", "Used as an evening greeting."),
        ("Au revoir !", "Goodbye!", "A standard, polite way to leave."),
        ("Merci beaucoup.", "Thank you very much.", "A warm and common expression of thanks."),
        ("S'il vous plaît.", "Please.", "Polite form, used with strangers or in formal situations."),
        ("S'il te plaît.", "Please.", "Informal form, used with someone you know well."),
        ("Excusez-moi.", "Excuse me.", "Polite way to get someone's attention or apologise for a small interruption."),
    ],
    "examples": [
        ("Bonjour, je m'appelle Alex.", "Hello, my name is Alex.", "Bonjour is a greeting; je m'appelle is the usual way to give your name."),
        ("J'apprends le français.", "I am learning French.", "J'apprends comes from apprendre, to learn."),
        ("Merci beaucoup !", "Thank you very much!", "Beaucoup means a lot or very much."),
        ("Le chat est noir.", "The cat is black.", "Le is a masculine singular article; noir means black."),
        ("J'ai trois livres.", "I have three books.", "Trois is pronounced /tʁwa/; the final S is silent."),
        ("Un café, s'il vous plaît.", "A coffee, please.", "A natural, polite way to order a coffee."),
    ],
    "conversations": [
        ("At a café",
         [("Client", "Bonjour !"), ("Serveur", "Bonjour !"), ("Client", "Un café, s'il vous plaît."), ("Serveur", "Bien sûr."), ("Client", "Merci beaucoup."), ("Serveur", "Avec plaisir.")],
         "Customer: Hello! / Server: Hello! / Customer: A coffee, please. / Server: Of course. / Customer: Thank you very much. / Server: My pleasure."),
        ("Meeting someone",
         [("A", "Salut !"), ("B", "Bonjour !"), ("A", "Comment ça va ?"), ("B", "Ça va bien, merci. Et toi ?"), ("A", "Très bien, merci !")],
         "A: Hi! / B: Hello! / A: How are you? / B: I'm well, thanks. And you? / A: Very well, thanks!"),
    ],
    "exercises": [
        ("Choose the correct meaning of “bonjour”.", ["Goodbye", "Hello / good morning", "Thank you", "Please"], 1, "Bonjour is a standard greeting, especially during the day."),
        ("Which spelling usually represents the “sh” sound?", ["OU", "CH", "OI", "PH"], 1, "CH usually represents /ʃ/, as in chat."),
        ("Which word contains the French U /y/ sound?", ["tout", "tu", "vous", "rouge"], 1, "Tu contains /y/. Tout, vous and rouge contain /u/."),
        ("What does the cedilla do in “français”?", ["Makes C sound like S", "Makes C silent", "Makes C sound like K", "Makes the vowel nasal"], 0, "Ç makes C sound like S before A, O or U."),
        ("What does “merci beaucoup” mean?", ["Good evening", "See you tomorrow", "Thank you very much", "Excuse me"], 2, "Merci means thank you; beaucoup means very much."),
        ("Which word means “mountain”?", ["maison", "montagne", "montre", "matin"], 1, "Montagne means mountain."),
    ],
    "speaking": [
        "Say the French alphabet slowly. Pay extra attention to E, G, J, U, R and W.",
        "Practise the contrast aloud: tu /ty/ versus tout /tu/; rue /ʁy/ versus roue /ʁu/.",
        "Read these words aloud three times: bonjour, merci, français, café, maison, chat, rouge, trois.",
        "Read this short passage aloud: Bonjour ! Je m'appelle Alex. J'apprends le français. Merci beaucoup et au revoir !",
        "Canadian French note: Quebec and other Canadian French accents vary. Start with clear, broadly understood pronunciation. In many Quebec accents, T and D can be affricated before /i/, /y/ and /ɥ/, as in tu and petit. You will study regional speech in later lessons.",
    ],
    "summary": [
        "French has 26 basic letters, with French letter names.",
        "The six vowel letters are A, E, I, O, U and Y.",
        "OU usually sounds /u/; OI usually sounds /wa/; CH usually sounds /ʃ/; PH usually sounds /f/.",
        "French has nasal vowels, written accents, and many silent final consonants.",
        "French U /y/ and OU /u/ are different sounds and can distinguish words.",
        "Canadian French has regional pronunciation features; variation is normal.",
    ],
    "assessment": [
        ("How many basic letters are in the French alphabet?", ["24", "26", "28", "30"], 1, "French uses the same 26 basic letters as English."),
        ("Which French letter name sounds like the middle sound in “measure”?", ["J", "A", "M", "T"], 0, "French J is /ʒ/, like the middle sound in measure."),
        ("Which word contains the French U /y/ sound?", ["tout", "tu", "bon", "moi"], 1, "Tu contains /y/; tout contains /u/."),
        ("What does the cedilla in français do?", ["Makes C sound like S", "Makes C silent", "Makes C sound like K", "Makes C nasal"], 0, "Ç makes C sound like S before A, O or U."),
        ("Which spelling usually sounds like “sh”?", ["OU", "CH", "OI", "PH"], 1, "CH usually represents /ʃ/."),
        ("What does “bon” mean?", ["Bad", "Good", "House", "Bread"], 1, "Bon means good."),
        ("Which word normally has a silent final T?", ["petit", "parler", "chat", "montagne"], 0, "The final T in petit is normally silent."),
        ("What sound does OI commonly represent?", ["/i/", "/u/", "/wa/", "/ɑ̃/"], 2, "OI commonly represents /wa/, as in moi."),
        ("Which accent appears in café?", ["Tréma", "Accent aigu", "Cédille", "Accent grave"], 1, "É has an accent aigu."),
        ("Which French word means mountain?", ["maison", "montagne", "merci", "rouge"], 1, "Montagne means mountain."),
    ],
}


# Expanded textbook chapter: extra depth, guided drills, and more practice.
# These additions deliberately make Lesson 1 a substantial study unit.
LESSON_1["vocabulary"] += [
    ("lettre", "letter (of the alphabet)", "letr", "/lɛtʁ/", "Quelle est cette lettre ? — What letter is this?"),
    ("voyelle", "vowel", "vwah-yel", "/vwa.jɛl/", "A est une voyelle. — A is a vowel."),
    ("consonne", "consonant", "kohn-sohn", "/kɔ̃.sɔn/", "B est une consonne. — B is a consonant."),
    ("prononciation", "pronunciation", "proh-nohn-see-ah-see-ohn", "/pʁɔ.nɔ̃.sja.sjɔ̃/", "La prononciation est importante. — Pronunciation is important."),
    ("son", "sound", "sohn", "/sɔ̃/", "Écoutez le son. — Listen to the sound."),
    ("bouche", "mouth", "boosh", "/buʃ/", "Ouvrez la bouche. — Open your mouth."),
    ("langue", "tongue; language", "lahng", "/lɑ̃ɡ/", "La langue française. — The French language."),
    ("nez", "nose", "nay", "/ne/", "Le son passe par le nez. — The sound passes through the nose."),
    ("pain", "bread", "pan (nasal)", "/pɛ̃/", "Je mange du pain. — I am eating bread."),
    ("bon", "good", "bohn (nasal)", "/bɔ̃/", "C'est bon. — It's good."),
    ("beau / belle", "beautiful; handsome", "boh / bel", "/bo / bɛl/", "C'est une belle maison. — It's a beautiful house."),
    ("livre", "book", "leevr", "/livʁ/", "Voici un livre. — Here is a book."),
    ("petit / petite", "small (masculine / feminine)", "puh-tee / puh-teet", "/pə.ti / pə.tit/", "Un petit chat. — A small cat."),
    ("grand / grande", "big; tall (masculine / feminine)", "grahn / grahnd", "/ɡʁɑ̃ / ɡʁɑ̃d/", "Une grande maison. — A big house."),
    ("noir / noire", "black (masculine / feminine)", "nwahr", "/nwaʁ/", "Un chat noir. — A black cat."),
    ("vert / verte", "green (masculine / feminine)", "vair / vert", "/vɛʁ / vɛʁt/", "Un livre vert. — A green book."),
    ("bleu / bleue", "blue (masculine / feminine)", "bluh", "/blø/", "Le ciel est bleu. — The sky is blue."),
    ("livre audio", "audiobook", "leevr oh-dee-oh", "/livʁ o.djo/", "J'écoute un livre audio. — I listen to an audiobook."),
    ("épeler", "to spell out", "ay-puh-lay", "/e.pə.le/", "Pouvez-vous épeler votre nom ? — Can you spell your name?"),
    ("répéter", "to repeat", "ray-pay-tay", "/ʁe.pe.te/", "Répétez, s'il vous plaît. — Repeat, please."),
    ("lentement", "slowly", "lahnt-mohn", "/lɑ̃t.mɑ̃/", "Parlez lentement. — Speak slowly."),
    ("rapidement", "quickly", "rah-peed-mohn", "/ʁa.pid.mɑ̃/", "Il parle rapidement. — He speaks quickly."),
    ("écouter", "to listen", "ay-koo-tay", "/e.ku.te/", "Écoutez attentivement. — Listen carefully."),
    ("parler", "to speak", "par-lay", "/paʁ.le/", "Je parle un peu français. — I speak a little French."),
    ("comprendre", "to understand", "kohn-prahn-dr", "/kɔ̃.pʁɑ̃dʁ/", "Je comprends. — I understand."),
]
LESSON_1["grammar"] += [
    ("How to read IPA pronunciation",
     "IPA is the International Phonetic Alphabet: one symbol represents one speech sound. Slashes show a broad pronunciation, not ordinary spelling. For example, chat is /ʃa/: /ʃ/ is the 'sh' sound and /a/ is an open 'ah' vowel. The French R is commonly /ʁ/, made with the back of the tongue or uvula area. You do not need to memorise every IPA symbol today. Use it as a reliable reference when English spelling clues are misleading."),
    ("The six vowel letters are not just six vowel sounds",
     "A, E, I, O, U and Y are the six vowel letters, but French has more vowel sounds than letters. A vowel can change because of an accent, a neighbouring letter, or a spelling combination. For example, é in été is different from è in père. The letter E is especially variable: compare le, été, mère and petit. Learn the sound of a whole word rather than assuming one letter always has one sound."),
    ("Open and closed E: é, è, ê and unaccented e",
     "The sound /e/ is a close-mid vowel, often heard in café and été. The sound /ɛ/ is more open, as in père, mère and fête. The accent aigu appears on é; the accent grave appears on è; the circumflex appears on ê. Unaccented e has several possible pronunciations and can sometimes be very weak or silent, depending on the word and speaking style. This is why accents matter when reading aloud."),
    ("The French R: where it is made",
     "French R is usually a voiced uvular or velar fricative/approximant, often written /ʁ/ in broad transcription. It is not the English R made with the tongue curled or bunched in the middle of the mouth. Try a gentle gargling-like airflow at the back of the mouth, without forcing or scraping your throat. Practise in short words such as rue, rouge, Paris and merci. A light, comfortable R is better than an exaggerated one."),
    ("Nasal vowels: what your mouth and nose do",
     "For a nasal vowel, the soft palate lowers so some air resonates through the nose while the vowel is being produced. Do not add a strong separate 'n' at the end. Compare oral vowel plus consonant with a nasal vowel: beau /bo/ versus bon /bɔ̃/; lit /li/ versus lin /lɛ̃/ (regional details vary). Put a finger lightly beside your nose to notice vibration, but do not pinch your nose shut while speaking."),
    ("The common nasal spelling families",
     "AN and EN often represent /ɑ̃/ as in dans and enfant. ON often represents /ɔ̃/ as in bon and maison. IN, AIN and EIN often represent /ɛ̃/ as in cinq, pain and plein. UN may represent /œ̃/ in varieties that preserve the distinction, while many speakers merge it with /ɛ̃/. The exact vowel quality varies by region, including in Canada. These spellings are useful patterns, not perfect one-to-one rules."),
    ("When N or M is pronounced separately",
     "N and M do not automatically make the preceding vowel nasal. Before another vowel, they are often pronounced as consonants or help form a syllable boundary: année, amie, immense. Double consonants can also affect how a word is divided or read. Compare enfant, where EN is nasal, with ennemi, where the N is pronounced. Always consider the letters that follow the vowel."),
    ("C and G: hard and soft sounds",
     "C before E, I or Y is usually soft /s/: ceci, cinéma. C before A, O or U is usually hard /k/: café, code, cube. Ç forces the soft /s/ sound before A, O or U: français, garçon. G before E, I or Y is usually /ʒ/: gel, girafe. G before A, O or U is usually /ɡ/: gare, gomme, guitare. GU before E or I often keeps the hard /ɡ/ sound, as in guitare."),
    ("S, SS and Z",
     "A single S between two vowels is often pronounced /z/, as in maison and rose. SS between vowels is pronounced /s/, as in poisson. At the beginning of a word, S is usually /s/: salut, soir. Z is generally /z/: zéro. These patterns help explain why maison has a /z/ sound even though it is written with one S."),
    ("The letters H and the two kinds of H words",
     "The letter H is not pronounced in ordinary French words. Traditionally, dictionaries distinguish h muet and h aspiré. Neither is pronounced, but h aspiré blocks liaison and elision: les héros keeps the vowel boundary, and le héros does not become l'héros. With h muet, liaison or elision can occur: les hommes, l'homme. You can learn which category a word belongs to from a dictionary or vocabulary entry."),
    ("Liaison: linking a final consonant to the next word",
     "In some fixed grammatical contexts, a normally silent final consonant is pronounced at the start of the next word when that word begins with a vowel sound. This is called liaison. For example, vous avez is commonly pronounced /vu.za.ve/, and les amis /le.za.mi/. Liaison is required in some contexts, optional in others, and incorrect in others. Do not add it everywhere; learn common combinations as phrases."),
    ("Enchaînement: connecting sounds that are already pronounced",
     "Enchaînement is different from liaison. If a final consonant is already pronounced, it can flow smoothly into the next vowel sound. For example, avec elle is spoken continuously, with the final /k/ of avec connecting to elle. There is no new consonant being activated; the existing consonant simply links to the following syllable. Smooth French speech depends on these connections."),
    ("Syllables and French rhythm",
     "French rhythm is organised around groups of words and syllables rather than the strong stress pattern typical of English. A final syllable in a rhythmic group often receives a slight prominence, but French does not normally use the same strong word-by-word stress that English does. Practise saying bon-jour, mai-son, té-lé-phone and mon-ta-gne with an even, connected rhythm. Avoid stressing the first syllable of every word."),
    ("Final consonants: a practical rule with exceptions",
     "A common memory aid is that final C, R, F and L are more likely to be pronounced, while many other final consonants are often silent. This is only a rough guide: blanc has a pronounced C in some contexts, but many words break simple rules. Final R is heard in parler; final F in neuf; final L in avril. Final consonants may also change through inflection or liaison. Learn pronunciation with each word."),
    ("French U versus OU: a physical mouth exercise",
     "For /y/ in tu, begin by making an 'ee' tongue position and then round your lips without moving your tongue back. For /u/ in tout, the tongue is farther back and the lips are rounded. Alternate slowly: /i/–/y/–/u/. Then say si–su–sou, tu–tout, rue–roue. If the sounds collapse into one, slow down and exaggerate the lip rounding first, then make the movement smaller."),
    ("Quebec and Canadian French: variation, not one single accent",
     "Canadian French includes Quebec, Acadian, Franco-Ontarian, Franco-Manitoban and other varieties. Pronunciation differs by region, generation, formality and speaker. In many Quebec varieties, /t/ and /d/ may be affricated before /i/, /y/ and /ɥ/, giving tu and dîner a noticeable release. Some vowels also differ from European reference French. This course begins with widely understood standard forms, then labels regional forms clearly."),
]
LESSON_1["expressions"] += [
    ("Comment prononce-t-on ce mot ?", "How do you pronounce this word?", "Useful when asking someone to model a word."),
    ("Pouvez-vous répéter ?", "Can you repeat?", "Polite request; vous is the formal or plural you."),
    ("Plus lentement, s'il vous plaît.", "More slowly, please.", "A natural classroom request."),
    ("Je ne comprends pas.", "I don't understand.", "Useful when you need clarification."),
    ("Je comprends.", "I understand.", "A simple way to confirm understanding."),
    ("Comment ça s'écrit ?", "How is it written/spelled?", "Ask about spelling."),
    ("Ça s'écrit comment ?", "How do you spell that?", "Common conversational alternative."),
    ("Comment dit-on ... en français ?", "How do you say ... in French?", "Insert the word or phrase you want to translate."),
    ("Qu'est-ce que ça veut dire ?", "What does that mean?", "Ask for the meaning of a word or expression."),
    ("Je parle un peu français.", "I speak a little French.", "A useful beginner phrase; français is the language name."),
    ("Je suis en train d'apprendre.", "I'm learning / in the process of learning.", "A natural way to explain that you are currently learning."),
    ("Enchanté / Enchantée.", "Nice to meet you.", "The written ending agrees with the speaker; pronunciation is generally the same."),
]
LESSON_1["examples"] += [
    ("La lettre A se prononce « ah ».", "The letter A is pronounced 'ah'.", "Se prononce means is pronounced. The letter name is being discussed."),
    ("Le mot « chat » commence par CH.", "The word chat begins with CH.", "Commence par means begins with. CH represents /ʃ/."),
    ("Dans « trois », OI se prononce /wa/.", "In trois, OI is pronounced /wa/.", "The final S in trois is silent in isolation."),
    ("Le mot « bon » contient une voyelle nasale.", "The word bon contains a nasal vowel.", "ON commonly represents /ɔ̃/ in this word."),
    ("Le R français se forme à l'arrière de la bouche.", "The French R is formed at the back of the mouth.", "À l'arrière means at the back."),
    ("Écoutez, puis répétez.", "Listen, then repeat.", "Puis means then; répétez is a polite/plural command."),
    ("Je voudrais apprendre à bien prononcer le français.", "I would like to learn to pronounce French well.", "Je voudrais is a polite conditional expression; this sentence previews later grammar."),
    ("Est-ce que vous pouvez épeler votre nom ?", "Can you spell your name?", "A useful question; épeler means to spell out."),
    ("Le son /u/ est différent du son /y/.", "The /u/ sound is different from the /y/ sound.", "Différent de means different from."),
    ("Les amis arrivent à huit heures.", "The friends arrive at eight o'clock.", "Les amis illustrates liaison: /z/ links the words."),
    ("Vous avez un livre.", "You have a book.", "Vous avez illustrates liaison between vous and avez."),
    ("Une petite amie parle français.", "A girlfriend speaks French.", "Petite has a pronounced final T before the following vowel sound; this is enchaînement."),
]
LESSON_1["conversations"] += [
    ("In a French class",
     [("Professeur", "Bonjour tout le monde !"), ("Étudiant", "Bonjour !"), ("Professeur", "Écoutez et répétez : bonjour."), ("Étudiant", "Bonjour."), ("Professeur", "Très bien. Maintenant, le mot « français »."), ("Étudiant", "Français."), ("Professeur", "Excellent !")],
     "Teacher: Hello, everyone! / Student: Hello! / Teacher: Listen and repeat: bonjour. / Student: Bonjour. / Teacher: Very good. Now the word français. / Student: Français. / Teacher: Excellent!"),
    ("Asking for spelling help",
     [("A", "Excusez-moi, comment ça s'écrit ?"), ("B", "Quel mot ?"), ("A", "« Maison »."), ("B", "M-A-I-S-O-N."), ("A", "Merci. Pouvez-vous répéter lentement ?"), ("B", "Bien sûr : M-A-I-S-O-N.")],
     "A: Excuse me, how is it spelled? / B: Which word? / A: Maison. / B: M-A-I-S-O-N. / A: Thank you. Can you repeat slowly? / B: Of course: M-A-I-S-O-N."),
    ("A beginner explains their level",
     [("A", "Bonjour ! Je parle un peu français."), ("B", "Ah oui ?"), ("A", "Oui, j'apprends le français."), ("B", "Très bien !"), ("A", "Merci. Parlez-vous anglais ?"), ("B", "Oui, un peu.")],
     "A: Hello! I speak a little French. / B: Oh, yes? / A: Yes, I am learning French. / B: Very good! / A: Thank you. Do you speak English? / B: Yes, a little."),
]
LESSON_1["exercises"] += [
    ("Which transcription represents the French R in broad IPA?", ["/r/", "/ʁ/", "/l/", "/h/"], 1, "The common French R is represented as /ʁ/."),
    ("Which word has a nasal vowel written ON?", ["bon", "chat", "café", "rue"], 0, "Bon contains the nasal vowel /ɔ̃/."),
    ("In which word is S usually pronounced /z/ because it is between vowels?", ["salut", "maison", "soir", "merci"], 1, "The single S between vowels in maison is usually /z/."),
    ("Which spelling usually represents /wa/?", ["OI", "OU", "CH", "GN"], 0, "OI commonly represents /wa/, as in trois."),
    ("Which word contains the /ʃ/ sound?", ["chat", "gare", "zéro", "vous"], 0, "CH in chat represents /ʃ/."),
    ("What is the purpose of Ç in garçon?", ["To make G soft", "To make C sound like S before A/O/U", "To make the vowel nasal", "To silence the R"], 1, "The cedilla makes C represent /s/ before A, O or U."),
    ("Which pair contrasts French U and OU?", ["tu / tout", "chat / chien", "bon / beau", "merci / matin"], 0, "Tu has /y/; tout has /u/."),
    ("What is liaison?", ["Making every final letter silent", "Linking a normally silent final consonant before a vowel sound in certain contexts", "Speaking more loudly", "Adding an extra vowel"], 1, "Liaison activates a normally silent final consonant in specific grammatical contexts."),
    ("Which phrase commonly has liaison?", ["vous avez", "chat noir", "café chaud", "rouge tomate"], 0, "In vous avez, the final S is pronounced /z/ and links to avez."),
    ("Which statement about French H is correct?", ["It is always pronounced /h/", "It is never written", "It is not pronounced, but h aspiré blocks liaison/elision", "It always makes the previous vowel nasal"], 2, "Both h muet and h aspiré are silent; h aspiré blocks certain links."),
    ("Which word begins with a soft C sound /s/?", ["café", "code", "cinéma", "cube"], 2, "C before E, I or Y is usually soft /s/."),
    ("Which spelling commonly represents /ɲ/ as in montagne?", ["GN", "PH", "OU", "OI"], 0, "GN commonly represents /ɲ/."),
    ("What does épeler mean?", ["To listen", "To spell out", "To repeat", "To understand"], 1, "Épeler means to spell a word letter by letter."),
    ("Which expression politely asks someone to speak more slowly?", ["Au revoir", "Plus lentement, s'il vous plaît", "Merci beaucoup", "Bonsoir"], 1, "Plus lentement, s'il vous plaît means more slowly, please."),
]
LESSON_1["speaking"] += [
    "Articulation drill: say /i/ (as in si), then /y/ (as in tu), then /u/ (as in tout). Repeat five slow cycles without rushing.",
    "R drill: say rue, rouge, Paris and merci gently. Keep the sound at the back of the mouth and avoid forcing your throat.",
    "Nasal drill: alternate beau–bon, peau–pont and thé–temps. Listen for the nasal resonance rather than adding a separate N.",
    "Consonant drill: say ça–ka, ce–que, gé–gué, and sa–za. Notice how spelling changes the sound.",
    "Liaison drill: say les amis, vous avez and deux enfants as connected groups. Do not insert a pause between the words.",
    "Read the café conversation once slowly, once at a natural pace, and once while looking away from the English translation.",
    "Record yourself privately if you wish, then compare the rhythm and vowel distinction. Recording is optional; this app does not require microphone access.",
]
LESSON_1["assessment"] += [
    ("Which IPA symbol is commonly used for the French R?", ["/ʁ/", "/ŋ/", "/θ/", "/x/"], 0, "French R is commonly transcribed /ʁ/."),
    ("Which word contains the nasal vowel /ɔ̃/?", ["bon", "beau", "chat", "rue"], 0, "Bon contains /ɔ̃/; beau has an oral /o/ vowel."),
    ("A single S between two vowels is often pronounced:", ["/s/", "/z/", "/ʃ/", "silent"], 1, "In maison, the S between vowels is pronounced /z/."),
    ("Which spelling usually represents /ɲ/?", ["GN", "CH", "PH", "OU"], 0, "GN represents /ɲ/ in montagne."),
    ("Which phrase demonstrates liaison?", ["vous avez", "chat noir", "café chaud", "livre rouge"], 0, "The final S in vous is pronounced /z/ before avez."),
    ("What is true about h aspiré?", ["It is pronounced /h/", "It blocks liaison and elision even though H is silent", "It makes every vowel nasal", "It is only used in verbs"], 1, "H itself is silent, but h aspiré blocks liaison and elision."),
    ("Which word has a soft C /s/?", ["café", "cube", "cinéma", "code"], 2, "C before I is normally soft /s/."),
    ("What does “épeler” mean?", ["To spell out", "To listen", "To speak slowly", "To translate"], 0, "Épeler means to spell a word letter by letter."),
    ("Which expression means “I don't understand”?", ["Je comprends.", "Je ne comprends pas.", "Je parle français.", "Au revoir."], 1, "Je ne comprends pas means I don't understand."),
    ("Which is the best description of Canadian French?", ["There is only one Canadian accent", "It is identical in every region", "It includes regional varieties with pronunciation differences", "It never uses standard French"], 2, "Canadian French includes multiple regional varieties and speaker styles."),
]
LESSON_1["summary"] += [
    "IPA can show sounds more accurately than English-style pronunciation hints.",
    "French R is usually /ʁ/; nasal vowels are produced with nasal resonance.",
    "C and G change sound depending on the following vowel; Ç marks a soft C before A, O and U.",
    "Liaison and enchaînement connect words, but they are different processes.",
    "French rhythm is built around connected syllables and phrase groups.",
    "Canadian French is diverse; Quebec French is important but not the only Canadian variety.",
]

# ---------------------------------------------------------------------
# Theme and helpers
# ---------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.stApp { background: #f7fbf7; }
.block-container { padding-top: 1.5rem; max-width: 1180px; }
[data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e7eee8; }
[data-testid="stSidebar"] * { color: #263b2d; }
h1, h2, h3 { color: #203b2a; font-weight: 900 !important; }
.eyebrow { color: #58a66b; font-size: .78rem; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
.hero { background: linear-gradient(120deg,#e5f7e8,#f1faef); border: 1px solid #d5edd9; border-radius: 24px; padding: 28px 30px; }
.hero-title { font-size: 2.1rem; font-weight: 900; color: #21452c; line-height: 1.15; }
.hero-copy { color: #52715a; font-size: 1rem; margin-top: 8px; }
.stat { background: white; border: 1px solid #e5eee6; border-radius: 18px; padding: 17px 18px; min-height: 100px; }
.stat-number { color: #2f9b4c; font-size: 1.8rem; font-weight: 900; }
.stat-label { color: #718276; font-size: .82rem; font-weight: 800; }
.lesson-card { background: white; border: 1px solid #e5eee6; border-radius: 16px; padding: 15px 17px; margin: 7px 0; }
.lesson-done { border-color: #9bd5a7; background: #f1fbf2; }
.muted { color: #718276; font-size: .9rem; }
div.stButton > button { border-radius: 13px; font-weight: 800; min-height: 2.65rem; }
div.stButton > button[kind="primary"] { background: #58b96b; border: 0; color: white; }
div.stButton > button[kind="primary"]:hover { background: #419d55; color: white; }
</style>
""", unsafe_allow_html=True)

if "xp" not in st.session_state:
    st.session_state.xp = 0
if "completed" not in st.session_state:
    st.session_state.completed = []
if "active_lesson" not in st.session_state:
    st.session_state.active_lesson = 1
if "page" not in st.session_state:
    st.session_state.page = "Home"
for key, default in (("practice_rounds", 0), ("practice_correct", 0), ("practice_total", 0),
                     ("earned_achievements", []), ("selected_language", "")):
    if key not in st.session_state:
        st.session_state[key] = default

LANGUAGES = {
    "Canadian French": {"flag": "🇨🇦", "status": "available"},
    "Angolan Portuguese": {"flag": "🇦🇴", "status": "coming soon"},
    "Gujarati": {"flag": "🇮🇳", "status": "coming soon"},
    "Hindi": {"flag": "🇮🇳", "status": "coming soon"},
    "English": {"flag": "🇬🇧", "status": "coming soon"},
}
ACHIEVEMENTS = [
    ("first_lesson", "🌱", "First steps", "Complete your first lesson", lambda: len(st.session_state.completed) >= 1),
    ("five_lessons", "📚", "Building a habit", "Complete 5 lessons", lambda: len(st.session_state.completed) >= 5),
    ("a1_complete", "🏅", "A1 explorer", "Complete 15 lessons", lambda: len(st.session_state.completed) >= 15),
    ("practice_one", "🎯", "Practice makes progress", "Complete your first practice round", lambda: st.session_state.practice_rounds >= 1),
    ("practice_ten", "🔥", "Practice regular", "Complete 10 practice rounds", lambda: st.session_state.practice_rounds >= 10),
    ("thirty_lessons", "🌍", "Language adventurer", "Complete 30 lessons", lambda: len(st.session_state.completed) >= 30),
    ("all_lessons", "🎓", "Mastery journey", "Complete all 90 lessons", lambda: len(st.session_state.completed) >= 90),
]
def refresh_achievements():
    earned = set(st.session_state.earned_achievements)
    new_titles = []
    for aid, icon, title, description, condition in ACHIEVEMENTS:
        if condition() and aid not in earned:
            earned.add(aid)
            new_titles.append(title)
    st.session_state.earned_achievements = sorted(earned)
    for title in new_titles:
        st.toast(f"Achievement unlocked: {title}", icon="🏆")

def lesson_is_unlocked(lesson_id):
    return lesson_id == 1 or (lesson_id - 1) in st.session_state.completed

def open_lesson(lesson_id):
    st.session_state.active_lesson = lesson_id
    st.session_state.page = "Lesson"

def mark_lesson_complete(lesson_id):
    if lesson_id not in st.session_state.completed:
        st.session_state.completed.append(lesson_id)
        st.session_state.xp += 25
        refresh_achievements()

# Reconcile milestones for returning users.
refresh_achievements()

# Sidebar
# Language choice is the first screen after sign-in.
if not st.session_state.selected_language:
    st.title("🌍 Choose your learning language")
    st.write("Choose an available course. More languages will appear as they are developed.")
    for language, details in LANGUAGES.items():
        left, right = st.columns([4, 1])
        with left:
            st.markdown(f"### {details['flag']} {language}")
            st.caption("Available now" if details["status"] == "available" else "Coming soon")
        with right:
            if details["status"] == "available":
                if st.button("Start learning", key=f"choose_{language}", type="primary"):
                    st.session_state.selected_language = language
                    st.session_state[f"learner_{st.session_state.active_user}_selected_language"] = language
                    st.rerun()
            else:
                st.button("Coming soon", key=f"soon_{language}", disabled=True)
    st.stop()

with st.sidebar:
    st.markdown("## 🍀 Learn Language Academy")
    st.caption(f"Signed in: {st.session_state.active_user}")
    if st.button("Sign out", use_container_width=True):
        username = st.session_state.active_user
        for field in ("xp", "completed", "active_lesson", "practice_rounds", "practice_correct", "practice_total", "earned_achievements", "selected_language"):
            st.session_state[f"learner_{username}_{field}"] = st.session_state.get(field, [] if field in ("completed", "earned_achievements") else 0)
        st.session_state.pop("active_user", None)
        for key in ("xp", "completed", "active_lesson", "page", "practice_rounds", "practice_correct", "practice_total", "earned_achievements", "selected_language"):
            st.session_state.pop(key, None)
        st.rerun()
    st.markdown("---")
    page_options = ["Home", "Learning Path", "Lesson", "Vocabulary", "Practice", "Achievements", "Settings"]
    selected_page = st.radio("YOUR LEARNING SPACE", page_options, index=page_options.index(st.session_state.page) if st.session_state.page in page_options else 0)
    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()
    st.markdown("---")
    st.markdown(f"**{LANGUAGES[st.session_state.selected_language]['flag']} {st.session_state.selected_language} · English explanations**")
    st.progress(len(st.session_state.completed) / 90)
    st.caption(f"{len(st.session_state.completed)} of 90 lessons completed")
    st.markdown(f"**⭐ {st.session_state.xp} XP**")

def page_header(kicker, title, subtitle=None):
    st.markdown(f'<div class="eyebrow">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    if subtitle:
        st.markdown(f'<p class="muted">{subtitle}</p>', unsafe_allow_html=True)

def render_authored_a1_lesson(lesson_id):
    lesson = A1_LESSONS[lesson_id]
    st.markdown(f'<div class="eyebrow">A1 · ABSOLUTE BEGINNER · LESSON {lesson_id} OF 90</div>', unsafe_allow_html=True)
    st.title(lesson["title"])
    st.markdown(f"**Goal:** {lesson['goal']}")
    st.caption("Canadian French focus · Explanations in English · Suggested study time: 30–45 minutes")
    st.progress(lesson_id / 90, text=f"Course progress · Lesson {lesson_id} of 90")
    tabs = st.tabs(["1 · Vocabulary", "2 · Grammar", "3 · Expressions", "4 · Examples", "5 · Conversations", "6 · Exercises", "7 · Speaking", "8 · Summary", "9 · Answer key & test"])
    with tabs[0]:
        st.subheader("Essential vocabulary")
        st.write("Learn each word with its meaning, an approximate pronunciation guide, IPA and an example.")
        for french, meaning, pronunciation, ipa, example in lesson["vocabulary"]:
            with st.container(border=True):
                left, right = st.columns([1, 2])
                with left:
                    st.markdown(f"### {french}")
                    st.caption(f"Say it: {pronunciation}")
                    st.caption(f"IPA: {ipa}")
                with right:
                    st.write(meaning)
                    st.markdown(f"*{example}*")
    with tabs[1]:
        st.subheader("Grammar and usage")
        for title, explanation in lesson["grammar"]:
            with st.expander(title, expanded=True):
                st.write(explanation)
        st.info("Canadian French note: these lessons teach broadly understood standard French first, and identify common Quebec usage differences where relevant.")
    with tabs[2]:
        st.subheader("Useful expressions")
        for phrase, meaning, context in lesson["expressions"]:
            with st.container(border=True):
                st.markdown(f"**{phrase}** — {meaning}")
                st.caption(context)
    with tabs[3]:
        st.subheader("French sentences in context")
        for french, english, explanation in lesson["examples"]:
            with st.container(border=True):
                st.markdown(f"### {french}")
                st.write(english)
                st.caption(explanation)
    with tabs[4]:
        st.subheader("Practical conversations")
        for title, dialogue, translation in lesson["conversations"]:
            st.markdown(f"**{title}**")
            for speaker, line in dialogue:
                st.markdown(f"- **{speaker}:** {line}")
            with st.expander("Show English translation"):
                st.write(translation)
    with tabs[5]:
        st.subheader("Practice exercises")
        st.write("Choose an answer and check it. Mistakes never block progress.")
        for index, (question, options, answer, explanation) in enumerate(lesson["exercises"]):
            selected = st.radio(question, options, index=None, key=f"a1_l{lesson_id}_exercise_{index}")
            if st.button("Check", key=f"a1_l{lesson_id}_check_{index}"):
                if selected is None:
                    st.warning("Choose an answer first.")
                elif options.index(selected) == answer:
                    st.success("Correct! " + explanation)
                else:
                    st.error("Not quite. " + explanation)
    with tabs[6]:
        st.subheader("Speaking practice")
        st.write("No microphone or recording is required. Read aloud and practise the patterns.")
        for index, instruction in enumerate(lesson["speaking"], start=1):
            st.markdown(f"{index}. {instruction}")
    with tabs[7]:
        st.subheader("What you learned")
        for item in lesson["summary"]:
            st.markdown(f"- {item}")
    with tabs[8]:
        st.subheader(f"Lesson {lesson_id} assessment")
        st.write("20 questions · One point each · No hearts, lives or failure lockout.")
        responses = []
        for index, (question, options, answer, explanation) in enumerate(lesson["assessment"]):
            selected = st.radio(question, options, index=None, key=f"a1_l{lesson_id}_assessment_{index}")
            responses.append((selected, options, answer, explanation))
        if st.button(f"Submit Lesson {lesson_id} assessment", type="primary", key=f"a1_l{lesson_id}_submit"):
            unanswered = sum(1 for selected, _, _, _ in responses if selected is None)
            if unanswered:
                st.warning(f"Please answer all 20 questions. Remaining: {unanswered}.")
            else:
                score = sum(1 for selected, options, answer, _ in responses if options.index(selected) == answer)
                st.session_state[f"a1_l{lesson_id}_score"] = score
                st.session_state[f"a1_l{lesson_id}_submitted"] = True
                st.rerun()
        if st.session_state.get(f"a1_l{lesson_id}_submitted", False):
            score = st.session_state[f"a1_l{lesson_id}_score"]
            st.metric("Your score", f"{score}/20", f"{score * 5}%")
            if score >= 18:
                st.success("Excellent work! You have a strong grasp of this lesson.")
            elif score >= 14:
                st.success("Good progress! Review the explanations for any missed answers.")
            else:
                st.info("Keep practising. You can review the lesson and retake the assessment.")
            for index, (question, options, answer, explanation) in enumerate(lesson["assessment"]):
                selected = st.session_state.get(f"a1_l{lesson_id}_assessment_{index}")
                if selected != options[answer]:
                    st.markdown(f"**{index + 1}. {question}**")
                    st.caption(f"Correct answer: {options[answer]}. {explanation}")
            if st.button("Retake assessment", key=f"a1_l{lesson_id}_retake"):
                st.session_state[f"a1_l{lesson_id}_submitted"] = False
                for index in range(len(lesson["assessment"])):
                    st.session_state.pop(f"a1_l{lesson_id}_assessment_{index}", None)
                st.rerun()
    st.markdown("---")
    st.subheader("Complete this lesson")
    st.write("Your assessment score does not block completion. Finish studying, then mark the lesson complete to unlock the next chapter.")
    if lesson_id in st.session_state.completed:
        st.success(f"Lesson {lesson_id} is already marked complete.")
    elif st.button(f"Mark Lesson {lesson_id} complete · Earn 25 XP", type="primary", key=f"complete_a1_lesson_{lesson_id}"):
        mark_lesson_complete(lesson_id)
        st.success(f"Lesson {lesson_id} completed! You earned 25 XP. Lesson {lesson_id + 1} is now unlocked.")
        st.session_state.page = "Learning Path"
        st.rerun()
    if st.button("Back to Learning Path", key=f"back_a1_lesson_{lesson_id}"):
        st.session_state.page = "Learning Path"
        st.rerun()


def render_lesson_one():
    lesson = ALL_LESSONS[0]
    st.markdown('<div class="eyebrow">A1 · ABSOLUTE BEGINNER · LESSON 1 OF 90</div>', unsafe_allow_html=True)
    st.title(lesson["title"])
    st.markdown("**Goal:** Recognise the French alphabet, understand essential sound patterns, and read simple French words.")
    st.caption("Canadian French focus · Explanations in English · Suggested study time: 35–45 minutes")
    st.progress(1 / 90, text="Course progress · Lesson 1 of 90")
    tabs = st.tabs(["1 · Vocabulary", "2 · Grammar", "3 · Expressions", "4 · Examples", "5 · Conversations", "6 · Exercises", "7 · Speaking", "8 · Summary", "9 · Answer key & test"])

    with tabs[0]:
        st.subheader("Essential vocabulary")
        st.write("Learn each word with its meaning, an approximate pronunciation guide, IPA, and an example.")
        for fr, meaning, pron, ipa, example in LESSON_1["vocabulary"]:
            with st.container(border=True):
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.markdown(f"### {fr}")
                    st.caption(f"Say it: {pron}")
                    st.caption(f"IPA: {ipa}")
                with c2:
                    st.write(meaning)
                    st.markdown(f"*{example}*")

        st.subheader("The 26 French letter names")
        alphabet = [
            ("A","ah"),("B","bay"),("C","say"),("D","day"),("E","uh"),("F","eff"),("G","zhay"),
            ("H","ahsh"),("I","ee"),("J","zhee"),("K","kah"),("L","ell"),("M","emm"),
            ("N","enn"),("O","oh"),("P","pay"),("Q","kü"),("R","air"),("S","ess"),
            ("T","tay"),("U","ü"),("V","vay"),("W","doo-bluh-vay"),("X","eeks"),("Y","ee-grek"),("Z","zed"),
        ]
        cols = st.columns(4)
        for i, (letter, sound) in enumerate(alphabet):
            with cols[i % 4]:
                st.markdown(f"**{letter}**")
                st.caption(sound)

    with tabs[1]:
        st.subheader("Grammar and pronunciation rules")
        st.write("French spelling is more predictable when you learn common letter patterns. These are useful rules, with exceptions.")
        for title, explanation in LESSON_1["grammar"]:
            with st.expander(title, expanded=True):
                st.write(explanation)
        st.info("Pronunciation reminder: English-friendly spellings are only approximations. Use the IPA symbols and repeated speaking practice to refine the sounds.")

    with tabs[2]:
        st.subheader("Useful everyday expressions")
        for phrase, meaning, context in LESSON_1["expressions"]:
            with st.container(border=True):
                st.markdown(f"**{phrase}** — {meaning}")
                st.caption(context)

    with tabs[3]:
        st.subheader("French sentences in context")
        for french, english, explanation in LESSON_1["examples"]:
            with st.container(border=True):
                st.markdown(f"### {french}")
                st.write(english)
                st.caption(explanation)

    with tabs[4]:
        st.subheader("Practical conversations")
        for title, lines, translation in LESSON_1["conversations"]:
            st.markdown(f"**{title}**")
            for speaker, line in lines:
                st.markdown(f"- **{speaker}:** {line}")
            with st.expander("Show English translation"):
                st.write(translation)

    with tabs[5]:
        st.subheader("Practice exercises")
        st.write("Choose an answer for each question. You can check your work whenever you are ready; mistakes never block progress.")
        for i, (question, options, answer, explanation) in enumerate(LESSON_1["exercises"]):
            choice = st.radio(question, options, index=None, key=f"l1_ex_{i}")
            if st.button("Check", key=f"l1_check_{i}"):
                if choice is None:
                    st.warning("Choose an answer first.")
                elif options.index(choice) == answer:
                    st.success("Correct! " + explanation)
                else:
                    st.error("Not quite. " + explanation)

    with tabs[6]:
        st.subheader("Speaking practice")
        st.write("No microphone or recording is required. Read aloud and compare your pronunciation with the guides in the vocabulary section.")
        for i, instruction in enumerate(LESSON_1["speaking"], start=1):
            st.markdown(f"{i}. {instruction}")
        st.info("For a focused drill, repeat tu–tout and rue–roue slowly. Keep the vowel difference clear.")

    with tabs[7]:
        st.subheader("What you learned")
        for item in LESSON_1["summary"]:
            st.markdown(f"- {item}")

    with tabs[8]:
        st.subheader("Comprehensive Lesson 1 assessment")
        st.write("20 questions · One point each · No hearts, lives, or failure lockout.")
        responses = []
        for i, (question, options, answer, explanation) in enumerate(LESSON_1["assessment"]):
            selected = st.radio(question, options, index=None, key=f"l1_assess_{i}")
            responses.append((selected, options, answer, explanation))
        if st.button("Submit Lesson 1 assessment", type="primary", key="l1_submit_assessment"):
            unanswered = sum(1 for selected, _, _, _ in responses if selected is None)
            if unanswered:
                st.warning(f"Please answer all 20 questions. Remaining: {unanswered}.")
            else:
                score = sum(1 for selected, options, answer, _ in responses if options.index(selected) == answer)
                st.session_state.l1_assessment_score = score
                st.session_state.l1_assessment_submitted = True
        if st.session_state.get("l1_assessment_submitted"):
            score = st.session_state.l1_assessment_score
            st.metric("Your score", f"{score}/10")
            if score >= 9:
                st.success("Excellent work! You have a strong start.")
            elif score >= 7:
                st.success("Good progress! Review any explanations you need.")
            else:
                st.info("Keep practising. You can review the lesson and retake the assessment.")
            for i, (question, options, answer, explanation) in enumerate(LESSON_1["assessment"]):
                selected = st.session_state.get(f"l1_assess_{i}")
                correct = selected == options[answer]
                st.markdown(f"{'✅' if correct else '❌'} **{i+1}. {question}**")
                if not correct:
                    st.caption(f"Correct answer: {options[answer]}. {explanation}")
            if st.button("Retake assessment", key="l1_retake"):
                st.session_state.l1_assessment_submitted = False
                for i in range(len(LESSON_1["assessment"])):
                    st.session_state.pop(f"l1_assess_{i}", None)
                st.rerun()

    st.markdown("---")
    st.subheader("Complete this lesson")
    st.write("You can complete the lesson after studying the sections and attempting the assessment. Your score does not block completion.")
    if 1 in st.session_state.completed:
        st.success("Lesson 1 is already marked complete.")
    elif st.button("Mark Lesson 1 complete · Earn 25 XP", type="primary", key="complete_lesson_1"):
        mark_lesson_complete(1)
        st.success("Lesson 1 completed! You earned 25 XP. Lesson 2 is now unlocked.")
        st.session_state.page = "Learning Path"
        st.rerun()
    if st.button("Back to Learning Path", key="back_from_lesson"):
        st.session_state.page = "Learning Path"
        st.rerun()

# ---------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------
page = st.session_state.page

if page == "Home":
    username = st.session_state.active_user
    st.markdown(f"""
    <div class="hero">
      <div class="eyebrow">YOUR {st.session_state.selected_language.upper()} JOURNEY</div>
      <div class="hero-title">Bonjour, {username}! 🇨🇦</div>
      <div class="hero-copy">A structured 90-lesson journey from A1 beginner to C2 mastery. Learn step by step, with progress and XP — never hearts or lives.</div>
    </div>
    """, unsafe_allow_html=True)
    accuracy = 100 * st.session_state.practice_correct / st.session_state.practice_total if st.session_state.practice_total else 0
    a, b, c, d = st.columns(4)
    with a:
        st.markdown(f'<div class="stat"><div class="stat-number">⭐ {st.session_state.xp}</div><div class="stat-label">TOTAL XP</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown(f'<div class="stat"><div class="stat-number">{len(st.session_state.completed)}/90</div><div class="stat-label">LESSONS COMPLETED</div></div>', unsafe_allow_html=True)
    with c:
        st.markdown(f'<div class="stat"><div class="stat-number">{st.session_state.practice_rounds}</div><div class="stat-label">PRACTICE ROUNDS</div></div>', unsafe_allow_html=True)
    with d:
        st.markdown(f'<div class="stat"><div class="stat-number">{accuracy:.0f}%</div><div class="stat-label">PRACTICE ACCURACY</div></div>', unsafe_allow_html=True)
    st.caption(f"Practice answers: {st.session_state.practice_correct} correct out of {st.session_state.practice_total} · Starting level: A1")
    page_header("CONTINUE LEARNING", "Your next lesson")
    if 1 not in st.session_state.completed:
        st.markdown("**Lesson 1 · French Alphabet, Sounds and Pronunciation**")
        st.write("Your first complete lesson is ready, with vocabulary, grammar, expressions, examples, conversations, exercises, speaking practice, summary and assessment.")
        if st.button("Start Lesson 1", type="primary"):
            st.session_state.page = "Lesson"
            st.rerun()
    else:
        next_lesson = next((x for x in ALL_LESSONS if x["id"] not in st.session_state.completed), None)
        if next_lesson:
            st.markdown(f"**Lesson {next_lesson['id']} · {next_lesson['title']}**")
            if next_lesson["id"] == 1 or next_lesson["id"] in A1_LESSONS:
                st.success("This lesson is ready. Continue your A1 journey!")
                if st.button(f"Open Lesson {next_lesson['id']}", type="primary", key="home_open_next_lesson"):
                    st.session_state.active_lesson = next_lesson["id"]
                    st.session_state.page = "Lesson"
                    st.rerun()
            else:
                st.info("This lesson is on the course roadmap. Its full content will be added in a later course update.")
        else:
            st.success("You have completed all 90 lessons!")

elif page == "Learning Path":
    page_header("YOUR COURSE", f"{st.session_state.selected_language} · A1 to C2", "All 90 lessons are listed in the exact course order. Detailed lesson content is being built progressively.")
    for level_name, titles in LEVELS.items():
        first_id = sum(len(v) for k, v in LEVELS.items() if list(LEVELS).index(k) < list(LEVELS).index(level_name)) + 1
        done_in_level = sum(1 for lesson_id in range(first_id, first_id + len(titles)) if lesson_id in st.session_state.completed)
        with st.expander(f"{level_name} · {done_in_level}/{len(titles)} complete", expanded=level_name.startswith("A1")):
            for offset, title in enumerate(titles):
                lesson_id = first_id + offset
                completed = lesson_id in st.session_state.completed
                unlocked = lesson_is_unlocked(lesson_id)
                col1, col2 = st.columns([5, 1])
                with col1:
                    icon = "✅" if completed else ("🌱" if unlocked else "🔒")
                    st.markdown(f"**{icon} Lesson {lesson_id}: {title}**")
                    has_content = lesson_id == 1 or lesson_id in A1_LESSONS
                    st.caption(("Complete lesson available now" if lesson_id == 1 else "Full lesson available · Unlocks in sequence") if has_content else "On the course roadmap · Content coming later")
                with col2:
                    if not unlocked:
                        st.button("Locked", key=f"path_locked_{lesson_id}", disabled=True)
                    elif has_content:
                        st.button("Review" if completed else "Start", key=f"path_lesson_{lesson_id}", type="primary" if not completed else "secondary", on_click=open_lesson, args=(lesson_id,))
                    else:
                        st.button("Coming soon", key=f"path_soon_{lesson_id}", disabled=True)

elif page == "Lesson":
    if st.session_state.active_lesson == 1:
        render_lesson_one()
    elif st.session_state.active_lesson in A1_LESSONS:
        render_authored_a1_lesson(st.session_state.active_lesson)
    else:
        st.warning("This lesson is on the roadmap; its full content will be added in a later course update.")
        if st.button("Return to Learning Path"):
            st.session_state.page = "Learning Path"
            st.rerun()

elif page == "Vocabulary":
    page_header("YOUR WORD BANK", "French foundations & vocabulary", "A growing reference library. New everyday topics appear automatically as you unlock the lessons where they are taught.")

    def french_number_under_100(number):
        units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
                 "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        if number <= 16:
            return units[number]
        if number < 20:
            return "dix-" + units[number - 10]
        tens = {20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante"}
        if number in tens:
            return tens[number]
        if number < 70:
            base, remainder = divmod(number, 10)
            return tens[base * 10] + (" et un" if remainder == 1 else ("-" + units[remainder] if remainder else ""))
        if number < 80:
            remainder = number - 60
            return "soixante et onze" if number == 71 else "soixante-" + (units[remainder] if remainder <= 16 else "dix-" + units[remainder - 10])
        if number == 80:
            return "quatre-vingts"
        remainder = number - 80
        return "quatre-vingt-" + (units[remainder] if remainder <= 16 else "dix-" + units[remainder - 10])

    def vocab_entries(pairs, note=""):
        return [(fr, en, "", "", note or f"{fr} = {en}") for fr, en in pairs]

    number_entries = [
        (french_number_under_100(n), str(n), "", "", f"{n} = {french_number_under_100(n)}")
        for n in range(0, 101)
    ]
    larger_number_values = [
        (100, "cent"), (200, "deux cents"), (300, "trois cents"), (400, "quatre cents"),
        (500, "cinq cents"), (600, "six cents"), (700, "sept cents"), (800, "huit cents"),
        (900, "neuf cents"), (1000, "mille"), (2000, "deux mille"), (3000, "trois mille"),
        (4000, "quatre mille"), (5000, "cinq mille"), (6000, "six mille"),
        (7000, "sept mille"), (8000, "huit mille"), (9000, "neuf mille"),
        (10000, "dix mille"), (100000, "cent mille"), (1000000, "un million"),
    ]
    larger_number_entries = [
        (word, f"{value:,}".replace(",", " "), "", "", f"{value:,} = {word}")
        for value, word in larger_number_values
    ]

    vocabulary_groups = {
        "Alphabet & letter names": [(a, b, "", "", f"Letter {a} is pronounced approximately {b}.") for a, b in [
            ("A","ah"),("B","bay"),("C","say"),("D","day"),("E","uh"),("F","eff"),("G","zhay"),("H","ahsh"),
            ("I","ee"),("J","zhee"),("K","kah"),("L","ell"),("M","emm"),("N","enn"),("O","oh"),("P","pay"),
            ("Q","kü"),("R","air"),("S","ess"),("T","tay"),("U","ü"),("V","vay"),("W","doo-bluh-vay"),
            ("X","eeks"),("Y","ee-grek"),("Z","zed")]],
    }

    # Topic collections are released with their matching lesson, not all at once.
    # Keep adding entries here as each lesson is written; unlocked topics appear automatically.
    lesson_topic_collections = {
        1: ("Lesson 1 · Alphabet & pronunciation", LESSON_1["vocabulary"]),
        2: ("Greetings & polite expressions", vocab_entries([
            ("Bonjour","Hello / Good morning"),("Bonsoir","Good evening"),("Salut","Hi / Bye"),
            ("Au revoir","Goodbye"),("À bientôt","See you soon"),("À demain","See you tomorrow"),
            ("Merci","Thank you"),("Merci beaucoup","Thank you very much"),("S'il vous plaît","Please"),
            ("De rien","You're welcome"),("Excusez-moi","Excuse me"),("Pardon","Sorry / Pardon"),
            ("Comment ça va ?","How are you?"),("Ça va bien","I'm doing well"),("Et vous ?","And you?"),
            ("Enchanté(e)","Nice to meet you")
        ])),
        3: ("Personal information & introductions", vocab_entries([
            ("Je m'appelle…","My name is…"),("Comment vous appelez-vous ?","What is your name?"),
            ("Quel âge avez-vous ?","How old are you?"),("J'ai … ans","I am … years old"),
            ("Je viens de…","I come from…"),("J'habite à…","I live in…"),("Je parle anglais","I speak English"),
            ("la langue","language"),("le pays","country"),("la ville","city"),("l'adresse","address"),
            ("le numéro de téléphone","phone number"),("l'étudiant / l'étudiante","student")
        ])),
        4: ("Numbers & counting · 0–100 and beyond", number_entries + larger_number_entries),
        5: ("Days, months, seasons & dates", vocab_entries([
            ("lundi","Monday"),("mardi","Tuesday"),("mercredi","Wednesday"),("jeudi","Thursday"),
            ("vendredi","Friday"),("samedi","Saturday"),("dimanche","Sunday"),
            ("janvier","January"),("février","February"),("mars","March"),("avril","April"),
            ("mai","May"),("juin","June"),("juillet","July"),("août","August"),("septembre","September"),
            ("octobre","October"),("novembre","November"),("décembre","December"),
            ("le printemps","spring"),("l'été","summer"),("l'automne","autumn / fall"),("l'hiver","winter"),
            ("aujourd'hui","today"),("demain","tomorrow"),("hier","yesterday"),("la date","date")
        ])),
        6: ("Time, clock & daily time expressions", vocab_entries([
            ("Quelle heure est-il ?","What time is it?"),("Il est une heure","It is one o'clock"),
            ("Il est deux heures","It is two o'clock"),("midi","noon"),("minuit","midnight"),
            ("et quart","quarter past"),("et demie","half past"),("moins le quart","quarter to"),
            ("le matin","morning"),("l'après-midi","afternoon"),("le soir","evening"),
            ("la nuit","night"),("tôt","early"),("tard","late"),("maintenant","now"),
            ("plus tard","later"),("à quelle heure ?","at what time?"),("l'horloge","clock"),
            ("la montre","watch")
        ])),
        7: ("Nouns, gender & articles", vocab_entries([
            ("le livre","the book · masculine"),("la table","the table · feminine"),
            ("un garçon","a boy · masculine"),("une fille","a girl · feminine"),
            ("l'école","the school · vowel-starting noun"),("les amis","the friends · plural"),
            ("un / une","a, an"),("le / la / l'","the · singular"),("les","the · plural"),
            ("des","some · plural"),("masculin","masculine"),("féminin","feminine"),
            ("singulier","singular"),("pluriel","plural"),("un nom","a noun")
        ])),
        8: ("Subject pronouns & être", vocab_entries([
            ("je","I"),("tu","you · informal singular"),("il","he / it"),("elle","she / it"),
            ("on","we / one / people"),("nous","we"),("vous","you · formal or plural"),
            ("ils","they · masculine or mixed"),("elles","they · feminine"),
            ("être","to be"),("je suis","I am"),("tu es","you are"),("il est","he is"),
            ("elle est","she is"),("nous sommes","we are"),("vous êtes","you are"),
            ("ils sont","they are")
        ])),
        9: ("Avoir & possession", vocab_entries([
            ("avoir","to have"),("j'ai","I have"),("tu as","you have"),("il a","he has"),
            ("elle a","she has"),("nous avons","we have"),("vous avez","you have"),
            ("ils ont","they have"),("mon / ma / mes","my"),("ton / ta / tes","your · informal"),
            ("son / sa / ses","his / her / its"),("notre / nos","our"),
            ("votre / vos","your · formal or plural"),("leur / leurs","their")
        ])),
        10: ("Adjectives & describing people", vocab_entries([
            ("grand / grande","tall / big"),("petit / petite","short / small"),
            ("jeune","young"),("vieux / vieille","old"),("gentil / gentille","kind"),
            ("intelligent / intelligente","intelligent"),("drôle","funny"),("sympathique","friendly"),
            ("beau / belle","handsome / beautiful"),("content / contente","happy"),
            ("fatigué / fatiguée","tired"),("sérieux / sérieuse","serious")
        ])),
        11: ("Family members & relationships", vocab_entries([
            ("la famille","family"),("la mère","mother"),("le père","father"),
            ("les parents","parents"),("la sœur","sister"),("le frère","brother"),
            ("la fille","daughter / girl"),("le fils","son"),("la grand-mère","grandmother"),
            ("le grand-père","grandfather"),("les grands-parents","grandparents"),
            ("la tante","aunt"),("l'oncle","uncle"),("la cousine","female cousin"),
            ("le cousin","male cousin"),("la femme","wife / woman"),("le mari","husband"),
            ("l'enfant","child"),("les enfants","children"),("un ami / une amie","a friend"),
            ("un collègue / une collègue","a colleague"),("un voisin / une voisine","a neighbour")
        ])),
        12: ("Colours, objects & describing things", vocab_entries([
            ("rouge","red"),("bleu / bleue","blue"),("vert / verte","green"),("jaune","yellow"),
            ("noir / noire","black"),("blanc / blanche","white"),("gris / grise","grey"),
            ("rose","pink"),("orange","orange"),("violet / violette","purple"),
            ("un objet","an object"),("une chose","a thing"),("la couleur","colour"),
            ("clair / claire","light"),("foncé / foncée","dark")
        ])),
        13: ("Food, drinks & restaurant vocabulary", vocab_entries([
            ("le pain","bread"),("le fromage","cheese"),("le lait","milk"),("l'eau","water"),
            ("le café","coffee"),("le thé","tea"),("le jus","juice"),("la pomme","apple"),
            ("la banane","banana"),("le poulet","chicken"),("le poisson","fish"),
            ("le riz","rice"),("les légumes","vegetables"),("les fruits","fruit"),
            ("le menu","menu"),("l'addition","the bill"),("Je voudrais…","I would like…")
        ])),
        14: ("Everyday activities & present-tense verbs", vocab_entries([
            ("parler","to speak"),("manger","to eat"),("aimer","to like / love"),("habiter","to live"),
            ("travailler","to work"),("étudier","to study"),("écouter","to listen"),
            ("regarder","to watch"),("marcher","to walk"),("jouer","to play"),
            ("tous les jours","every day"),("souvent","often"),("parfois","sometimes"),
            ("toujours","always"),("jamais","never")
        ])),
        18: ("Daily routines & reflexive actions", vocab_entries([
            ("se réveiller","to wake up"),("se lever","to get up"),("se doucher","to shower"),
            ("se laver","to wash oneself"),("s'habiller","to get dressed"),("se brosser les dents","to brush one's teeth"),
            ("se préparer","to get ready"),("se dépêcher","to hurry"),("se reposer","to rest"),
            ("se coucher","to go to bed"),("se promener","to go for a walk"),("la routine","routine")
        ])),
        22: ("House, rooms & household objects", vocab_entries([
            ("la maison","house"),("l'appartement","apartment"),("la chambre","bedroom"),
            ("le salon","living room"),("la cuisine","kitchen"),("la salle de bains","bathroom"),
            ("les toilettes","toilet / restroom"),("la salle à manger","dining room"),
            ("la porte","door"),("la fenêtre","window"),("la table","table"),("la chaise","chair"),
            ("le lit","bed"),("le canapé","sofa"),("le réfrigérateur","refrigerator"),
            ("la clé","key"),("l'escalier","stairs"),("le jardin","garden")
        ])),
        23: ("Shopping, clothes & accessories", vocab_entries([
            ("le magasin","shop / store"),("le centre commercial","shopping centre"),
            ("les vêtements","clothes"),("une chemise","shirt"),("un pantalon","trousers"),
            ("une robe","dress"),("une jupe","skirt"),("un manteau","coat"),("une veste","jacket"),
            ("des chaussures","shoes"),("des chaussettes","socks"),("un chapeau","hat"),
            ("la taille","size"),("la cabine d'essayage","fitting room"),("essayer","to try on"),
            ("acheter","to buy"),("vendre","to sell"),("C'est combien ?","How much is it?")
        ])),
        24: ("Money, prices & everyday payments", vocab_entries([
            ("l'argent","money"),("le prix","price"),("combien","how much / how many"),
            ("l'euro","euro"),("le dollar","dollar"),("les pièces","coins"),("les billets","banknotes"),
            ("la carte bancaire","bank card"),("payer","to pay"),("en espèces","in cash"),
            ("cher / chère","expensive"),(" bon marché","inexpensive"),("la monnaie","change"),
            ("le reçu","receipt"),("la réduction","discount"),("le budget","budget")
        ])),
        25: ("Restaurants, cafés & ordering food", vocab_entries([
            ("le restaurant","restaurant"),("le café","café / coffee"),("la réservation","reservation"),
            ("une table pour deux","a table for two"),("le serveur / la serveuse","waiter / waitress"),
            ("le plat","dish"),("l'entrée","starter"),("le dessert","dessert"),("la boisson","drink"),
            ("la carte","menu"),("la cuisson","cooking level"),("végétarien / végétarienne","vegetarian"),
            ("sans gluten","gluten-free"),("l'addition, s'il vous plaît","the bill, please"),
            ("Je prends…","I'll have…"),("C'était délicieux","It was delicious")
        ])),
        26: ("Transportation & asking for directions", vocab_entries([
            ("la voiture","car"),("l'autobus / le bus","bus"),("le métro","metro / subway"),
            ("le train","train"),("le taxi","taxi"),("le vélo","bicycle"),("l'avion","airplane"),
            ("la gare","train station"),("l'aéroport","airport"),("l'arrêt","stop"),
            ("un billet","ticket"),("un aller simple","one-way ticket"),("un aller-retour","return ticket"),
            ("à gauche","to the left"),("à droite","to the right"),("tout droit","straight ahead"),
            ("près de","near"),("loin de","far from"),("Où se trouve… ?","Where is…?")
        ])),
        27: ("Weather, nature & seasons", vocab_entries([
            ("Quel temps fait-il ?","What's the weather like?"),("il fait beau","the weather is nice"),
            ("il fait chaud","it is hot"),("il fait froid","it is cold"),("il pleut","it is raining"),
            ("il neige","it is snowing"),("le soleil","sun"),("la pluie","rain"),("la neige","snow"),
            ("le vent","wind"),("un nuage","cloud"),("un orage","thunderstorm"),
            ("la température","temperature"),("la forêt","forest"),("la rivière","river"),
            ("le lac","lake"),("la montagne","mountain"),("la plage","beach")
        ])),
        28: ("Health, body parts & medical expressions", vocab_entries([
            ("la tête","head"),("les yeux","eyes"),("les oreilles","ears"),("le nez","nose"),
            ("la bouche","mouth"),("la gorge","throat"),("le dos","back"),("le bras","arm"),
            ("la main","hand"),("la jambe","leg"),("le pied","foot"),("le ventre","stomach"),
            ("la santé","health"),("un médecin","doctor"),("une pharmacie","pharmacy"),
            ("un rendez-vous","appointment"),("J'ai mal à…","I have pain in…"),
            ("Je ne me sens pas bien","I don't feel well"),("une ordonnance","prescription")
        ])),
        40: ("Hobbies, interests & leisure", vocab_entries([
            ("les loisirs","leisure activities"),("la lecture","reading"),("la musique","music"),
            ("le cinéma","cinema"),("la photographie","photography"),("la cuisine","cooking"),
            ("la danse","dance"),("le sport","sport"),("la natation","swimming"),
            ("la randonnée","hiking"),("les jeux vidéo","video games"),("jouer d'un instrument","to play an instrument"),
            ("sortir avec des amis","to go out with friends"),("passer du temps","to spend time"),
            ("J'adore…","I love…"),("Je préfère…","I prefer…")
        ])),
        41: ("Travel, hotels & accommodation", vocab_entries([
            ("le voyage","trip / journey"),("les vacances","holidays / vacation"),("la destination","destination"),
            ("l'hôtel","hotel"),("la chambre","room"),("la réception","reception desk"),
            ("la réservation","reservation"),("la chambre simple","single room"),("la chambre double","double room"),
            ("les bagages","luggage"),("la valise","suitcase"),("le passeport","passport"),
            ("la carte d'embarquement","boarding pass"),("la douane","customs"),("le séjour","stay"),
            ("réserver","to book"),("annuler","to cancel"),("complet","fully booked")
        ])),
        42: ("Education, studies & professions", vocab_entries([
            ("l'école","school"),("le collège","middle school"),("le lycée","high school"),
            ("l'université","university"),("un cours","class / course"),("un devoir","homework"),
            ("un examen","exam"),("une note","grade / mark"),("un diplôme","degree / diploma"),
            ("un professeur","teacher / professor"),("un étudiant / une étudiante","student"),
            ("un ingénieur / une ingénieure","engineer"),("un médecin","doctor"),
            ("un avocat / une avocate","lawyer"),("un infirmier / une infirmière","nurse"),
            ("un métier","occupation / profession"),("étudier","to study"),("réussir","to succeed / pass")
        ])),
        43: ("Work, meetings & workplace communication", vocab_entries([
            ("le travail","work"),("le bureau","office"),("un collègue","colleague"),
            ("un responsable","manager"),("une réunion","meeting"),("un rendez-vous","appointment"),
            ("un projet","project"),("une tâche","task"),("une équipe","team"),
            ("un emploi","job"),("un salaire","salary"),("un horaire","schedule"),
            ("une pause","break"),("une échéance","deadline"),("travailler à distance","to work remotely"),
            ("envoyer un courriel","to send an email"),("prendre des notes","to take notes")
        ])),
        44: ("Feelings, opinions & social interactions", vocab_entries([
            ("heureux / heureuse","happy"),("triste","sad"),("inquiet / inquiète","worried"),
            ("nerveux / nerveuse","nervous"),("fier / fière","proud"),("déçu / déçue","disappointed"),
            ("surpris / surprise","surprised"),("calme","calm"),("en colère","angry"),
            ("être d'accord","to agree"),("ne pas être d'accord","to disagree"),
            ("à mon avis","in my opinion"),("je pense que","I think that"),("je trouve que","I find that"),
            ("selon moi","according to me"),("ça dépend","it depends")
        ])),
        55: ("Banking, finance & administration", vocab_entries([
            ("la banque","bank"),("un compte bancaire","bank account"),("un compte courant","current account"),
            ("un compte épargne","savings account"),("un virement","bank transfer"),("un retrait","withdrawal"),
            ("un dépôt","deposit"),("un distributeur automatique","ATM"),("une facture","bill / invoice"),
            ("un formulaire","form"),("un document","document"),("une pièce d'identité","ID document"),
            ("une signature","signature"),("un contrat","contract"),("les impôts","taxes"),
            ("les frais","fees"),("un prêt","loan"),("un relevé bancaire","bank statement")
        ])),
        56: ("Technology, internet & digital communication", vocab_entries([
            ("un ordinateur","computer"),("un portable","laptop / mobile phone"),("un téléphone intelligent","smartphone"),
            ("un écran","screen"),("un clavier","keyboard"),("une souris","mouse"),
            ("un fichier","file"),("un dossier","folder"),("un mot de passe","password"),
            ("un compte","account"),("un site web","website"),("une application","app"),
            ("un réseau social","social network"),("une connexion","connection"),("le Wi-Fi","Wi-Fi"),
            ("télécharger","to download"),("mettre à jour","to update"),("envoyer une pièce jointe","to send an attachment")
        ])),
        57: ("News, media & current affairs", vocab_entries([
            ("les nouvelles","news"),("l'actualité","current affairs"),("un journal","newspaper"),
            ("un article","article"),("un reportage","news report"),("un journaliste","journalist"),
            ("une chaîne","channel"),("une émission","programme / show"),("la radio","radio"),
            ("les médias","the media"),("un titre","headline"),("une source","source"),
            ("une information","piece of information"),("une entrevue","interview"),
            ("un événement","event"),("selon le reportage","according to the report")
        ])),
        58: ("Debates, arguments & persuasion", vocab_entries([
            ("un débat","debate"),("un argument","argument / point"),("un point de vue","point of view"),
            ("un avantage","advantage"),("un inconvénient","disadvantage"),("une preuve","evidence"),
            ("un exemple","example"),("un désaccord","disagreement"),("un accord","agreement"),
            ("convaincre","to convince"),("soutenir une idée","to support an idea"),
            ("remettre en question","to question / challenge"),("d'une part","on one hand"),
            ("d'autre part","on the other hand"),("cependant","however"),("en revanche","on the other hand")
        ])),
        59: ("Canadian French idioms & informal speech", vocab_entries([
            ("pantoute","not at all · informal Quebec French"),("c'est le fun","that's fun · Quebec French"),
            ("magasiner","to go shopping · Quebec French"),("un dépanneur","corner convenience store · Quebec usage"),
            ("une blonde","girlfriend · Quebec usage"),("un chum","boyfriend / buddy · Quebec usage"),
            ("bienvenue","you're welcome · common Quebec response"),("à tantôt","see you later · Quebec usage"),
            ("ça marche","that works / okay"),("c'est correct","it's okay / that's fine"),
            ("avoir de la misère","to have difficulty · Quebec expression"),
            ("être tanné","to be fed up · Quebec expression")
        ])),
        65: ("Regional Canadian French expressions", vocab_entries([
            ("un char","car · informal Quebec usage"),("une tuque","knit winter hat · Canadian usage"),
            ("des mitaines","mittens · Canadian usage"),("une fin de semaine","weekend · common Canadian French"),
            ("le dîner","lunch · common Quebec usage"),("le souper","supper / dinner · common Quebec usage"),
            ("faire frette","to be very cold · informal Quebec expression"),
            ("c'est plate","that's boring / unfortunate · Quebec usage"),
            ("une blonde","girlfriend · Quebec usage"),("un gars","guy · informal"),
            ("une fille","girl · informal"),("une gang","group / crew · informal Quebec usage")
        ])),
        66: ("Colloquial Quebec French & spoken forms", vocab_entries([
            ("chu","spoken contraction of je suis · informal"),("ch't'un","spoken contraction of je suis un · informal"),
            ("y a","spoken form of il y a · informal"),(" t'sais","spoken contraction of tu sais · informal"),
            ("ben","informal spoken form of bien"),("faque","informal spoken form meaning so / therefore"),
            ("asteur","informal Quebec form of maintenant"),("icitte","regional spoken form of ici"),
            ("pantoute","not at all · informal"),("j'sais pas","spoken contraction of je ne sais pas")
        ])),
        68: ("Professional emails, reports & formal writing", vocab_entries([
            ("Objet","Subject"),("Madame, Monsieur","Dear Sir or Madam"),("Bonjour Madame","Dear Madam"),
            ("Je vous écris au sujet de…","I am writing to you about…"),
            ("Veuillez trouver ci-joint…","Please find attached…"),("Je vous remercie de…","Thank you for…"),
            ("Je reste à votre disposition","I remain at your disposal"),
            ("Cordialement","Kind regards"),("Veuillez agréer…","Yours sincerely…"),
            ("un rapport","report"),("une pièce jointe","attachment"),("un délai","time limit"),
            ("une demande","request"),("une réponse","response"),("un suivi","follow-up")
        ])),
        69: ("Meetings, negotiations & presentations", vocab_entries([
            ("l'ordre du jour","agenda"),("un participant","participant"),("un compte rendu","meeting minutes"),
            ("un objectif","objective"),("une proposition","proposal"),("une négociation","negotiation"),
            ("un compromis","compromise"),("un accord","agreement"),("un désaccord","disagreement"),
            ("prendre la parole","to speak / take the floor"),("faire une présentation","to give a presentation"),
            ("passer au point suivant","to move to the next item"),("conclure","to conclude"),
            ("reporter une réunion","to postpone a meeting")
        ])),
        70: ("Complex opinions & abstract ideas", vocab_entries([
            ("la liberté","freedom"),("l'égalité","equality"),("la responsabilité","responsibility"),
            ("la société","society"),("la culture","culture"),("l'identité","identity"),
            ("la justice","justice"),("la confiance","trust"),("la solidarité","solidarity"),
            ("la possibilité","possibility"),("la conséquence","consequence"),("l'enjeu","issue / stake"),
            ("une perspective","perspective"),("une contradiction","contradiction"),
            ("remettre en cause","to call into question"),("prendre en considération","to take into consideration")
        ])),
        71: ("Literature, books & advanced reading", vocab_entries([
            ("un roman","novel"),("un récit","narrative / story"),("un personnage","character"),
            ("un narrateur","narrator"),("un auteur / une autrice","author"),
            ("un chapitre","chapter"),("un passage","passage"),("une intrigue","plot"),
            ("un thème","theme"),("un style","style"),("une métaphore","metaphor"),
            ("un point de vue","point of view"),("une œuvre","work / literary work"),
            ("un essai","essay"),("un recueil","collection")
        ])),
        72: ("French-Canadian society & cultural references", vocab_entries([
            ("la société québécoise","Quebec society"),("le patrimoine","heritage"),
            ("la culture francophone","Francophone culture"),("la langue officielle","official language"),
            ("la fête nationale","national holiday"),("le patrimoine culturel","cultural heritage"),
            ("une tradition","tradition"),("une coutume","custom"),("une région","region"),
            ("une communauté","community"),("la diversité","diversity"),("l'identité collective","collective identity"),
            ("le bilinguisme","bilingualism"),("la francophonie","the French-speaking world")
        ])),
        73: ("Humour, sarcasm, irony & nuance", vocab_entries([
            ("l'humour","humour"),("une blague","joke"),("une plaisanterie","joke / prank"),
            ("une taquinerie","teasing"),("le sarcasme","sarcasm"),("l'ironie","irony"),
            ("au second degré","not meant literally / tongue-in-cheek"),
            ("une expression figurée","figurative expression"),("une exagération","exaggeration"),
            ("se moquer de","to make fun of"),("faire allusion à","to allude to"),
            ("prendre au sérieux","to take seriously"),("c'est pour rire","it's just a joke")
        ])),
        74: ("Advanced listening & spontaneous conversation", vocab_entries([
            ("tu veux dire que…","you mean that…"),("si j'ai bien compris","if I understood correctly"),
            ("laisse-moi réfléchir","let me think"),("comment dire…","how can I put it…"),
            ("en fait","actually / in fact"),("disons que…","let's say that…"),
            ("ça dépend de…","it depends on…"),("je vois ce que tu veux dire","I see what you mean"),
            ("je n'avais pas pensé à ça","I hadn't thought of that"),
            ("pour revenir à…","to get back to…"),("bref","in short"),("quand même","all the same")
        ])),
        77: ("Regional Canadian French accents", vocab_entries([
            ("un accent","accent"),("la prononciation","pronunciation"),("l'intonation","intonation"),
            ("le débit","rate of speech"),("une voyelle","vowel"),("une consonne","consonant"),
            ("une syllabe","syllable"),("un son","sound"),("un accent régional","regional accent"),
            ("la langue parlée","spoken language"),("la langue familière","informal language")
        ])),
        78: ("Advanced idioms, proverbs & expressions", vocab_entries([
            ("Après la pluie, le beau temps","Every cloud has a silver lining"),
            ("Petit à petit, l'oiseau fait son nid","Little by little, the bird builds its nest"),
            ("Mieux vaut tard que jamais","Better late than never"),
            ("avoir le cœur sur la main","to be very generous"),
            ("coûter les yeux de la tête","to cost an arm and a leg"),
            ("donner sa langue au chat","to give up guessing"),
            ("tomber dans les pommes","to faint"),
            ("avoir d'autres chats à fouetter","to have other fish to fry")
        ])),
        79: ("Sophisticated vocabulary & synonyms", vocab_entries([
            ("important","important"),("essentiel","essential"),("primordial","paramount"),
            ("commencer","to begin"),("entamer","to commence"),("entreprendre","to undertake"),
            ("dire","to say"),("affirmer","to state"),("soutenir","to maintain / argue"),
            ("montrer","to show"),("démontrer","to demonstrate"),("souligner","to emphasise"),
            ("aider","to help"),("appuyer","to support"),("favoriser","to encourage / promote"),
            ("un problème","problem"),("une difficulté","difficulty"),("un enjeu","major issue")
        ])),
        81: ("Academic & literary communication", vocab_entries([
            ("une hypothèse","hypothesis"),("une théorie","theory"),("une recherche","research"),
            ("une étude","study"),("une analyse","analysis"),("une conclusion","conclusion"),
            ("une référence","reference"),("une citation","quotation / citation"),
            ("un argumentaire","argumentation"),("une bibliographie","bibliography"),
            ("une méthodologie","methodology"),("un phénomène","phenomenon"),
            ("une démarche","approach / process"),("une publication","publication")
        ])),
        82: ("Persuasive & rhetorical communication", vocab_entries([
            ("convaincre","to convince"),("persuader","to persuade"),("défendre une thèse","to defend a thesis"),
            ("mettre en évidence","to highlight"),("faire valoir","to put forward"),
            ("il va de soi que","it goes without saying that"),("force est de constater que","it must be acknowledged that"),
            ("en d'autres termes","in other words"),("à cet égard","in this regard"),
            ("cela dit","that said"),("certes","admittedly"),("néanmoins","nevertheless")
        ])),
        83: ("Professional & business communication", vocab_entries([
            ("une entreprise","company"),("un client","client"),("un fournisseur","supplier"),
            ("un partenaire","partner"),("un chiffre d'affaires","revenue / turnover"),
            ("un budget prévisionnel","projected budget"),("une stratégie","strategy"),
            ("un objectif commercial","business objective"),("un devis","quotation / estimate"),
            ("une commande","order"),("une livraison","delivery"),("une négociation","negotiation"),
            ("la rentabilité","profitability"),("un bénéfice","profit"),("une perte","loss")
        ])),
        84: ("Cultural & historical references", vocab_entries([
            ("l'histoire","history"),("un événement historique","historical event"),
            ("une époque","era"),("un siècle","century"),("une génération","generation"),
            ("un mouvement","movement"),("une révolution","revolution"),("une commémoration","commemoration"),
            ("une personnalité historique","historical figure"),("un monument","monument"),
            ("une mémoire collective","collective memory"),("un héritage","legacy")
        ])),
        85: ("Spontaneous debates & intellectual discussions", vocab_entries([
            ("je nuancerais cette idée","I would qualify that idea"),
            ("je partage en partie cet avis","I partly agree with that view"),
            ("il faut distinguer… de…","we must distinguish… from…"),
            ("cela soulève la question de…","this raises the question of…"),
            ("dans quelle mesure… ?","to what extent…?"),
            ("rien ne permet d'affirmer que…","nothing allows us to claim that…"),
            ("il convient de rappeler que…","it is worth recalling that…"),
            ("je souhaiterais revenir sur…","I would like to return to…")
        ])),
        86: ("Humour, wordplay & double meanings", vocab_entries([
            ("un jeu de mots","pun / play on words"),("un double sens","double meaning"),
            ("une expression à double sens","double entendre"),("une homonymie","homonymy"),
            ("un calembour","pun"),("une ambiguïté","ambiguity"),("une chute","punchline"),
            ("une répartie","witty retort"),("une allusion","allusion"),("un sous-entendu","implication / innuendo"),
            ("littéralement","literally"),("au sens figuré","figuratively")
        ])),
        87: ("Podcasts, radio & television vocabulary", vocab_entries([
            ("un balado","podcast · Canadian French"),("un épisode","episode"),("un animateur","host"),
            ("une animatrice","host"),("une entrevue","interview"),("un invité","guest"),
            ("un auditeur","listener"),("un téléspectateur","viewer"),("une station de radio","radio station"),
            ("une chaîne de télévision","TV channel"),("en direct","live"),("en différé","recorded / delayed"),
            ("un extrait","clip / excerpt"),("un sous-titre","subtitle")
        ])),
        88: ("Advanced creative & professional writing", vocab_entries([
            ("un brouillon","draft"),("une version finale","final version"),("un paragraphe","paragraph"),
            ("une introduction","introduction"),("une conclusion","conclusion"),("un argument","argument"),
            ("une transition","transition"),("un ton","tone"),("un registre","register"),
            ("une reformulation","rephrasing"),("une révision","revision"),("une correction","correction"),
            ("la cohérence","coherence"),("la fluidité","fluency / flow")
        ])),
        89: ("Native-level conversation & communication", vocab_entries([
            ("ça fait longtemps","it's been a long time"),("qu'est-ce que tu deviens ?","what have you been up to?"),
            ("on se tient au courant","let's keep each other updated"),("ça me ferait plaisir","I'd be happy to"),
            ("je te laisse","I'll let you go"),("on en reparle","we'll talk about it again"),
            ("c'est une bonne question","that's a good question"),("je n'y avais jamais pensé","I'd never thought about that"),
            ("pour être honnête","to be honest"),("si tu veux mon avis","if you want my opinion"),
            ("ça ne m'étonnerait pas","that wouldn't surprise me")
        ])),
    }

    for lesson_id, (collection_name, entries) in lesson_topic_collections.items():
        if lesson_is_unlocked(lesson_id):
            vocabulary_groups[collection_name] = entries

    chosen_group = st.selectbox("Choose a vocabulary collection", list(vocabulary_groups.keys()))
    search_word = st.text_input("Search this collection", placeholder="Search a French word or English meaning")
    entries = vocabulary_groups[chosen_group]
    if search_word.strip():
        needle = search_word.strip().lower()
        entries = [entry for entry in entries if needle in " ".join(str(x) for x in entry).lower()]
    st.caption(f"{len(entries)} entries · New topics appear as you unlock their lessons")
    for fr, meaning, pron, ipa, example in entries:
        with st.container(border=True):
            left, right = st.columns([1, 2])
            with left:
                st.markdown(f"**{fr}**")
                if pron or ipa:
                    st.caption(f"{pron} · {ipa}")
            with right:
                st.write(meaning)
                st.caption(example)

elif page == "Practice":
    page_header("PRACTICE CENTRE", "Choose a lesson to practise", "Each round contains 10 questions. Finish a round to see your score and earn XP; retry for a newly shuffled set. Practice never blocks lesson progress.")
    available_practice = [item for item in ALL_LESSONS if lesson_is_unlocked(item["id"]) and (item["id"] == 1 or item["id"] in A1_LESSONS)]
    practice_labels = [f"Lesson {item['id']} · {item['title']}" for item in available_practice]
    selected_practice = st.selectbox("Practice lesson", practice_labels, key="practice_lesson_select")
    selected_id = available_practice[practice_labels.index(selected_practice)]["id"]
    lesson_bank = LESSON_1 if selected_id == 1 else A1_LESSONS[selected_id]
    question_bank = lesson_bank["exercises"] + lesson_bank["assessment"]
        if "practice_questions" not in st.session_state or st.session_state.get("practice_lesson_active") != selected_id:
            st.session_state.practice_questions = random.sample(question_bank, 10)
            st.session_state.practice_lesson_active = selected_id
            st.session_state.practice_submitted = False
        if "practice_submitted" not in st.session_state:
            st.session_state.practice_submitted = False
        if st.session_state.practice_submitted:
            score = st.session_state.practice_round_score
            st.subheader("Your practice result")
            st.metric("Score", f"{score}/10", f"{score * 10}% accuracy")
            st.write(f"You got **{score} out of 10** correct.")
            st.progress(score / 10)
            st.success("Practice round completed · +15 XP earned")
            st.caption("Your next attempt will use a different shuffled set of questions.")
            if st.button("Try again · New 10 questions", type="primary", key="new_practice_round"):
                st.session_state.practice_questions = random.sample(question_bank, 10)
                st.session_state.practice_submitted = False
                st.rerun()
        else:
            for i, (question, options, answer, explanation) in enumerate(st.session_state.practice_questions):
                st.radio(f"{i+1}. {question}", options, index=None, key=f"practice_round_{st.session_state.practice_rounds}_{i}")
            if st.button("Submit 10-question practice", type="primary", key="submit_practice_round"):
                responses = [st.session_state.get(f"practice_round_{st.session_state.practice_rounds}_{i}") for i in range(10)]
                if any(value is None for value in responses):
                    st.warning(f"Please answer all 10 questions. Answered: {sum(value is not None for value in responses)}/10.")
                else:
                    score = sum(1 for response, (_, options, answer, _) in zip(responses, st.session_state.practice_questions) if options.index(response) == answer)
                    st.session_state.practice_round_score = score
                    st.session_state.practice_rounds += 1
                    st.session_state.practice_correct += score
                    st.session_state.practice_total += 10
                    st.session_state.xp += 15
                    st.session_state.practice_submitted = True
                    refresh_achievements()
                    st.rerun()

elif page == "Achievements":
    page_header("YOUR MILESTONES", "Achievements", "Earn milestones through lessons and practice. Newly unlocked achievements appear as notifications.")
    for achievement_id, icon, title, description, condition in ACHIEVEMENTS:
        earned = achievement_id in st.session_state.earned_achievements
        with st.container(border=True):
            if earned:
                st.markdown(f"### 🟩 {icon} {title} · UNLOCKED")
                st.markdown(f":green[{description}]")
            else:
                st.markdown(f"🔒 **{title}**")
                st.caption(description + " · Not yet unlocked")

elif page == "Settings":
    page_header("YOUR ACCOUNT", "Settings", "Manage your learning preferences. Progress is separated by username during this development phase.")
    st.text_input("Username", value=st.session_state.active_user, disabled=True)
    st.text_input("Native language", value="English", disabled=True)
    language_choices = [name for name, details in LANGUAGES.items() if details["status"] == "available"]
    current_language = st.session_state.selected_language if st.session_state.selected_language in language_choices else language_choices[0]
    new_language = st.selectbox("Learning language", language_choices, index=language_choices.index(current_language), key="settings_learning_language")
    if st.button("Save language preference", type="primary"):
        st.session_state.selected_language = new_language
        st.session_state[f"learner_{st.session_state.active_user}_selected_language"] = new_language
        st.success(f"Learning language set to {new_language}.")
        st.rerun()
    st.caption("More languages will appear here when their courses are ready.")
    st.divider()
    st.subheader("Reset learning progress")
    st.warning("This resets the progress for the account currently signed in: lessons, XP, practice history and achievements. Your username, password and learning-language preference will stay unchanged.")
    if not st.session_state.get("progress_reset_confirmation_open", False):
        if st.button("Reset my learning progress", type="secondary", key="start_progress_reset"):
            st.session_state.progress_reset_confirmation_open = True
            st.rerun()
    else:
        st.error(f"Are you sure you want to reset all learning progress for {st.session_state.active_user}? This cannot be undone.")
        confirm_col, cancel_col = st.columns(2)
        with confirm_col:
            if st.button("Yes, reset my progress", type="primary", key="confirm_progress_reset_button"):
                username = st.session_state.active_user
                language_preference = st.session_state.get("selected_language", "")
                # Remove this learner's cached progress while retaining their language preference.
                prefix = f"learner_{username}_"
                for cache_key in list(st.session_state.keys()):
                    if cache_key.startswith(prefix) and not cache_key.endswith("_selected_language"):
                        st.session_state.pop(cache_key, None)
                # Reset the active session's progress and transient lesson/practice state.
                reset_values = {
                    "xp": 0, "completed": [], "active_lesson": 1,
                    "practice_rounds": 0, "practice_correct": 0,
                    "practice_total": 0, "earned_achievements": [],
                }
                for key, value in reset_values.items():
                    st.session_state[key] = value
                for key in list(st.session_state.keys()):
                    if key.startswith(("l1_", "a1_l", "practice_round_")) or key in (
                        "practice_questions", "practice_submitted",
                        "practice_round_score", "practice_lesson_active",
                        "practice_lesson_select", "progress_reset_confirmation_open",
                    ):
                        st.session_state.pop(key, None)
                st.session_state.selected_language = language_preference
                st.session_state[f"learner_{username}_selected_language"] = language_preference
                st.session_state[f"learner_{username}_xp"] = 0
                st.session_state[f"learner_{username}_completed"] = []
                st.session_state[f"learner_{username}_active_lesson"] = 1
                st.session_state[f"learner_{username}_practice_rounds"] = 0
                st.session_state[f"learner_{username}_practice_correct"] = 0
                st.session_state[f"learner_{username}_practice_total"] = 0
                st.session_state[f"learner_{username}_earned_achievements"] = []
                st.session_state.page = "Home"
                st.rerun()
        with cancel_col:
            if st.button("Cancel", key="cancel_progress_reset"):
                st.session_state.progress_reset_confirmation_open = False
                st.rerun()

# Session-level per-user cache only. Official launch will move this to durable database storage.
if st.session_state.get("active_user"):
    current_username = st.session_state.active_user
    st.session_state[f"learner_{current_username}_xp"] = st.session_state.get("xp", 0)
    st.session_state[f"learner_{current_username}_completed"] = list(st.session_state.get("completed", []))
    st.session_state[f"learner_{current_username}_active_lesson"] = st.session_state.get("active_lesson", 1)
    st.session_state[f"learner_{current_username}_practice_rounds"] = st.session_state.get("practice_rounds", 0)
    st.session_state[f"learner_{current_username}_practice_correct"] = st.session_state.get("practice_correct", 0)
    st.session_state[f"learner_{current_username}_practice_total"] = st.session_state.get("practice_total", 0)
    st.session_state[f"learner_{current_username}_earned_achievements"] = list(st.session_state.get("earned_achievements", []))
    st.session_state[f"learner_{current_username}_selected_language"] = st.session_state.get("selected_language", "")
