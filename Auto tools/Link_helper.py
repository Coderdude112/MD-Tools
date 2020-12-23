#####################################################################
# Link_helper.py                                                    #
# Watches a folder for changes and updates links in MD documents    #
#####################################################################

# Import and configure all plugins
import time, os, subprocess, fileinput, sys, watchdog.events, watchdog.observers, configparser
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
file_type = ini_file['Globals']['file_type']        # The file extension of the files that make-up the notebook (This is usually .md for markdown notebooks)
notebook_dir = ini_file['Globals']['notebook_dir']  # The base directory of the notebook

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*' + file_type],ignore_patterns=['.~*'],ignore_directories=False,case_sensitive=False)    # Set the patterns for PatternMatchingEventHandler

    def on_any_event(self, event):
        if event.event_type == "modified":  # The file was modified
            return
        elif event.event_type == "moved":   # The file was renamed
            mdf.search_and_replace(notebook_dir, file_type, event.src_path, event.dest_path)
        elif event.event_type == "created": # The file was just created
            ini_file['Auto_tools_variables-do_NOT_edit']['deleted'] = 'no'
            ini_file['Auto_tools_variables-do_NOT_edit']['new_link'] = event.src_path
            ini_file.write(open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini", 'w', encoding='utf-8'))
        elif event.event_type == "deleted": # The file might have been deleted, but we're not sure. So, we will run File_deleted.py incase the file was moved
            ini_file['Auto_tools_variables-do_NOT_edit']['deleted'] = 'yes'
            ini_file['Auto_tools_variables-do_NOT_edit']['old_link'] = event.src_path
            ini_file.write(open(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini", 'w', encoding='utf-8'))

            subprocess.Popen([os.getcwd() + "\\File_deleted.py"], shell=True)   # Fork and run File_deleted.py

if __name__ == "__main__":
    print('Link_helper.py has successfully started.\nIf you read this, I hope you have an amazing day!')
    src_path = notebook_dir
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
