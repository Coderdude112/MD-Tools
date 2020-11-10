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
config.read(os.getcwd() + "\\variables.ini")    # Read the variables.ini file

# Define all variables, arrays, ect
working_path = config['Global']['working_path']
file_type = config['Global']['file_type']
last_deleted_file = None    # The filename of the last deleted file
old_link = None             # The old link that needs to be replaced with new_link
new_link = None             # The link that will replace old_link
files = []                  # An array wit all the files in notebook

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):  
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*' + file_type],ignore_patterns=['.~*'],ignore_directories=False,case_sensitive=False)  # Set the patterns for PatternMatchingEventHandler

    def on_any_event(self, event):
        if event.event_type == "modified":  # The file was modified
            return
        elif event.event_type == "moved":   # The file was renamed
            global old_link
            global new_link

            old_link = event.src_path
            new_link = event.dest_path
            
            search_and_replace()
        elif event.event_type == "created" and os.path.basename(event.src_path) != last_deleted_file:   # The file was just created
            config['Auto_tools_variables']['deleted'] = 'no'
            config['Auto_tools_variables']['new_link'] = event.src_path
            config.write(open(os.getcwd() + "\\variables.ini", 'w'))
        elif event.event_type == "deleted": # The file might have been deleted, but were not sure. We will run File_deleted.py to know for sure
            config['Auto_tools_variables']['deleted'] = 'yes'
            config['Auto_tools_variables']['old_link'] = event.src_path
            config.write(open(os.getcwd() + "\\variables.ini", 'w'))

            subprocess.Popen([os.getcwd() + "\\File_deleted.py"], shell=True)   # Fork and run File_deleted.py

def get_files():
    global files

    for r, d, f in os.walk(working_path): # Get all the files recursively in the path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def search_and_replace():
    get_files() # Get the files in the notebooks folder
        
    for i in files: # For all the files in the list replace the old_link with the new_link
        current_file_contence = open(i).read()  # Open the file
        current_file_contence = current_file_contence.replace(old_link, new_link)   # Replace old_link with new_link
        open(i, "wt").write(current_file_contence)  # Write the current_file_contence to the file

if __name__ == "__main__":
    print('Starting...')
    src_path = working_path
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
