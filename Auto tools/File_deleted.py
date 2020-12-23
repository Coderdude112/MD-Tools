#################################################################################
# File_deleted.py                                                               #
# Run by Link_helper.py to determine weather a file was deleted or moved dirs   #
#################################################################################

# Import and configure all plugins
import time, os, configparser, sys
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

time.sleep(1)   # Wait a second to let Link_helper.py update variables.ini if it needs to

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
deleted = ini_file['Auto_tools_variables-do_NOT_edit']['deleted']   # If this is "yes" then a file was deleted. If this is "no" then a file was moved dirs
notebook_dir = ini_file['Globals']['notebook_dir']                  # The base directory of the notebook
file_type = ini_file['Globals']['file_type']                        # The file extension of the files that make-up the notebook (This is usually .md for markdown notebooks)
old_link = ini_file['Auto_tools_variables-do_NOT_edit']['old_link'] # The old link that will be replaced by the new_link
new_link = ini_file['Auto_tools_variables-do_NOT_edit']['new_link'] # The new link that will replace the old_link
alert_file = ini_file['Globals']['alert_file']                      # The file to use when making detailed alerts to the user

if deleted == "no": # The file was moved, not deleted
    mdf.search_and_replace(notebook_dir, file_type, old_link, new_link)
elif deleted == "yes":  # The file was deleted, not moved
    mdf.search_and_alert(notebook_dir, file_type, old_link, 'Broken link due to deletion', alert_file, 'Broken link due to deletion')
