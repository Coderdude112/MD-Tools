#####################################################################################
# File_deleted.py                                                                   #
# Used along with Link_helper.py to determine weather a file was deleted or moved   #
#####################################################################################

# Import and configure all plugins
import time
import os
import configparser
import os.path
from os import path
from win10toast import ToastNotifier
n = ToastNotifier() 
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\variables.ini")    # Read the Variables.ini file

# Define variables
notebook = config['Manual_variables']['notebook']
file_type = config['Manual_variables']['file_type']
alert_file = config['Manual_variables']['alert_file']

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
def search_and_alert():
    print("Search and alert was triggered")

    files = []
    for r, d, f in os.walk(notebook):  # For all files in the look_path that also match the file type, add them to a list. (r=root, d=directories, f = files)
        for file in f:
            if file_type in file:
                files.append(os.path.join(r, file))
    for i in files: # For all the files in the list search and alert
        with open(i) as myfile:
            if old_link in myfile.read():
                with open(alert_file, "a") as alertfile:
                    alertfile.write("The file \"" + old_link + "\" was deleted. The file \"" + i + "\" still has a link to this note.\n\n")

time.sleep(1)

config.read(os.getcwd() + "\\variables.ini")    # Read the Variables.ini file
deleted = config['Auto_tools_variables']['deleted']
old_link = config['Auto_tools_variables']['old_link']
new_link = config['Auto_tools_variables']['new_link']

if deleted == "no": # The file was moved, not deleted
    search_and_replace()
    exit()
elif deleted == "yes":  # The file was deleted
    search_and_alert()

    time.sleep(2)
    if path.exists(alert_file) == True:
        n.show_toast("File Deleted", "The file " + os.path.basename(old_link) + " was deleted.\n Check the ALERT file", icon_path=os.getcwd() + "\\Alert.ico", duration=10)
        exit()
    else:
        exit()