#################################################################
# Search and replace.py                                         #
# Looks for the old_string and replace it with the new_string   #
#################################################################

# Import and configure all plugins
import os, configparser, sys
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
notebook_dir = ini_file['Globals']['noteboook_dir']     # The directory to use with search and replace
file_type = ini_file['Globals']['file_type']            # The file type to use with search and replace 
sar_old_string = ini_file['Other']['sar_old_string']    # The string that will be replaced by sar_new_string when using 'Search and replace.py'
sar_new_string = ini_file['Other']['sar_new_string']    # The string that will replace the sar_old_string when using 'Search and replace.py'

mdf.search_and_replace(notebook_dir, file_type, sar_old_string, sar_new_string)
