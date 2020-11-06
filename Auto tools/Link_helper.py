#####################################################################
# Link_helper.py                                                    #
# Watches a folder for changes and updates links in MD documents    #
#####################################################################

# Import and configure all plugins
import time, os, subprocess, fileinput
import watchdog.events, watchdog.observers
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\variables.ini")    # Read the Variables.ini file

# Make all variables global
global notebook, file_type, last_deleted_file, old_link, new_link

# Define all variables
notebook = config['Manual_variables']['notebook']
file_type = config['Manual_variables']['file_type']
last_deleted_file = None    # Just the filename of the last deleted file
old_link = None             # The link to search for in the files
new_link = None             # The link to replace the old link with

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):  
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*' + file_type],ignore_patterns=['.~*'],ignore_directories=False,case_sensitive=False)  # Set the patterns for PatternMatchingEventHandler

    def on_any_event(self, event):
        if event.event_type == "modified":  # The file was modified
            return
        elif event.event_type == "moved":   # The file was renamed
            old_link = event.src_path
            new_link = event.dest_path
            
            search_and_replace()
            return
        elif event.event_type == "created" and os.path.basename(event.src_path) != last_deleted_file:   # The file was just created
            config['Auto_tools_variables']['deleted'] = 'no'
            config['Auto_tools_variables']['new_link'] = event.src_path
            with open(os.getcwd() + "\\variables.ini", 'w') as configfile:
                config.write(configfile)

            return
        elif event.event_type == "deleted": # The file might have been deleted, but were not sure. We will run File_deleted.py to know for sure
            config['Auto_tools_variables']['deleted'] = 'yes'
            config['Auto_tools_variables']['old_link'] = event.src_path
            with open(os.getcwd() + "\\variables.ini", 'w') as configfile:
                config.write(configfile)

            subprocess.Popen([os.getcwd() + "\\File_deleted.py"], shell=True)
            return

def get_files():
    global files
    files = []

    for r, d, f in os.walk(notebook):   # Get all the files recursively in the 'notebook' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def search_and_replace():
    get_files() # Get the files in the notebooks folder
        
    for i in files: # For all the files in the list replace the old_link with the new_link
        openfile = open(i, "rt")
        data = openfile.read()
        data = data.replace(old_link, new_link)

        openfile.close()
        openfile = open(i, "wt")
        openfile.write(data)
        openfile.close()

if __name__ == "__main__":
