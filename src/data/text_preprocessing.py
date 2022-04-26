import re
from typing import List


class TextPreprocessing(object):
    """
    Handles text pre-processing
    """

    def __init__(self, text: str):
        self._text = text

    def extract_words(self) -> List[str]:
        """Take a text and extract the words containing only alphabets and more than two characters."""
        words_pattern = '[a-z][a-z]+'
        try:
            clean_text = re.findall(words_pattern, self._text, flags=re.IGNORECASE)
            clean_text = ' '.join(clean_text)
        except Exception:
            print(self._text + " has the wrong format and failed.")
        return clean_text
