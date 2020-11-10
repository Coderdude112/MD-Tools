#########################################################################
# File appender.py                                                      #
# Look for all the files with a specific extension and append some text #
#########################################################################

# Import and configure all plugins
import os
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the variables.ini file

# Define all variables, arrays, ect
fa_path = config['File_appender']['fa_path']
fa_text = config['File_appender']['fa_text']
fa_file_type = config['File_appender']['fa_file_type']
files = []                  # An array with all the files in fa_path
current_file_content = None # The contence of the current file opened in append mode

def get_files():
    global files

    for r, d, f in os.walk(fa_path): # Get all the files recursively in the path_to_search (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if fa_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'

get_files() # Get all the files in fa_path
for i in files: # Append the text in fa_text to all the files in the fa_path
    open(i, "a").write(fa_text)
