"""
Used to access the data files.
"""

import pkg_resources

import emojifier.data

DATA_DIRECTORY_NAME = emojifier.data.__name__
PATH_TO_COMMENTS_FILE = pkg_resources.resource_filename(DATA_DIRECTORY_NAME, "emojipasta-comments.txt")
PATH_TO_MAPPINGS_FILE = pkg_resources.resource_filename(DATA_DIRECTORY_NAME, "emoji-mappings.json")
