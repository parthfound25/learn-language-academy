from pathlib import Path
import unittest


class SidebarNavigationTests(unittest.TestCase):
    def test_navigation_does_not_force_a_second_rerun(self):
        """Changing the sidebar radio already triggers Streamlit's normal rerun."""
        source = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
        start = source.index('    page_options = ["Home", "Learning Path", "Lesson", "Vocabulary", "Practice", "Achievements", "Settings"]')
        end = source.index('    st.markdown("---")', start)
        navigation_block = source[start:end]

        self.assertIn("st.session_state.page = selected_page", navigation_block)
        self.assertNotIn("st.rerun(", navigation_block)


if __name__ == "__main__":
    unittest.main()
