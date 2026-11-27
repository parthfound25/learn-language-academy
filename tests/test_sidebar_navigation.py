from pathlib import Path
import unittest


class SidebarNavigationTests(unittest.TestCase):
    def test_navigation_uses_callback_without_forcing_a_second_rerun(self):
        """The keyed radio callback updates the page before Streamlit's normal rerun."""
        source = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
        start = source.index('    page_options = ["Home", "Learning Path", "Lesson", "Vocabulary", "Practice", "Achievements", "Settings"]')
        end = source.index('    st.markdown("---")', start)
        navigation_block = source[start:end]

        self.assertIn('key="main_navigation"', navigation_block)
        self.assertIn("on_change=sync_navigation_page", navigation_block)
        self.assertIn("def sync_navigation_page():", source)
        self.assertIn('st.session_state.page = selected', source)
        self.assertNotIn("st.rerun(", navigation_block)


if __name__ == "__main__":
    unittest.main()
