import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class NavigationTests(unittest.TestCase):
    def test_sidebar_navigation_uses_stable_key_and_single_callback(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn('key="main_navigation"', app)
        self.assertIn("on_change=sync_navigation_page", app)
        self.assertIn('st.session_state.page = selected', app)
        self.assertNotIn("if selected_page != st.session_state.page:", app)
        self.assertNotIn("st.rerun()", app.split('st.radio(\n            "YOUR LEARNING SPACE"', 1)[1].split('st.markdown("---")', 1)[0])

    def test_sidebar_navigation_resynchronizes_after_in_page_navigation(self):
        app = (ROOT / "app.py").read_text(encoding="utf-8")
        self.assertIn('if st.session_state.get("main_navigation") != st.session_state.page:', app)
        self.assertIn('st.session_state.main_navigation = st.session_state.page if st.session_state.page in page_options else "Home"', app)


if __name__ == "__main__":
    unittest.main()
