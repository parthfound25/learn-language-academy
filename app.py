import hmac
import streamlit as st

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

def lesson_is_unlocked(lesson_id):
    return lesson_id == 1 or (lesson_id - 1) in st.session_state.completed

def open_lesson(lesson_id):
    st.session_state.active_lesson = lesson_id
    st.session_state.page = "Lesson"

def mark_lesson_complete(lesson_id):
    if lesson_id not in st.session_state.completed:
        st.session_state.completed.append(lesson_id)
        st.session_state.xp += 25

# Sidebar
with st.sidebar:
    st.markdown("## 🍀 Learn Language")
    st.caption(f"Signed in: {st.session_state.active_user}")
    if st.button("Sign out", use_container_width=True):
        username = st.session_state.active_user
        st.session_state[f"learner_{username}_xp"] = st.session_state.get("xp", 0)
        st.session_state[f"learner_{username}_completed"] = st.session_state.get("completed", [])
        st.session_state[f"learner_{username}_active_lesson"] = st.session_state.get("active_lesson", 1)
        st.session_state.pop("active_user", None)
        for key in ("xp", "completed", "active_lesson", "page"):
            st.session_state.pop(key, None)
        st.rerun()
    st.markdown("---")
    page_options = ["Home", "Learning Path", "Vocabulary", "Practice", "Achievements", "Settings"]
    selected_page = st.radio("YOUR LEARNING SPACE", page_options, index=page_options.index(st.session_state.page) if st.session_state.page in page_options else 0)
    if selected_page != st.session_state.page:
        st.session_state.page = selected_page
        st.rerun()
    st.markdown("---")
    st.markdown("**🇨🇦 Canadian French · English explanations**")
    st.progress(len(st.session_state.completed) / 90)
    st.caption(f"{len(st.session_state.completed)} of 90 lessons completed")
    st.markdown(f"**⭐ {st.session_state.xp} XP**")

