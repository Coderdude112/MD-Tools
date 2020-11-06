#############################################################################
# File_deleted.py                                                           #
# Run by Link_helper.py to determine weather a file was deleted or moved    #
#############################################################################

# Import and configure all plugins
import time
import os
import os.path
from os import path
from win10toast import ToastNotifier
n = ToastNotifier() 
import configparser
config = configparser.ConfigParser()

# Make all variables global
global notebook, file_type, alert_file, deleted, old_link, new_link

# Wait a second so we can really dertime if a file was deleted or just moved
time.sleep(1)
config.read(os.getcwd() + "\\variables.ini")    # Read the Variables.ini file

# Define variables
notebook = config['Manual_variables']['notebook']
file_type = config['Manual_variables']['file_type']
alert_file = config['Manual_variables']['alert_file']
deleted = config['Auto_tools_variables']['deleted']
old_link = config['Auto_tools_variables']['old_link']
new_link = config['Auto_tools_variables']['new_link']

def get_files():
    global files
    files = []
    
    for r, d, f in os.walk(notebook):   # Get all the files recursively in the 'notebook' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def search_and_replace():
    get_files()

    for i in files: # For all the files in the files array search and replace
        openfile = open(i, "rt")
        data = openfile.read()
        data = data.replace(old_link, new_link)

        openfile.close()
        openfile = open(i, "wt")
        openfile.write(data)
        openfile.close()
def search_and_alert():
    get_files()

    for i in files: # For all the files in the files array search and alert
        with open(i) as myfile:
            if old_link in myfile.read():
                with open(alert_file, "a") as alertfile:
                    alertfile.write("The file *" + os.path.basename(old_link) + "* was deleted, but the file **[" + os.path.basename(i) + "](" + i + ")** still has a link to the deleted file.\n\n")
                    n.show_toast("File Deleted", "The file " + os.path.basename(old_link) + " was deleted.\n Check the ALERT file", icon_path=os.getcwd() + "\\Alert.ico", duration=10)

if deleted == "no": # The file was moved, not deleted
    search_and_replace()
    exit()
elif deleted == "yes":  # The file was deleted
    search_and_alert()
    exit()
