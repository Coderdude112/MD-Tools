# MD Tools

Some of these tools are made to work in the background and update MD links when they are renamed, or moved within the `notebook` folder. 
Some other tools will only work if you run them (File appender.py, Search and replace.py, and Unused image deleter.py).

### Prerequisites

* Python 3+ - [Python 3](https://www.python.org/downloads/) must be installed (The latest version is fine)
* win10toast - `pip install win10toast`
* watchdog - `pip install watchdog`

---

### Auto Tools Setup

*Note:* The only files that are "auto tools" are Link_helper.py and File_deleted.py. These programs do not delete files, they alert you so you can delete them.

*Note:* Currently MD Tools only supports direct links (Ex: `A:\Notebooks\!Typora`) not relative links (Ex: `..\Notebooks\!Typora`) I am working on support for these, and a script that will make all links relative

1. Open the variables.ini file.
2. Edit the `notebook` and `alert_file variable`  and save the file. Do **not** use quotes.
3. Start the program:
   * **To run the auto tools in the foreground**
     1. Double click on the Link_helper.py file. This will open a CMD window with Link_helper.py running.
   * **To run the auto tools in the background**
     1. Double click on the 'Starter 2.vbs' file. This will run 'Starter 1.bat' in the background, which runs Link_helper.py in that background CMD window.

---

### Variables.ini

* [Manual_variables]
  * `notebook` - The path to the MD notebook folder to watch (Ex: `A:\Notebooks`)
  * `file_type` - File types to watch. Files without this will be ignored (Ex: `.md`)
  * `alert_file` - The file to put any alerts that auto tools or manual tools. (Ex: `A:\Notebooks\ALERT`)
* [File_appender]
  * `fa_path` - The path to use with 'File appender.py' (Ex: `A:\Notebooks`)
  * `fa_text` - The text to append to all files with the extension `fa_file_type` in `fa_path`
  * `fa_file_type` - File types of files to append `fa_text` to (Ex: `.md`)
* [Search_and_replace]
  * `sar_path` - The path to use with 'Search and replace.py' (Ex: `A:\Notebooks`)
  * `sar_file_type` - The types of files to run 'Search and replace.py' on (Ex: `.md`)
  * `sar_old_string` - The text that will be replaced with `sar_new_string` in files that match the `sar_file_type` in `sar_path`
  * `sar_new_string` - The text that will replace `sar_old_string` in files that match the `sar_file_type` in `sar_path`
* [Unused_image_finder]
  'Unused image finder.py' uses the same `alert_file` as defined in [Manual_variables]
  * `uif_path` - The path to use with 'Unused image finder.py' (Ex: `A:\Notebooks`)
  * `uif_file_type` - The types of files to run 'Unused_image_finder.py' on (Ex: `.md`)
  * `uif_image_path` - The path to the image folder. This will not work if the images in the `uif_image_path` have spaces (Ex: `A:\Notebooks\!Keep in place\Images`)
* [Auto_tools_variables]
  * Don't worry about these variables, they are used by the auto tools.
  * Do **NOT** edit these variables. Seriously you could loose your files

---

### Other Notes

* The "auto files" are only Link_helper.py and File_deleted.py. You only need to run Link_helper.py to use the "auto tools"
* The "manual tools" are 'File appender.py', 'Search and replace.py', and 'Unused image finder.py' only run when you run them. When running them make sure to set their correct variables in the variables.ini file
* Once you have fixed the alerts in the `alert_file` **delete** it. If it is kept around it can cause issues
