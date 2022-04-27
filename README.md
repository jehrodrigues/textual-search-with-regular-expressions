# Textual Search

**Task goal**: Search a specific term in a textual dataset.

---

### Contents

* [Installation](#installation)
* [Experimentation](#experimentation)

---

## Installation
```console
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Experimentation
in order to perform the textual search

```console
$ python -m search <search_file_name>
```

The parameter is a file (e.g. source.txt) containing the **source text** and the **search term**. The file must be inside the **./data/** directory and the extension must be .txt:
* **Source text**: lines of strings, with each line containing three words embedded in symbols, numbers and spaces
* **Search term**: always on the last line of the file, and contains a single word.