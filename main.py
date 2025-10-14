
##main.py

import os
from textalyzer import TextAnalyzer, SourceNotFoundError

def create_large_dummy_file(filename, lines):
    """Creates a large text file for demonstration purposes."""
    print(f"Creating a large dummy file named '{filename}'...")
    with open(filename, "w") as f:
        for i in range(lines):
            f.write(f"This is line number {i}. The quick brown fox jumps over the lazy dog. \n")
    print("Dummy file created.")

def main():
    """Main function to demonstrate the Textalyzer library."""
    large_file = "large_document.txt"
    
    # Create a large file to showcase memory efficiency
    create_large_dummy_file(large_file, 100000) # 100,000 lines
    
    print("\n--- Analyzing a Large File ---")
    try:
        # The generator ensures we don't load all 100k lines into memory at once
        file_analyzer = TextAnalyzer(large_file)
        
        word_count = file_analyzer.count_words()
        print(f"Total word count: {word_count}")
        
        frequencies = file_analyzer.get_word_frequency()
        print(f"Top 5 most common words: {frequencies.most_common(5)}")

    except SourceNotFoundError as e:
        print(f"ERROR: {e}")
    finally:
        # Clean up the dummy file
        if os.path.exists(large_file):
            os.remove(large_file)
            print(f"\nCleaned up {large_file}.")
            
    print("\n--- Analyzing a Non-Existent File (to show exception handling) ---")
    try:
        analyzer = TextAnalyzer("this_file_does_not_exist.txt")
    except SourceNotFoundError as e:
        print(f"Successfully caught expected error: {e}")


if __name__ == "__main__":
    main()