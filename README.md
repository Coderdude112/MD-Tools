# MD Tools

Tools within the 'Auto tools' dir are made to run in the background 100% of the time. These auto tools update MD links when they are renamed, or moved within the `notebook_dir`.
Tools within the 'Semi-auto tools' dir can be run on a regular schedule but shouldn't be run in the background 100% of the time.
Tools within the 'Manual tools' are tools that you only should run once (Such as 'File appender.py').

### Prerequisites

* Python 3+ - [Python 3](https://www.python.org/downloads/) must be installed (The latest version is fine)
* win10toast - `pip install win10toast`
* watchdog - `pip install watchdog`

---

### Auto Tools Setup

*Note:* Currently MD Tools only supports direct links (Ex: `A:\Notebooks\!Typora`) not relative links (Ex: `..\Notebooks\!Typora`) I am working on support for these.

Do **not** use quotes when setting any variables.

1. Open the variables.ini file.
2. Set the `notebook_dir` variable to the base directory of your markdown notebook.
3. If you do not use .md files set `file_type` to the extension of the files that make up your notebook.
4. Set the `alert_file` to a empty file (If this does not exist MD Tools will create it with this path). This will be used when making detailed alerts.
5. Start the program:
   * **To run the auto tools in the foreground**: Double click on the Link_helper.py file. This will open a CMD window with Link_helper.py running.
   * **To run the auto tools in the background**: Double click on the 'Starter 2.vbs' file. This will run 'Starter 1.bat' in the background, which runs Link_helper.py in that background CMD window.

---

### Variables.ini

#### Globals

These variables are used in most files. Paths / directories in the variables.ini file are never in quotes (Spaces are OK)

| Variable name | Use / comment                                                |
| ------------- | ------------------------------------------------------------ |
| notebook_dir  | The base directory of the notebook                           |
| images_dir    | The directory where all images used in the markdown notebook are stored |
| file_type     | The file extension of the files that make-up the notebook (This is usually .md for markdown notebooks) |
| alert_file    | The file to use when making detailed alerts to the user      |

#### Other

| Variable name  | Use / comment                                                |
| -------------- | ------------------------------------------------------------ |
| fa_text        | The text to append when using 'File appender.py'             |
| sar_old_string | The string that will be replaced by sar_new_string when using 'Search and replace.py' |
| sar_new_string | The string that will replace the sar_old_string when using 'Search and replace.py' |

#### Auto_tools_variables-do_NOT_edit

**DO NOT EDIT** these variables. This will cause issues

| Variable name | Use / comment                                                |
| ------------- | ------------------------------------------------------------ |
| deleted       | If this is "yes" then a file was deleted. If this is "no" then a file was moved directories |
| old_link      | The old link that will be replaced by the new_link           |
| new_link      | The new link that will replace the old_link                  |
