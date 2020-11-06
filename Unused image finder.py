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
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the Variables.ini file

# Set all variables
alert_file = config['Manual_variables']['alert_file']
uif_path = config['Unused_image_finder']['uif_path']
uif_file_type = config['Unused_image_finder']['uif_file_type']
uif_image_path = config['Unused_image_finder']['uif_image_path']

def get_files():
    global files
    files = []

    for r, d, f in os.walk(uif_path):   # Get all the files recursively in the 'uif_path' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if uif_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def get_images():
    global images
    images = []

    for r, d, f in os.walk(uif_image_path):   # Get all the files recursively in the 'uif_image_path' path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            images.append(file) # Add the images to the array 'images'
def unused_images_alert():
    for i in images:
        with open(alert_file, "a") as alert_file_data:   # For all the unused images
            alert_file_data.write("The image \"" + i + "\" is currently unused.\n\n")
            n.show_toast("Unused Image", "The image " + i + " is unused.\n Check the ALERT file", icon_path=os.getcwd() + "\\Auto tools\\Alert.ico", duration=10)

get_files()
get_images()

for i in files: # For all the items within the 'files' array
    with open(i) as open_file:
        file_data = open_file.read() # Read the file into the variable 'file_data'
        for image in images:
            if image in file_data:  # Check if the images are in 'file_data'
                images.remove(image)    # The image is found, so remove it

unused_images_alert()   # Alert to the unused images