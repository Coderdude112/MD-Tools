#################################################################
# Search and replace.py                                         #
# Looks for the old_string and replace it with the new_string   #
#################################################################

# Import plugins
import os
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the Variables.ini file

# Define variables
sar_path = config['Search_and_replace']['sar_path']
sar_file_type = config['Search_and_replace']['sar_file_type']
sar_old_string = config['Search_and_replace']['sar_old_string']
sar_new_string = config['Search_and_replace']['sar_new_string']

def get_files():
    global files
    files = []

    for r, d, f in os.walk(sar_path):   # Get all the files recursively in the 'sar_path' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if sar_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'

get_files()
for i in files: # For all the files in the list replace the sar_old_link with the sar_new_link
    openfile = open(i, "rt")
    data = openfile.read()
    data = data.replace(sar_old_string, sar_new_string)

    openfile.close()
    openfile = open(i, "wt")
    openfile.write(data)
    openfile.close()