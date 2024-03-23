import re
import unittest
from io import StringIO
from unittest.mock import patch, mock_open

from colore.filter import from_args, from_file, filter_lines, get_pairs


class TestFilterFunctions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open,
           read_data="pattern1\ncolor1\npattern2\ncolor2\n")
    @patch("colore.filter.all_colors", create=True,
           return_value={"color1": "\033[30m", "color2": "\033[32m"})
    def test_from_file(self, mock_all_colors, mock_open_file):
        patterns, colors = from_file("test_path")
        self.assertEqual(len(patterns), 2)
        self.assertEqual(patterns[0].pattern, "pattern1")
        self.assertEqual(patterns[1].pattern, "pattern2")
        self.assertEqual(colors[0], "\033[30m")
        self.assertEqual(colors[1], "\033[32m")

    @patch('builtins.open', create=True)
    def test_from_file_oserror(self, mock_open):
        mock_open.side_effect = OSError('Mocked OSError')
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            with self.assertRaises(SystemExit):
                from_file('test.txt')
        self.assertEqual(fake_stdout.getvalue(), "Mocked OSError\n")

    @patch("sys.argv",
           ["script_name", "pattern1", "color1", "pattern2", "color2"])
    @patch("colore.filter.all_colors",
           return_value={"color1": "\033[30m", "color2": "\033[32m"})
    def test_from_args(self, mock_all_colors):
        patterns, colors = from_args()
        self.assertEqual(len(patterns), 2)
        self.assertEqual(patterns[0].pattern, "pattern1")
        self.assertEqual(patterns[1].pattern, "pattern2")
        self.assertEqual(colors[0], "\033[30m")
        self.assertEqual(colors[1], "\033[32m")

    @patch("colore.filter.all_colors",
           return_value={"color1": "\033[30m", "color2": "\033[32m"})
    def test_get_pairs(self, mock_all_colors):
        pairs = ("pattern1", "color1", "pattern2", "color2", "pattern3", "32;1;4")
        patterns, colors = get_pairs(pairs)
        self.assertEqual(len(patterns), 3)
        self.assertEqual(patterns[0].pattern, "pattern1")
        self.assertEqual(patterns[1].pattern, "pattern2")
        self.assertEqual(patterns[2].pattern, "pattern3")
        self.assertEqual(colors[0], "\033[30m")
        self.assertEqual(colors[1], "\033[32m")
        self.assertEqual(colors[2], "\033[32;1;4m")

    def test_get_pairs_error(self):
        pairs = ("patt(ern1", "color1")
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            with self.assertRaises(SystemExit):
                patterns, colors = get_pairs(pairs)
            self.assertEqual(fake_stdout.getvalue(), "missing ), unterminated subpattern at position 4\n")

    @patch("sys.stdin", StringIO("line1\npattern2\nline3\n"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_filter_lines(self, mock_stdout):
        patterns = [re.compile("pattern1"), re.compile("pattern2")]
        colors = ["\033[30m", "\033[32m"]
        filter_lines((patterns, colors))
        self.assertEqual(
            mock_stdout.getvalue(), "line1\n\033[32mpattern2\033[0m\nline3\n"
        )


if __name__ == "__main__":
    unittest.main()
