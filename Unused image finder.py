#####################################################################
# Unused image deleter.py                                           #
# Finds images that are in the image_folder but not in any notes    #
#####################################################################

# Import and configure all plugins
import os
from win10toast import ToastNotifier
n = ToastNotifier()
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the variables.ini file

# Define all variables, arrays, ect
alert_file = config['Global']['alert_file']
uif_path = config['Unused_image_finder']['uif_path']
uif_file_type = config['Unused_image_finder']['uif_file_type']
uif_image_path = config['Unused_image_finder']['uif_image_path']
files = []              # An array with all the files in uif_path
images = []             # An array with all the files in uif_image_path regaurdless of their extention
need_to_alert = False   # Do we need to alert the user of something

def get_files():
    global files

    for r, d, f in os.walk(uif_path): # Get all the files recursively in the uif_path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if uif_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def get_images():
    global images

    for r, d, f in os.walk(uif_image_path):   # Get all the files recursively in the 'uif_image_path' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            images.append(file) # Add the images to the array 'images'

get_files()
get_images()

for i in files: # For all the items within the files array
    current_file_contence = open(i).read
    for j in images:    # For all the items in the array images
        if j in current_file_contence:
            images.remove(j)    # The image is used at least once, so remove it from the images array

for i in images:    # Add a notice in the alert_file for all the unused images left in images
    global need_to_alert

    need_to_alert = True
    open(alert_file, "a").write("The image \"" + i + "\" is currently unused.\n")

if need_to_alert == True:
    n.show_toast("Unused Image", "At least one unused image has been found.\nCheck the ALERT file", icon_path=os.getcwd() + "\\Auto tools\\Alert.ico", duration=10)
    open(alert_file, "a").write("\n")
