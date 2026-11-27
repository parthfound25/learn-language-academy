from pathlib import Path
import unittest


class ResponsiveLayoutTests(unittest.TestCase):
    def test_device_toggle_offers_mobile_and_laptop_views(self):
        source = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
        self.assertIn('st.session_state.device_view = "mobile" if st.session_state.device_view == "laptop" else "laptop"', source)
        self.assertIn('switch_label = "📱" if st.session_state.device_view == "laptop" else "💻"', source)
        self.assertIn("device-mobile-marker", source)
        self.assertIn("device-laptop-marker", source)

    def test_layout_stays_responsive_on_narrow_screens(self):
        source = (Path(__file__).resolve().parents[1] / "app.py").read_text(encoding="utf-8")
        self.assertIn("@media (max-width: 768px)", source)
        self.assertIn("max-width: 460px", source)
        self.assertIn("flex-wrap: wrap", source)


if __name__ == "__main__":
    unittest.main()
