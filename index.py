# pylint: disable=C0111, W1401, C0301

#default imports
from configparser import ConfigParser

#custom imports
from components.Redditscraping import Redditscraping
from components.Reddit import Reddit



#Importing settings
CONFIG = ConfigParser()

# parse existing file
CONFIG.read('./settings.ini')

# read values from a section
IMAGE_PATH = CONFIG.get('settings', 'images_path')
IMAGE_LIMIT = CONFIG.getint('settings', 'image_limit')
CUTE_REDDITS = str(CONFIG.get("settings", "cute_reddits")).replace(" ", "").split(",")

# accessing the reddit class and gathering the front page sub names
REDDIT = Reddit()
CORE_SUBS = REDDIT.gather_frontpage_sub_gathering()

CORE = Redditscraping(CORE_SUBS, (IMAGE_PATH + "/core/"), IMAGE_LIMIT)
CORE.gather_images()

#Cute gathering
CUTE = Redditscraping(CUTE_REDDITS, (IMAGE_PATH + "/cute/"), IMAGE_LIMIT)
CUTE.gather_images()
