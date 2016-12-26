# pylint: disable=C0111, W1401, C0301

from components.Redditscraping import Redditscraping
from components.Reddit import Reddit

# accessing the reddit class and gathering the front page sub names
REDDIT = Reddit()
CORE_SUBS = REDDIT.gather_frontpage_sub_gathering()

CORE = Redditscraping(CORE_SUBS, "E:/projects/imgurDumps/core/", 100)
CORE.gather_images()

#Cute gathering
CUTE = Redditscraping(["aww", "animalssmiling", "catpics", "cats", "cute", "Daww", "ferrets", "Hedgehogs", "PuppySmiles", "AnimalsBeingDerps", "CuteCritters", "hardcoreaww"], "E:/projects/imgurDumps/cute/", 100)
CUTE.gather_images()
