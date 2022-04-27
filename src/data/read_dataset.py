# -*- coding: utf-8 -*-
"""
Script used to read external files in order to generate the processed set.
"""

import logging
import pandas as pd
from pathlib import Path
from typing import Tuple
from src.data.text_preprocessing import TextPreprocessing

project_dir = Path(__file__).resolve().parents[2]


class DatasetReader:
    """Handles dataset reading"""

    def __init__(self, search_file_name: str):
        self._search_file_name = search_file_name

    def get_data(self) -> Tuple[pd.DataFrame, str]:
        """Reads search dataset."""
        path = project_dir / 'data' / self._search_file_name
        logging.info(f'processing: {path}')
        df_search = pd.DataFrame
        search_term = ""
        if path.exists() and path.name.endswith('.txt'):
            reader = open(path)
            try:
                # read the file
                lines = reader.readlines()

                # search term
                search_term = lines.pop()

                # check if the search term has only one word
                assert len(search_term.split()) == 1

                # convert into a dataframe
                df_search = pd.DataFrame(lines, columns=['text'])

                # pre-process the dataset
                df_search['text'] = df_search.text.apply(lambda x: TextPreprocessing(x).extract_words())

            except Exception:
                logging.error(f'the file is empty or has a wrong format and has been skipped: {self._search_file_name}')
            finally:
                reader.close()
        else:
            logging.error(f'directory or file is invalid or does not exist: {path}')

        return df_search, search_term
