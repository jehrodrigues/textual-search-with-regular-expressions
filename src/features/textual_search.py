# -*- coding: utf-8 -*-
"""
Script used to perform the search function on the dataset.
"""

import re
import logging
import pandas as pd
from typing import List


class TextualSearch:
    """Handles search feature"""

    def __init__(self, df_search: pd.DataFrame, search_term: str):
        self._df_search = df_search
        self._search_term = search_term

    def search_term(self) -> List[str]:
        """Search the term in the dataset."""
        logging.info(f'search term: {self._search_term}')
        output_search = []
        try:
            # regular expression to search the term
            output_search = self._df_search.text.apply(lambda x: [x] if re.search(self._search_term, x,
                                                                                  flags=re.IGNORECASE) else None).dropna().values.tolist()
        except Exception:
            logging.error(f'source text or search term has a wrong format.')

        return output_search
