#####################################################################
# Link_helper.py                                                    #
# Watches a folder for changes and updates links in MD documents    #
# Works with File-deleted.py for when a file moves or is deleted    #
#####################################################################

# Import and configure all plugins
import time
import os
import subprocess
import fileinput
import watchdog.events
import watchdog.observers
import configparser
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\variables.ini")    # Read the Variables.ini file

# Define all variables
notebook = config['Manual_variables']['notebook']
file_type = config['Manual_variables']['file_type']
last_deleted_file = "NOT SET YET"   # Just the filename of the last deleted file
last_event = "NOT SET YET"          # Used to see what the last event was
old_link = "NOT SET YET"            # The link to search for in the files
new_link = "NOT SET YET"            # The link to replace the old link with 

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):  
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.md'],ignore_patterns=['.~*'],ignore_directories=False,case_sensitive=False)  # Set the patterns for PatternMatchingEventHandler

    def on_any_event(self, event):
        global notebook
        global file_type
        global last_deleted_file
        global last_event
        global old_link
        global new_link

        if event.event_type == "modified":  # The file was modified
            return
        elif event.event_type == "moved":   # The file was renamed
            old_link = event.src_path
            new_link = event.dest_path
            
            search_and_replace()
            record_last_event(event.event_type)
            return
        elif event.event_type == "created" and os.path.basename(event.src_path) != last_deleted_file:   # The file was just created
            config['Auto_tools_variables']['deleted'] = 'no'
            config['Auto_tools_variables']['new_link'] = event.src_path
            with open(os.getcwd() + "\\variables.ini", 'w') as configfile:
                config.write(configfile)

            record_last_event(event.event_type)
            return
        elif event.event_type == "deleted": # The file might have been deleted so we will run "File_deleted.py"
            config['Auto_tools_variables']['deleted'] = 'yes'
            config['Auto_tools_variables']['old_link'] = event.src_path
            with open(os.getcwd() + "\\variables.ini", 'w') as configfile:
                config.write(configfile)

            subprocess.Popen([os.getcwd() + "\\File_deleted.py"], shell=True)

            record_last_event(event.event_type)
            return
            
def search_and_replace():
    print("Search and replace was triggered")

    files = []
    for r, d, f in os.walk(notebook):  # For all files in the look_path that also match the file type, add them to a list. (r=root, d=directories, f = files)
        for file in f:
            if file_type in file:
                files.append(os.path.join(r, file))
    for i in files: # For all the files in the list search and replace
        openfile = open(i, "rt")
        data = openfile.read()
        data = data.replace(old_link, new_link)

        openfile.close()
        openfile = open(i, "wt")
        openfile.write(data)
        openfile.close()
def record_last_event(event_type):
    global last_event

    last_event = event_type

if __name__ == "__main__":
    print('Starting...')
    src_path = notebook
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