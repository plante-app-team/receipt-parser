from unittest import TestCase
from unittest.mock import patch

from src.handlers.home import home_handler


class TestHomeHandler(TestCase):
    @patch("src.handlers.home.Environment")
    def test_home_handler(self, mock_env):
        mock_env.return_value.get_template.return_value.render.return_value = (
            "Rendered Template"
        )
        status_code, template = home_handler()
        self.assertEqual(status_code, 200)
        self.assertIsNotNone(template)
