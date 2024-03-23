import unittest
from unittest.mock import patch, mock_open

from colore.colors import all_colors, color_code, basic_colors, custom_aliases


class TestColors(unittest.TestCase):

    def test_color_code(self):
        self.assertEqual(color_code("31"), "\033[31m")
        self.assertEqual(color_code("42"), "\033[42m")
        self.assertEqual(color_code("82"), "\033[82m")
        self.assertEqual(color_code("100"), "\033[100m")

    def test_basic_colors(self):
        colors = basic_colors()
        self.assertEqual(colors["yellow"], "\033[33m")
        self.assertEqual(colors["lblue"], "\033[94m")
        self.assertEqual(colors["_yellow"], "\033[43m")
        self.assertEqual(colors["_lblue"], "\033[104m")

    @patch("os.path.expanduser", return_value="/home/user")
    @patch("os.path.isfile", side_effect=[True, False])
    @patch("builtins.open", new_callable=mock_open, read_data="new_name 31\n")
    def test_custom_aliases(self, mock_open_file, mock_isfile,
                            mock_expanduser):
        aliases = custom_aliases()
        self.assertEqual(aliases["new_name"], "\033[31m")
        self.assertNotIn("not_exist", aliases)

    @patch("colore.colors.basic_colors",
           return_value={"red": "\033[31m", "green": "\033[32m"})
    @patch("colore.colors.custom_aliases",
           return_value={"yellow": "\033[43m", "blue": "\033[34m"})
    def test_all_colors(self, mock_custom_aliases, mock_basic_colors):
        colors = all_colors()
        self.assertEqual(colors["red"], "\033[31m")
        self.assertEqual(colors["green"], "\033[32m")
        self.assertEqual(colors["yellow"], "\033[43m")
        self.assertEqual(colors["blue"], "\033[34m")

    @patch.dict("colore.colors.FG", {"fg_color": "90"})
    @patch.dict("colore.colors.BG", {"_bg_color": "104"})
    def test_all_colors_compounds(self):
        colors = all_colors()
        self.assertEqual(colors["fg_color"], "\033[90m")
        self.assertEqual(colors["_bg_color"], "\033[104m")
        self.assertEqual(colors["fg_color_bg_color"], "\033[90;104m")


if __name__ == "__main__":
    unittest.main()
