#####################################################################
# Broken link finder.py                                             #
# Find links within the 'blf_path' and make sure all the links work #
#####################################################################

# Import and configure all plugins
import os, re
from win10toast import ToastNotifier
n = ToastNotifier()
import configparser
config = configparser.ConfigParser()
config.read(os.getcwd() + "\\Auto tools\\variables.ini")    # Read the variables.ini files

# Define all variables, arrays, ect
alert_file = config['Global']['alert_file']
blf_path = config['Broken_link_finder']['blf_path']
blf_file_type = config['Broken_link_finder']['blf_file_type']
files = []                      # A list of all the files in blf_path
current_file = None             # The current file we are looking at
current_file_contence = None    # The contence of current_file
current_link = None             # The link we are currently testing
raw_links = []                  # An array with all the links in current_file_contence with '](' in the begining and ')' on the end
polished_links = []             # An array with the same links as raw_links but without the '](' and ')'
need_to_alert = False           # Do we need to alert the user of something

def get_files():
    global files

    for r, d, f in os.walk(blf_path): # Get all the files recursively in blf_path (r=root, d=directories, f = files)
        for file in f:  # Just get the filenames
            if blf_file_type in file:   # Filter out files that don't match the extention
                files.append(os.path.join(r, file)) # Add the files to the array 'files'
def test_link():
    if './' in current_link or 'http' in current_link or '.com' in current_link:    # The link is reletive or is an internet link
        return
    elif os.path.isfile(current_link) == True:  # The link is working
        return
    else:   # The link must be broken
        global need_to_alert

        need_to_alert = True
        open(alert_file, "a").write("The file **[" + os.path.basename(current_file) + "](" + current_file + ")** has a [broken link](" + current_link + ").\n")

get_files() # Get all the files in blf_path
for i in files:
    current_file = i
    current_file_contence = open(i).read()

    if '](' in current_file_contence:   # There is at least one link in current_file_contence
        raw_links = []  # Reset this array to prevent errors
        polished_links = [] # Reset this array to prevent errors

        raw_links = re.findall(r']\(.*?\)', current_file_contence)  # Use the regex to find all the links in current_file_contence and add them to the array raw_links
        for i in raw_links: # Polish the links by removing '](' from the begining and ')' from the end
            polished_links.append(i.lstrip('](').rstrip(')'))

        for i in polished_links:    # Test each of the polished links
            current_link = i

            test_link()

if need_to_alert == True:   # We found at least one broken link and need to alert the user
    n.show_toast("Broken Link", "At least one broken link has been found.\nCheck the ALERT file", icon_path=os.getcwd() + "\\Auto tools\\Alert.ico", duration=10)
    open(alert_file, "a").write("\n")