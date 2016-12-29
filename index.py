# pylint: disable=C0111, W1401, C0301

# default imports]
from os import path, makedirs
from configparser import ConfigParser

# custom imports
from components.Reddit import Reddit
from components.RedditClient import RedditClient
from components.Redditscraping import Redditscraping

# Importing settings
CONFIG = ConfigParser()

# parse existing file
CONFIG.read('./settings.ini')

# read values from a section

# settings
IMAGE_PATH = CONFIG.get('settings', 'images_path')
IMAGE_LIMIT = CONFIG.getint('settings', 'image_limit')

# options
BUILD_CORE = CONFIG.getboolean("options", "build_core")
NAME_TYPE = CONFIG.get("options", "name_type")
PAGE_TYPE = CONFIG.get("options", "page_type")

# scraping_options
FOLDER_NAMES = str(CONFIG.get("scraping_options", "folder_names")).replace(" ", "").split(",")

# check if IMAGE_PATH end folder exists (otherwise create it)
if not path.exists(IMAGE_PATH):
    makedirs(IMAGE_PATH)

# accessing the reddit class and gathering the front page sub names
if BUILD_CORE:
    REDDIT = Reddit()
    CORE = Redditscraping(RedditClient(REDDIT.frontpage, (IMAGE_PATH + "/core/"), IMAGE_LIMIT, NAME_TYPE, PAGE_TYPE))
    CORE.gather_images()

# scraping
for name in FOLDER_NAMES:
    try:
        selected_subreddits = str(CONFIG.get("scraping_options", name)).replace(" ", "").split(",")
        scraping = Redditscraping(RedditClient(selected_subreddits, (IMAGE_PATH + "/%s/" % name), IMAGE_LIMIT, NAME_TYPE, PAGE_TYPE))
        scraping.gather_images()
    except Exception as error:
        if type(error).__name__ == "NoOptionError":
            print("folder_name: ''{}'' did not have any provided subreddits - code: 01".format(name))


# I would suggest using the aiohttp library for downloading the images. It is asynchronous so it can download multiple files at the same time.