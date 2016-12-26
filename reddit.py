# pylint: disable=C0111, W1401, C0301

from components.Redditscraping import Redditscraping

#Cute gathering
CUTE = Redditscraping(["aww", "animalssmiling", "catpics", "cats", "cute", "Daww", "ferrets", "Hedgehogs", "PuppySmiles", "AnimalsBeingDerps", "CuteCritters", "hardcoreaww"])
CUTE.gather_images("E:/projects/imgurDumps/cute/", 100)
