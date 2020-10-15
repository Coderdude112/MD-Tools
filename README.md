# MD Tools

These tools are made to work in the background and update MD links when they are renamed, or moved within the `notebook` folder. It will also make a note if a file is deleted that still has a link

### Prerequisites

* Python 3+ - [Python 3](https://www.python.org/downloads/) must be installed (The latest version is fine)

---

### Setup

1. Open the variables.ini file.
2. Edit the `notebook` and `alert_file variable  and save the file. Do **not** use quotes.
3. Start the program by running the 'Link helper.py' file

---

### Variables.ini

* `notebook` - The path to the notebook folder (Ex: A:\Notebooks)
* `file_type` - File types to watch. Files without this will be ignored (Ex: .md)
* `alert_file` - The alert file. This is used if a file is deleted, but still has a link somewhere else in the `notebook` folder. (Ex: A:\Notebooks\ALERT)

Do **not** edit the variables under the `[Auto_tools_variables]`.
