# PyRedditImgurScraping


PyRedditImgurScraping is a Python (3) tool to scrape [Reddit](https://www.reddit.com/) subreddits.
This tool enables you to pull [Imgur](http://imgur.com/) images that are within the 
selected reddit subreddits and download them into your selected folder

## Settings.ini

### *Settings*

[image_path](): The direct path to the location you want to save your images.

[image_limit](): The max amount of images to download per subreddit (max 100, default: 50).

### *Options*

[build_core](): If true, this will tell the tool to scrape the frontpage (reddit) 
for the current most active subreddits and then scrape all the Imgur links directly 
from them subreddits.

[name_type](): If changed to one of three options (random, standard, name), will 
affect the image name. (random: random number, standard: number counting system, 
name: the downloaded image name).

### *Scraping_options*

[folder_names](): This will be the folder name of which the images will be pulled into, 
you then will have to create a duplicate of that name below the folder_names. Giving that value all
the subreddits you want to scrape. These values should be single space while seperated by a single comma.
Check the below example for a better understanding.

### *Example*
```ini
[settings]
images_path = %userprofile%\Pictures
image_limit = 50

[options]
build_core = false
name_type = standard

[scraping_options]
folder_names = cute, awesomeSubReddits
cute = aww, animalssmiling, catpics, cats
awesomeSubReddits = AskReddit, MuseumOfReddit, AccidentalComedy
```
## License

&copy; 2016 Stephen Lineker-Miller <smmstephenmiller@gmail.com>

This is free software. It is licensed under the [MIT License](http://opensource.org/licenses/MIT). Feel free to use this in your own work. However, if you modify and/or redistribute it, please attribute me in some way, and distribute your work under this or a similar license. A shout-out or a beer would be appreciated.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=MYR4398RVSV68)