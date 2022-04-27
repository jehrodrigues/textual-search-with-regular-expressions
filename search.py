# -*- coding: utf-8 -*-
import logging
import argparse
from src.features.textual_search import TextualSearch
from src.data.read_dataset import DatasetReader


if __name__ == '__main__':
    # Parser descriptors
    parser = argparse.ArgumentParser(
        description='''Script used to perform the textual search.''')

    parser.add_argument('search_file_name',
                        # nargs='*',
                        help='The file must be inside the ./data/ directory and the extension must be .txt: {source.txt}.')

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    args = parser.parse_args()
    search_file_name = args.search_file_name

    # Data reader
    df_search, search_term = DatasetReader(search_file_name).get_data()

    # Textual Search
    output_search = TextualSearch(df_search, search_term).search_term()

    # Output
    logging.info(f'output: ')
    [print("[" + ' '.join(out) + "]") for out in output_search]
