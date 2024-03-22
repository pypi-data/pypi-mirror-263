import pkg_resources
import xmlrpc.client
import socket
import os


# Function to check internet connection
def is_connected():
    try:
        # Connect to PyPI server to check internet connection
        socket.create_connection(("pypi.org", 443), timeout=1)
        return True
    except OSError:
        pass
    return False

def print_release_notes():
    """
    Print release notes for the latest version of the package.
    """
    release_notes_file = os.path.join(os.path.dirname(__file__), 'release.txt')
    if os.path.exists(release_notes_file):
        with open(release_notes_file, 'r') as file:
            release_notes = file.read()
            print("Release Notes:")
            print(release_notes)
    else:
        print("Release notes not found.")


# Check for internet connection

# Import your functions here        
from .ascii import print_ascii, ascii_art, ascii_art_colored, print_ascii_colored
from .print_additions import (
    nice_print, print_warning, print_colored, print_debug, print_header,
    print_bold, print_danger, print_green, print_info, print_italic,
    print_red, print_strikethrough, print_success, print_system, print_underline
)
from .id import generateId, generateTextId, splitStringAt50Percent
from .jsonify import (
    addJson, backupJson, createJson, deleteJson, deleteJsonData,
    editJson, loadJsonData, overwriteJson, sortJsonFile,
    validateJson, renameJson,readJson
)
from .additional_functions import (
    camel_to_snake, deep_copy, factorial, flatten_list, is_prime,
    is_valid_date, is_valid_email, log_error, log_info, log_warning,
    merge_dicts, read_csv, remove_whitespace, retry_func, reverse_list,
    timer, write_to_file, unique_elements, truncate_string
)
from .files import (
    addFile,backupFile,createFile,deleteDataFromFile,deleteFile,editFile,
    loadDataFromFile,overwriteFile,readFile,renameFile,sortFile,validateFile
)
from .profanities import(has_profanity)
from .youtube import downloadYoutube
if is_connected():
    def get_latest_version(package_name):
        """Get the latest version of a package from PyPI."""
        try:
            client = xmlrpc.client.ServerProxy('https://pypi.org/pypi')
            releases = client.package_releases(package_name)
            if releases:
                return releases[0]  # Return the latest version
            else:
                print("Package not found on PyPI.")
                return None
        except Exception as e:
            print(f"Failed to fetch latest version: {e}")
            return None

    # Check for updates when the package is imported
    latest_version = get_latest_version("kurumii")
    if latest_version:
        installed_version = pkg_resources.get_distribution(__name__).version
        if installed_version and latest_version > installed_version:
            print_additions.print_info("A newer version is available. Please consider upgrading: `pip install --upgrade kurumii`")
            print_release_notes()
        else:
            pass

    try:
        __version__ = pkg_resources.get_distribution(__name__).version
    except pkg_resources.DistributionNotFound:
        # Package is not installed
        __version__ = None

    def check_for_updates():
        # Code to check for updates goes here
        installed_version = __version__
        # Assume get_latest_version() fetches the latest version from PyPI
        latest_version = get_latest_version("kurumii")  # You need to implement this function
        if latest_version and latest_version > installed_version:
            print_additions.print_info("A newer version is available. Please consider upgrading.")

else:
    print_additions.print_red("No internet connection or too slow connection. Skipping version check.")
