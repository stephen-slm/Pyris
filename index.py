# pylint: disable=C0111, W1401, C0301

#default imports
from configparser import ConfigParser

#custom imports
from components.Reddit import Reddit
from components.Redditscraping import Redditscraping

#Importing settings
CONFIG = ConfigParser()

# parse existing file
CONFIG.read('./settings.ini')

# read values from a section

#settings
IMAGE_PATH = CONFIG.get('settings', 'images_path')
IMAGE_LIMIT = CONFIG.getint('settings', 'image_limit')
CUTE_REDDITS = str(CONFIG.get("settings", "cute_reddits")).replace(" ", "").split(",")

#options
BUILD_CORE = CONFIG.getboolean("options", "build_core")
NAMES_TYPE = CONFIG.getboolean("options", "names_type")

# accessing the reddit class and gathering the front page sub names
if BUILD_CORE:
    REDDIT = Reddit()
    CORE = Redditscraping(REDDIT.frontpage, (IMAGE_PATH + "/core/"), IMAGE_LIMIT, NAMES_TYPE)
    CORE.gather_images()

#Cute gathering
CUTE = Redditscraping(CUTE_REDDITS, (IMAGE_PATH + "/cute/"), IMAGE_LIMIT, NAMES_TYPE)
CUTE.gather_images()
