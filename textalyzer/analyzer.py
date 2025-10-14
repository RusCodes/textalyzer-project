# textalyzer/analyzer.py

import logging
import string
from collections import Counter
import os

# --- Setup Logging ---
# Configure logging to provide informative output during the library's operations.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# --- Custom Exception ---
class SourceNotFoundError(FileNotFoundError):
    """Custom exception raised when the text source (file) cannot be found."""
    pass


# --- Core Class: TextAnalyzer ---
class TextAnalyzer:
    """
    A class to perform text analysis on a given source (file path or string).

    This analyzer is designed to be memory-efficient by streaming content from
    files line-by-line using a generator, making it suitable for large files.
    """

    # In textalyzer/analyzer.py, inside the TextAnalyzer class

    # In textalyzer/analyzer.py, inside the TextAnalyzer class

    def __init__(self, source):
        """
        Initializes the TextAnalyzer with a source.

        Args:
            source (str): A file path or a block of text.

        Raises:
            SourceNotFoundError: If the source is a path that does not exist.
        """
        self.source = source
        is_on_disk = os.path.exists(source)

        # --- THIS IS THE CORRECTED LOGIC ---
        # A tuple of common text file extensions
        file_extensions = ('.txt', '.md', '.log', '.csv', '.json')
        
        # Check if the source looks like a path
        looks_like_path = ('/' in source or '\\' in source or source.endswith(file_extensions))

        if is_on_disk and os.path.isfile(source):
            self._is_file = True
            logger.info(f"Initialized TextAnalyzer for file: {source}")
        elif not is_on_disk and looks_like_path:
            # If it's not on disk but LOOKS like a path, raise the error.
            raise SourceNotFoundError(f"The file path '{source}' was not found.")
        elif isinstance(source, str):
            # Otherwise, it's a string for analysis.
            self._is_file = False
            logger.info("Initialized TextAnalyzer for a string source.")
        else:
            raise TypeError("Source must be a valid file path or a string.")

    def _words_generator(self):
        """
        A generator that yields cleaned words from the source.

        It streams from a file or iterates over a string, ensuring low memory usage.
        Words are converted to lowercase and stripped of punctuation.

        Yields:
            str: A cleaned word from the source text.
        """
        if self._is_file and not os.path.exists(self.source):
            raise SourceNotFoundError(f"The file path '{self.source}' was not found.")
        
        if self._is_file:
            try:
                with open(self.source, 'r', encoding='utf-8') as f:
                    for line in f:
                        # Replace punctuation with space, then split
                        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
                        cleaned_line = line.translate(translator)
                        for word in cleaned_line.split():
                            yield word.lower()
            except FileNotFoundError:
                logger.error(f"File not found during analysis: {self.source}")
                raise SourceNotFoundError(f"The file path '{self.source}' was not found.")
            except Exception as e:
                logger.error(f"An unexpected error occurred while reading file: {e}")
                raise
        else: # The source is a string
            translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
            cleaned_text = self.source.translate(translator)
            for word in cleaned_text.split():
                yield word.lower()

    def count_words(self):
        """
        Counts the total number of words in the source.

        Returns:
            int: The total word count.
        """
        logger.info(f"Starting word count analysis...")
        count = sum(1 for _ in self._words_generator())
        logger.info(f"Word count completed. Total words: {count}")
        return count

    def get_word_frequency(self):
        """
        Calculates the frequency of each word in the source.

        Returns:
            collections.Counter: A Counter object mapping words to their frequencies.
        """
        logger.info(f"Starting word frequency analysis...")
        frequencies = Counter(self._words_generator())
        logger.info(f"Word frequency analysis completed.")
        return frequencies