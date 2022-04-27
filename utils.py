# -*- coding: utf-8 -*-
"""
Helper utilities and decorators.
"""

import pandas as pd
from IPython.display import Markdown, display
from src.features.textual_search import TextualSearch


def format_output(text):
    """Format the output."""
    output = ""
    for t in text:
        output += str(t).replace("'", "") + "\n"
    return output


def printmd(text):
    """Display a markdown."""
    display(Markdown(text))


def make_color(text, color):
    """Set a color."""
    start = "<span style='color:" + color + "'>"
    return start + text + "</span>"


def search_interactive(source, term):
    """Perform a interactive search."""
    df_search = pd.DataFrame(eval(source), columns=['text'])
    output_search = TextualSearch(df_search, term).search_term()
    printmd("Output: <br>" + make_color(str(format_output(output_search)), 'green'))