def page_header(kicker, title, subtitle=None):
    st.markdown(f'<div class="eyebrow">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    if subtitle:
        st.markdown(f'<p class="muted">{subtitle}</p>', unsafe_allow_html=True)

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
        st.write("10 questions · One point each · No hearts, lives, or failure lockout.")
        responses = []
        for i, (question, options, answer, explanation) in enumerate(LESSON_1["assessment"]):
            selected = st.radio(question, options, index=None, key=f"l1_assess_{i}")
            responses.append((selected, options, answer, explanation))
        if st.button("Submit Lesson 1 assessment", type="primary", key="l1_submit_assessment"):
            unanswered = sum(1 for selected, _, _, _ in responses if selected is None)
            if unanswered:
                st.warning(f"Please answer all 10 questions. Remaining: {unanswered}.")
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
                for i in range(10):
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
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">YOUR CANADIAN FRENCH JOURNEY</div>
      <div class="hero-title">Bonjour, learner! 🇨🇦</div>
      <div class="hero-copy">A structured 90-lesson journey from A1 beginner to C2 mastery. Learn step by step, with progress and XP — never hearts or lives.</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    a, b, c = st.columns(3)
    with a:
        st.markdown(f'<div class="stat"><div class="stat-number">⭐ {st.session_state.xp}</div><div class="stat-label">TOTAL XP</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown(f'<div class="stat"><div class="stat-number">{len(st.session_state.completed)}/90</div><div class="stat-label">LESSONS COMPLETED</div></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="stat"><div class="stat-number">A1</div><div class="stat-label">STARTING LEVEL</div></div>', unsafe_allow_html=True)
    st.write("")
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
            st.info("The full detailed content for each lesson is being added one lesson at a time. Lesson 1 is currently available in full.")
            if next_lesson["id"] == 2:
                st.button("Open Lesson 2", disabled=True, help="Lesson 2 content will be added in the next curriculum update.")
        else:
            st.success("You have completed all 90 lessons!")

elif page == "Learning Path":
    page_header("YOUR COURSE", "Canadian French · A1 to C2", "All 90 lessons are listed in the exact course order. Detailed lesson content is being built progressively.")
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
                    if lesson_id == 1:
                        st.caption("Complete lesson available now · Canadian French pronunciation focus")
                    elif lesson_id == 2:
                        st.caption("Next lesson in the sequence · Detailed content will be added next")
                    else:
                        st.caption("On the course roadmap")
                with col2:
                    if lesson_id == 1:
                        st.button("Review" if completed else "Start", key=f"path_lesson_{lesson_id}", type="primary" if not completed else "secondary", on_click=open_lesson, args=(1,))
                    elif not unlocked:
                        st.button("Locked", key=f"path_locked_{lesson_id}", disabled=True)
                    elif lesson_id == 2:
                        st.button("Coming next", key=f"path_next_{lesson_id}", disabled=True)
                    else:
                        st.button("Coming soon", key=f"path_soon_{lesson_id}", disabled=True)

elif page == "Lesson":
    if st.session_state.active_lesson == 1:
        render_lesson_one()
    else:
        st.warning("The detailed content for this lesson has not been added yet. Lesson 1 is the current completed-content milestone.")
        if st.button("Return to Learning Path"):
            st.session_state.page = "Learning Path"
            st.rerun()

elif page == "Vocabulary":
    page_header("YOUR WORD BANK", "French vocabulary", "Vocabulary from the complete Lesson 1 course content.")
    for fr, meaning, pron, ipa, example in LESSON_1["vocabulary"]:
        with st.container(border=True):
            left, right = st.columns([1, 2])
            with left:
                st.markdown(f"**{fr}**")
                st.caption(f"{pron} · {ipa}")
            with right:
                st.write(meaning)
                st.caption(example)

elif page == "Practice":
    page_header("QUICK PRACTICE", "Practise your French", "Try a question from Lesson 1. Mistakes never block your progress.")
    practice_items = LESSON_1["exercises"]
    if "practice_question" not in st.session_state:
        st.session_state.practice_question = 0
    idx = st.session_state.practice_question % len(practice_items)
    question, options, answer, explanation = practice_items[idx]
    selected = st.radio(question, options, index=None, key=f"practice_choice_{idx}")
    if st.button("Check answer", type="primary"):
        if selected is None:
            st.warning("Choose an answer first.")
        elif options.index(selected) == answer:
            st.success("Correct! " + explanation)
        else:
            st.info("Not quite. " + explanation)
    if st.button("Next question"):
        st.session_state.practice_question += 1
        st.rerun()

elif page == "Achievements":
    page_header("YOUR MILESTONES", "Achievements", "Celebrate learning milestones. No hearts or lives.")
    milestones = [
        ("🌱", "First steps", "Complete your first lesson", len(st.session_state.completed) >= 1),
        ("📚", "Getting consistent", "Complete 5 lessons", len(st.session_state.completed) >= 5),
        ("🏅", "A1 explorer", "Complete 15 lessons", len(st.session_state.completed) >= 15),
        ("🌍", "Language adventurer", "Complete 30 lessons", len(st.session_state.completed) >= 30),
        ("🎓", "French mastery journey", "Complete all 90 lessons", len(st.session_state.completed) >= 90),
    ]
    for icon, title, description, earned in milestones:
        with st.container(border=True):
            st.markdown(f"{'✅' if earned else icon} **{title}**")
            st.caption(description + (" · Unlocked" if earned else " · Not yet unlocked"))

elif page == "Settings":
    page_header("YOUR ACCOUNT", "Settings", "Your learner account is managed through Streamlit Secrets.")
    st.text_input("Username", value=st.session_state.active_user, disabled=True)
    st.text_input("Native language", value="English", disabled=True)
    st.text_input("Learning language", value="Canadian French", disabled=True)
    st.caption("To add another learner, add their username and password under the [users] section in Streamlit Secrets.")

# Persist this learner's progress within the current Streamlit session.
if st.session_state.get("active_user"):
    current_username = st.session_state.active_user
    st.session_state[f"learner_{current_username}_xp"] = st.session_state.get("xp", 0)
    st.session_state[f"learner_{current_username}_completed"] = st.session_state.get("completed", [])
    st.session_state[f"learner_{current_username}_active_lesson"] = st.session_state.get("active_lesson", 1)
