#####################################################
# Functions.py                                      #
# Used so I don't repeat my functions too much lol  #
#####################################################

# Import and configure all plugins
import os, fileinput, re
from win10toast import ToastNotifier
winToast = ToastNotifier()

# Return all the files within a directory that match the file type 
# Needed variables:
# directory - The directory to get the files recursivly from
# file_type - Used to select only certin files. Use '' to select all files within the directory
def get_files(directory, file_type):
    dir_contents = []   # An array that will be filled with all the files in the directory (recursively) that also match the file_type

    for r, d, f in os.walk(directory):  # Get all the files recursively in the directory (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if file_type in file:   # Filter out files that don't match the extention
                dir_contents.append(os.path.join(r, file)) # Add the files to the array 'files'
    
    return dir_contents

# Do a search and replace for files within a directory
# Needed variables:
# directory - The directory to get the files recursivly from (For get_files)
# file_type - Used to select only certin files. Use '' to select all files within the directory (For get_files)
# old_string - The string that will be replaced
# new_string - The string that will replace the old_string
def search_and_replace(directory, file_type, old_string, new_string):
    current_file_contents = None    # The contents of the current file

    for i in get_files(directory, file_type):
        if old_string in open(i, encoding='utf-8').read():    # If the old_string is in the file
            current_file_contents = open(i, encoding="utf-8").read().replace(old_string, new_string)
            open(i, "w", encoding="utf-8").write(current_file_contents)

# Do a search, send a notification, and make a note within a file for all the files that contain a string within a directory
# Needed variables:
# directory - The directory to get the files recursivly from (For get_files)
# file_type - Used to select only certin files. Use '' to select all files within the directory (For get_files)
# string_to_find - The string to fing within the files. If this string is present then we will make a message of it in the alert_file and send a notification
# alert_file - The file to use when making a note to a user
# file_message_ID - The message ID to write to the alert_file when the string_to_find is found
# notification_message_ID - The message ID to give to the user when the string_to_find is found at least once (For alert)
def search_and_alert(directory, file_type, string_to_find, file_message_ID, alert_file, notification_message_ID):
    need_to_alert = None    # If this is True then we need to alert the user because the string_to_find was found at least once

    for i in get_files(directory, file_type):
        if string_to_find in open(i, encoding='utf-8').read():  # If the string_to_find is found within the file
            need_to_alert = True

            # Append a message to the alert_file
            if file_message_ID == 'Broken link due to deletion':
                open(alert_file, "a", encoding="utf-8").write("The file *" + os.path.basename(string_to_find) + "* was deleted. This deletion created a broken link within the file **[" + os.path.basename(i) + "](" + i + ")**.\n")
    
    if need_to_alert == True:   # We need to alert the user beacuse we found the string_to_find at least once
        open(alert_file, "a", encoding='utf-8').write("\n") # Add a MD normal spacing line to the alert_file
        toast_alert(notification_message_ID)

# Give a Windows 10 toast notification to the user
# Needed variables:
# notification_message_ID - The message ID to give to the user
def toast_alert(notification_message_ID):
    if notification_message_ID == 'Broken link due to deletion':
        winToast.show_toast("Broken Link", "Due to a file deletion, a broken link has been created.\nCheck the ALERT file", icon_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\Alert.ico", duration=10)
    elif notification_message_ID == 'Broken link found':
        winToast.show_toast("Broken Link", "At least one broken link has been found.\nCheck the ALERT file", icon_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\Alert.ico", duration=10)
    elif notification_message_ID == 'Unused image':
        winToast.show_toast("Unused Image", "At least one unused image has been found.\nCheck the ALERT file", icon_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\Alert.ico", duration=10)
