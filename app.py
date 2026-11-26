import streamlit as st

st.set_page_config(
    page_title="Learn Language Academy by Parth",
    page_icon="🇫🇷",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Secrets-based username and password authentication ---
import hmac

try:
    configured_users = dict(st.secrets["users"])
except Exception:
    configured_users = {}

if not configured_users:
    st.title("🍀 Learn Language Academy by Parth")
    st.error("No learner accounts are configured.")
    st.markdown("Add usernames and passwords in Streamlit → App settings → Secrets:")
    st.code('[users]\n"Parth Sharma" = "CHOOSE_A_NEW_PASSWORD"\n"Another User" = "CHOOSE_ANOTHER_PASSWORD"', language="toml")
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

# --- Theme ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.stApp { background: #f7fbf7; }
.block-container { padding-top: 1.6rem; max-width: 1180px; }
[data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e7eee8; }
[data-testid="stSidebar"] * { color: #263b2d; }
h1, h2, h3 { color: #203b2a; font-weight: 900 !important; }
.eyebrow { color: #58a66b; font-size: .78rem; font-weight: 900; letter-spacing: .12em; text-transform: uppercase; }
.hero { background: linear-gradient(120deg,#e5f7e8,#f1faef); border: 1px solid #d5edd9; border-radius: 24px; padding: 28px 30px; }
.hero-title { font-size: 2.15rem; font-weight: 900; color: #21452c; line-height: 1.15; }
.hero-copy { color: #52715a; font-size: 1rem; margin-top: 8px; }
.stat { background: white; border: 1px solid #e5eee6; border-radius: 18px; padding: 17px 18px; min-height: 105px; }
.stat-number { color: #2f9b4c; font-size: 1.8rem; font-weight: 900; }
.stat-label { color: #718276; font-size: .82rem; font-weight: 800; }
.unit { background: white; border: 1px solid #e5eee6; border-radius: 18px; padding: 17px; }
.lesson-node { background: #ffffff; border: 1px solid #e4eee5; border-radius: 16px; padding: 14px 16px; margin: 8px 0; }
.lesson-done { border-color: #9bd5a7; background: #f1fbf2; }
.small-muted { color: #718276; font-size: .88rem; }
div.stButton > button { border-radius: 13px; font-weight: 800; min-height: 2.7rem; }
div.stButton > button[kind="primary"] { background: #58b96b; border: 0; color: white; }
div.stButton > button[kind="primary"]:hover { background: #419d55; color: white; }
hr { border-color: #e6eee7; }
</style>
""", unsafe_allow_html=True)

# --- Starter content (will move into Supabase in the next build stage) ---
LESSONS = [
    {"id": 1, "title": "Bonjour !", "subtitle": "Say hello and goodbye", "unit": "First steps", "xp": 10, "words": [
        ("Bonjour", "Hello / Good morning", "bohn-zhoor"),
        ("Salut", "Hi / Bye (informal)", "sah-loo"),
        ("Bonsoir", "Good evening", "bohn-swahr"),
        ("Au revoir", "Goodbye", "oh ruh-vwahr"),
        ("Merci", "Thank you", "mehr-see"),
    ]},
    {"id": 2, "title": "My name is…", "subtitle": "Introduce yourself", "unit": "First steps", "xp": 10, "words": [
        ("Je m'appelle…", "My name is…", "zhuh mah-pell"),
        ("Comment tu t'appelles ?", "What is your name? (informal)", "koh-mahn too tah-pell"),
        ("Enchanté(e)", "Nice to meet you", "ahn-shahn-tay"),
    ]},
    {"id": 3, "title": "How are you?", "subtitle": "Ask and answer how someone is", "unit": "First steps", "xp": 10, "words": [
        ("Ça va ?", "How are you? / Is it going well?", "sah vah"),
        ("Ça va bien.", "I'm doing well.", "sah vah byan"),
        ("Très bien, merci.", "Very well, thank you.", "treh byan mehr-see"),
    ]},
]

if "xp" not in st.session_state:
    st.session_state.xp = 0
if "completed" not in st.session_state:
    st.session_state.completed = []
if "active_lesson" not in st.session_state:
    st.session_state.active_lesson = 1

# --- Sidebar ---
with st.sidebar:
    st.markdown('## 🍀 Learn Language')
    st.caption(f"Signed in: {st.session_state.active_user}")
    if st.button('Sign out', use_container_width=True):
        username = st.session_state.active_user
        st.session_state[f"learner_{username}_xp"] = st.session_state.get("xp", 0)
        st.session_state[f"learner_{username}_completed"] = st.session_state.get("completed", [])
        st.session_state[f"learner_{username}_active_lesson"] = st.session_state.get("active_lesson", 1)
        st.session_state.pop("active_user", None)
        for key in ("xp", "completed", "active_lesson", "page_lesson"):
            st.session_state.pop(key, None)
        st.rerun()
    st.caption("ACADEMY BY PARTH")
    st.markdown("---")
    page = st.radio(
        "YOUR LEARNING SPACE",
        ["Home", "Learning Path", "Vocabulary", "Practice", "Achievements", "Settings"],
        label_visibility="visible",
    )
    st.markdown("---")
    st.markdown("**🇫🇷 French · A1 Beginner**")
    st.progress(len(st.session_state.completed) / len(LESSONS))
    st.caption(f"{len(st.session_state.completed)} of {len(LESSONS)} starter lessons completed")
    st.markdown(f"**⭐ {st.session_state.xp} XP**")

# --- Reusable UI ---
def header(label, title, subtitle=None):
    st.markdown(f'<div class="eyebrow">{label}</div>', unsafe_allow_html=True)
    st.title(title)
    if subtitle:
        st.markdown(f'<p class="small-muted">{subtitle}</p>', unsafe_allow_html=True)

def start_lesson(lesson_id):
    st.session_state.active_lesson = lesson_id
    st.session_state.page_lesson = True

# --- Pages ---
if page == "Home":
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">YOUR FRENCH JOURNEY STARTS HERE</div>
      <div class="hero-title">Bonjour, learner! 🇫🇷</div>
      <div class="hero-copy">Small lessons. Real progress. A new language, one step at a time.</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    a, b, c = st.columns(3)
    with a:
        st.markdown(f'<div class="stat"><div class="stat-number">⭐ {st.session_state.xp}</div><div class="stat-label">TOTAL XP</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown(f'<div class="stat"><div class="stat-number">{len(st.session_state.completed)}/{len(LESSONS)}</div><div class="stat-label">LESSONS COMPLETED</div></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="stat"><div class="stat-number">A1</div><div class="stat-label">CURRENT LEVEL</div></div>', unsafe_allow_html=True)
    st.write("")
    header("CONTINUE LEARNING", "Your French path")
    st.markdown("**Unit 1 · First steps**")
    st.progress(len(st.session_state.completed) / len(LESSONS))
    for lesson in LESSONS:
        done = lesson["id"] in st.session_state.completed
        left, right = st.columns([5, 1])
        with left:
            icon = "✅" if done else "🌱" if lesson["id"] == 1 or (lesson["id"] - 1) in st.session_state.completed else "🔒"
            st.markdown(f'<div class="lesson-node {"lesson-done" if done else ""}">{icon} &nbsp; <b>{lesson["title"]}</b><br><span class="small-muted">{lesson["subtitle"]} · {lesson["xp"]} XP</span></div>', unsafe_allow_html=True)
        with right:
            if done:
                st.button("Review", key=f"review_{lesson['id']}", on_click=start_lesson, args=(lesson["id"],))
            elif lesson["id"] == 1 or (lesson["id"] - 1) in st.session_state.completed:
                st.button("Start", key=f"start_{lesson['id']}", type="primary", on_click=start_lesson, args=(lesson["id"],))
            else:
                st.button("Locked", key=f"locked_{lesson['id']}", disabled=True)
elif page == "Learning Path":
    header("YOUR COURSE", "French · A1 Beginner", "Your course is organised into levels, units, lessons and checkpoints.")
    st.info("The complete A1–C2 curriculum will be added in the curriculum build stage. This is the first starter unit.")
    st.markdown("### Unit 1 · First steps")
    for lesson in LESSONS:
        done = lesson["id"] in st.session_state.completed
        st.markdown(f'{"✅" if done else "📗"} **Lesson {lesson["id"]}: {lesson["title"]}** — {lesson["subtitle"]}')

elif page == "Vocabulary":
    header("YOUR WORD BANK", "French vocabulary", "Words from your starter lessons.")
    rows = [word for lesson in LESSONS for word in lesson["words"]]
    for fr, en, pron in rows:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**{fr}**")
                st.caption(pron)
            with col2:
                st.write(en)

elif page == "Practice":
    header("QUICK PRACTICE", "Test what you know", "A short starter question. More exercise types will be added next.")
    question = st.radio("What does **Merci** mean?", ["Hello", "Thank you", "Goodbye", "Please"], index=None)
    if st.button("Check answer", type="primary"):
        if question == "Thank you":
            st.success("Correct! Merci means thank you.")
        elif question:
            st.error("Not quite. The correct answer is Thank you.")
        else:
            st.warning("Choose an answer first.")

elif page == "Achievements":
    header("YOUR MILESTONES", "Achievements", "Celebrate progress as you learn.")
    st.markdown("⭐ **Getting started** — Earn your first XP")
    st.markdown("📚 **First lesson** — Complete your first lesson")
    st.caption("Achievements will unlock automatically as you make progress.")

elif page == "Settings":
    header("YOUR ACCOUNT", "Settings", "Personalise your learning experience.")
    st.text_input("Username", value=st.session_state.active_user, disabled=True)
    st.text_input("Native language", value="English", disabled=True)
    st.text_input("Learning language", value="French", disabled=True)
    st.caption("Your account is managed through the usernames configured in Streamlit Secrets.")

# Lesson view is opened from the Home page.
if st.session_state.get("active_lesson") and st.session_state.get("page_lesson"):
    lesson = next((x for x in LESSONS if x["id"] == st.session_state.active_lesson), None)
    if lesson:
        st.markdown("---")
        st.markdown(f"### Lesson {lesson['id']} · {lesson['title']}")
        st.write(lesson["subtitle"])
        for fr, en, pron in lesson["words"]:
            st.markdown(f"**{fr}** — {en}  \n<small>{pron}</small>", unsafe_allow_html=True)
        if st.button("Finish lesson", type="primary", key="finish_lesson"):
            if lesson["id"] not in st.session_state.completed:
                st.session_state.completed.append(lesson["id"])
                st.session_state.xp += lesson["xp"]
            st.session_state.page_lesson = False
            st.success(f"Lesson completed! +{lesson['xp']} XP")
            st.rerun()


# Save this learner's progress separately within the current Streamlit session.
if st.session_state.get("active_user"):
    current_username = st.session_state.active_user
    st.session_state[f"learner_{current_username}_xp"] = st.session_state.get("xp", 0)
    st.session_state[f"learner_{current_username}_completed"] = st.session_state.get("completed", [])
    st.session_state[f"learner_{current_username}_active_lesson"] = st.session_state.get("active_lesson", 1)
