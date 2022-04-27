import re
import logging
from typing import List


class TextPreprocessing(object):
    """
    Handles text pre-processing
    """

    def __init__(self, text: str):
        self._text = text

    def extract_words(self) -> List[str]:
        """Take a text and extract the words containing only alphabets."""
        clean_text = []
        words_pattern = '[a-z]+'
        try:
            # extract words containing only alphabets
            clean_text = re.findall(words_pattern, self._text, flags=re.IGNORECASE)

            # convert list to string
            clean_text = ' '.join(clean_text)

            # check if the text has only three words
            assert len(clean_text.split()) == 3
        except Exception:
            logging.error(f'has a wrong format and failed: {clean_text}')

        return clean_text
