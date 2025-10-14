# textalyzer/__init__.py

"""
Textalyzer: A simple text analysis library.

This library provides a TextAnalyzer class for analyzing text from files or strings,
focusing on memory efficiency for large files through the use of generators.
"""

from .analyzer import TextAnalyzer, SourceNotFoundError

__version__ = "0.1.0"
__author__ = "Gemini AI"