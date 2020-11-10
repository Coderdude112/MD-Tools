#################################################################
# Search and replace.py                                         #
# Looks for the old_string and replace it with the new_string   #
#################################################################

# Import and configure all plugins
import os
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the variables.ini file

# Define all variables, arrays, ect
sar_path = config['Search_and_replace']['sar_path']
sar_file_type = config['Search_and_replace']['sar_file_type']
sar_old_string = config['Search_and_replace']['sar_old_string']
sar_new_string = config['Search_and_replace']['sar_new_string']
files = []                      # An array with all the files in sar_path
current_file_contence = None    # The contence of the current file

def get_files():
    global files

    for r, d, f in os.walk(sar_path): # Get all the files recursively in the sar_path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if sar_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'

get_files()
for i in files: # For all the files in the list replace the old_link with the new_link
    current_file_contence = open(i).read()  # Open the file
    current_file_contence = current_file_contence.replace(sar_old_string, sar_new_string)   # Replace old_link with new_link
    open(i, "wt").write(current_file_contence)  # Write the current_file_contence to the file
