from pathlib import Path


def test_sidebar_navigation_does_not_force_a_second_rerun():
    """Changing the sidebar radio already triggers Streamlit's normal rerun."""
    source = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
    start = source.index('    page_options = ["Home", "Learning Path", "Lesson", "Vocabulary", "Practice", "Achievements", "Settings"]')
    end = source.index('    st.markdown("---")', start)
    navigation_block = source[start:end]

    assert "st.session_state.page = selected_page" in navigation_block
    assert "st.rerun(" not in navigation_block
