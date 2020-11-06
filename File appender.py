#########################################################################
# File appender.py                                                      #
# Look for all the files with a specific extension and append some text #
#########################################################################

# Import plugins
import os
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the Variables.ini file

# Define variables
fa_path = config['File_appender']['fa_path']
fa_text = config['File_appender']['fa_text']
fa_file_type = config['File_appender']['fa_file_type']

def get_files():
    global files
    files = []

    for r, d, f in os.walk(fa_path):   # Get all the files recursively in the 'fa_path' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if fa_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'

get_files() # Get all the files in 'append_path'
for i in files: # Append the text in 'append_text' to all the files in the 'append_path'
    file1 = open(i, "a")    # append mode 
    file1.write(fa_text) 
    file1.close()
    print(i)