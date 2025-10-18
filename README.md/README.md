# Textalyzer 📝

Textalyzer is a small, memory-efficient Python library for basic text analysis. It's designed to process large text files without loading them entirely into memory by using generators to stream data.

## Features

-   Memory Efficient: Uses generators to process large files line-by-line.
-   Flexible API: Analyze text directly from a file path or a string.
-   Core Analyses:
    -   Count total words.
    -   Calculate word frequencies.
-   Built-in Logging: Provides informative logs about its operations.
-   Custom Exception: Raises `SourceNotFoundError` for missing files.
-   Well-Documented: Includes clear docstrings for all classes and methods.
-   Unit Tested: Comes with a suite of unit tests to ensure reliability.

## Installation

Currently, this is a local module. To use it, simply place the `textalyzer` directory in your project folder and import it.

## Usage

Here's a quick example of how to use `Textalyzer`.

python
from textalyzer import TextAnalyzer, SourceNotFoundError

# --- Analyzing a File ---
try:
    # Create a dummy file for the example
    with open("my_book.txt", "w") as f:
        f.write("This library is simple, but this library is effective.")

    analyzer = TextAnalyzer("my_book.txt")

    word_count = analyzer.count_words()
    print(f"Total words: {word_count}") # Output: Total words: 9

    frequencies = analyzer.get_word_frequency()
    print(f"Most common word: {frequencies.most_common(1)}") # Output: Most common word: [('this', 2)]

except SourceNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# --- Analyzing a String ---
text_block = "Analyzing text is fun. Text analysis can be insightful!"
string_analyzer = TextAnalyzer(text_block)
print(f"Word count from string: {string_analyzer.count_words()}") # Output: 9