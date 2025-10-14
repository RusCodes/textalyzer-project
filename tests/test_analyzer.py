# tests/test_analyzer.py

import unittest
import os
from collections import Counter
from textalyzer.analyzer import TextAnalyzer, SourceNotFoundError

class TestTextAnalyzer(unittest.TestCase):
    """Unit tests for the TextAnalyzer class."""

    def setUp(self):
        """Set up a temporary test file before each test."""
        self.test_file_path = "test_doc.txt"
        with open(self.test_file_path, "w") as f:
            f.write("Hello world! This is a test. Hello again, world.")
        
        self.string_source = "Python is great. Python is also fun!"

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_word_count_from_file(self):
        """Test counting words from a file source."""
        analyzer = TextAnalyzer(self.test_file_path)
        # Expected words: hello, world, this, is, a, test, hello, again, world -> 9 words
        self.assertEqual(analyzer.count_words(), 9)

    def test_word_frequency_from_file(self):
        """Test getting word frequency from a file source."""
        analyzer = TextAnalyzer(self.test_file_path)
        freq = analyzer.get_word_frequency()
        expected = Counter({'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'again': 1})
        self.assertEqual(freq, expected)
        
    def test_word_count_from_string(self):
        """Test counting words from a string source."""
        analyzer = TextAnalyzer(self.string_source)
        # Expected words: python, is, great, python, is, also, fun -> 7 words
        self.assertEqual(analyzer.count_words(), 7)

    def test_word_frequency_from_string(self):
        """Test getting word frequency from a string source."""
        analyzer = TextAnalyzer(self.string_source)
        freq = analyzer.get_word_frequency()
        expected = Counter({'python': 2, 'is': 2, 'great': 1, 'also': 1, 'fun': 1})
        self.assertEqual(freq, expected)

    def test_file_not_found_error(self):
        """Test that SourceNotFoundError is raised for a non-existent file."""
        with self.assertRaises(SourceNotFoundError):
            TextAnalyzer("non_existent_file.txt")
            
    def test_empty_file(self):
        """Test handling of an empty file."""
        empty_file = "empty.txt"
        open(empty_file, 'w').close() # create empty file
        analyzer = TextAnalyzer(empty_file)
        self.assertEqual(analyzer.count_words(), 0)
        self.assertEqual(analyzer.get_word_frequency(), Counter())
        os.remove(empty_file)

# This allows running tests directly from the command line
if __name__ == '__main__':
    unittest.main()