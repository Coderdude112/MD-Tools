#########################################################################
# Broken link finder.py                                                 #
# Find links within the 'notebook_dir' and make sure all the links work #
#########################################################################

# Import and configure all plugins
import os, os.path, re, configparser, sys
ini_file = configparser.ConfigParser()

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # Add the parent directory to the PATH so we can import our functions
import Functions as mdf # Import all functions within Functions.py as mdf

# Define all variables, arrays, ect
ini_file.read(os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\\variables.ini") # Read the variables.ini file up one directory
notebook_dir = ini_file['Globals']['notebook_dir']  # The directory to use with broken link finder
file_type = ini_file['Globals']['file_type']        # The file type to use with broken link finder
alert_file = ini_file['Globals']['alert_file']      # The file to use when making a note to a user
raw_links = []          # An array with all the links in current_file_contence with '](' in the begining and ')' on the end
polished_links = []     # An array with the same links as raw_links but without the '](' and ')'
need_to_alert = False   # Do we need to alert the user of something

for i in mdf.get_files(notebook_dir, file_type):
    if '](' in open(i, encoding="utf-8").read():    # If the file has any links in it
        raw_links = re.findall(r']\(.*\)\s', open(i, encoding="utf-8").read())   # Use the regex to find all the links in i and add them to the array raw_links

        for j in raw_links: # Polish all the links
            if './' not in j or 'http' not in j:    # The link is not a reletive or an internet link
                polished_links.append(j.strip().lstrip('](').rstrip(')'))
        for j in polished_links:    # Test the polished links
            if os.path.exists(j) == False:  # The link is broken so we will add an alert to the alert_file
                need_to_alert = True

                open(alert_file, "a", encoding="utf-8").write("The file **[" + os.path.basename(i) + "](" + i + ")** has a broken link pointing to `" + j + "`.\n")

if need_to_alert == True:
    open(alert_file, "a", encoding='utf-8').write("\n") # Add a MD normal spacing line to the alert_file
    mdf.toast_alert('Broken link found')
