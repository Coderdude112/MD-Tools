#########################################################################
# File appender.py                                                      #
# Look for all the files with a specific extension and append some text #
#########################################################################

# Import and configure all plugins
import os, configparser, sys
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
notebook_dir = ini_file['Globals']['notebook_dir']  # The directory to use with file appender
file_type = ini_file['Globals']['file_type']        # The file type to use with file appender
fa_text = ini_file['Other']['fa_text']              # The text to append when using 'File appender.py'

for i in mdf.get_files(notebook_dir, file_type):
    open(i, "a", encoding="utf-8").write(fa_text)   # Append the fa_text to all files within the array 'files'
