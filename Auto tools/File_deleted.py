#############################################################################
# File_deleted.py                                                           #
# Run by Link_helper.py to determine weather a file was deleted or moved    #
#############################################################################

# Import and configure all plugins
import time, os
from win10toast import ToastNotifier
n = ToastNotifier() 
import configparser
config = configparser.ConfigParser()

# Wait a second so we can really dertime if a file was deleted or just moved, then read the variables.ini file
time.sleep(1)
config.read(os.getcwd() + "\\variables.ini")    # Read the variables.ini file

# Define all variables, arrays, ect
working_path = config['Global']['working_path']
file_type = config['Global']['file_type']
alert_file = config['Global']['alert_file']
deleted = config['Auto_tools_variables']['deleted']
old_link = config['Auto_tools_variables']['old_link']
new_link = config['Auto_tools_variables']['new_link']
files = []  # An array with all of the files notebook

def get_files():
    global files

    for r, d, f in os.walk(working_path): # Get all the files recursively in the notebook (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def search_and_replace():
    get_files() # Get the files in the notebooks folder
        
    for i in files: # For all the files in the list replace the old_link with the new_link
        current_file_contence = open(i).read()  # Open the file
        current_file_contence = current_file_contence.replace(old_link, new_link)   # Replace old_link with new_link
        open(i, "wt").write(current_file_contence)  # Write the current_file_contence to the file
def search_and_alert():
    get_files()

    for i in files: # For all the files in the files array search and alert
        current_file_contence = open(i).read()
        if old_link in current_file_contence:
            global need_to_alert

            need_to_alert = True
            open(alert_file, "a").write("The file *" + os.path.basename(old_link) + "* was deleted, but the file **[" + os.path.basename(i) + "](" + i + ")** still has a link to the deleted file.\n")

if deleted == "no": # The file was moved, not deleted
    search_and_replace()
elif deleted == "yes":  # The file was deleted
    search_and_alert()

if need_to_alert == True:   # A broken link has been created due to the file being deleted so we need to alert the user
    n.show_toast("Broken Link", "Due to " + os.path.basename(old_link) + " being deleted a broken link has been created.\nCheck the ALERT file", icon_path=os.getcwd() + "\\Alert.ico", duration=10)
    open(alert_file, "a").write("\n")
