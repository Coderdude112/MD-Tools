#####################################################################
# Unused image deleter.py                                           #
# Finds images that are in the image_folder but not in any notes    #
#####################################################################

# Import and configure all plugins
import os, configparser, sys
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
image_dir = ini_file['Globals']['image_dir']    # The directory where all images used in the markdown notebook are stored
uif_path = ini_file['Globals']['notebook_dir']  # The base directory of the notebook
file_type = ini_file['Globals']['file_type']    # The file extension of the files that make-up the notebook (This is usually .md for markdown notebooks)
alert_file = ini_file['Globals']['alert_file']  # The file to use when making detailed alerts to the user
images = [] # An array with all the files in image_dir regaurdless of their extention


images = mdf.get_files(image_dir, '')  # An array with all the files in image_dir regaurdless of their extention

for i in mdf.get_files(uif_path, file_type):
    current_file_contence = open(i, encoding="utf-8").read()

    for j in images:
        if os.path.basename(j) in current_file_contence:
            images.remove(j)    # The image is used at least once, so remove it from the images array

if len(images) != 0:   # If the length of images is not zero (There are unused images)
    for i in images:    # Make a note in the alert_file for all the left over images that aren't used
        open(alert_file, "a", encoding="utf-8").write("The image **[" + os.path.basename(i) + "](" + i + ")** is unused.\n")
    
    open(alert_file, "a", encoding='utf-8').write("\n") # Add a MD normal spacing line to the alert_file
    mdf.toast_alert('Unused image')
