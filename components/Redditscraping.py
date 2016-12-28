# pylint: disable=W1401, C0301

import re
import urllib.request
from os import path, makedirs
from random import randint
from feedparser import parse as feedparser

ENTRIES_NAME = "entries"
SUMMARY_NAME = "summary"
TITLE_NAME = "title"

class Redditscraping:
    """ Class built for ripping imgur images from a reddit feed (rss) """

    def __init__(self, client):
        self.client = client
        self.i = 1
        self.image_count = 1

        if self.client.type not in ['random', 'standard', 'name']:
            self.client.type = "standard"

        if not path.exists(self.client.location):
            makedirs(self.client.location)

    def handle_errors(self, error_code, error, extra):
        """ handles errors that occure while scraping Reddit """

        if error_code == 1:
            print("Failed to download image: %s, error: %s" % (extra, str(error)))

    def gather_reddit_rss(self, room):
        """ will a room name and limit, while then gathering the rss food upto that limit """

        reddit_url = "https://www.reddit.com/r/" + room + "/.rss?limit=" + str(self.client.limit) + "&after=0"
        feed = feedparser(reddit_url)
        return feed

    def parse_imgur_links(self, entry_summary):
        """ This will take in the reddit entry summary, parsing out the imgur links out of the summary text """

        if re.search("(?P<url>https?://imgur.com/([A-z0-9\-]+))(\?[[^/]+)?", entry_summary):
            imgururl = re.search("(?P<url>https?://imgur.com/([A-z0-9\-]+))(\?[[^/]+)?", entry_summary)
            imgururl = "http://i." + imgururl.group(0)[7:] + ".jpeg"
            return imgururl
        elif re.search("(?P<url>https?://i.imgur.com/([A-z0-9\-]+))(\?[[^/]+)?", entry_summary):
            imgururl = re.search("(?P<url>https?://i.imgur.com/([A-z0-9\-]+))(\?[[^/]+)?", entry_summary)
            return imgururl.group(0) + ".jpeg"
        else:
            return ''

    def download_image(self, url, room, name):
        """ This will take in the url, room and name, downloading the image from the url while also printing this to the command line, stating the room and name """

        print("Downloading image room: r/%s, %s/%s" % (room, str(self.i), str(self.image_count)))
        try:
            urllib.request.urlretrieve(url, name)
            self.i += 1
        except (urllib.request.HTTPError, Exception) as err:
            self.handle_errors(1, err, url)

    def gather_images(self):
        """ goes through the provided array of rooms (sub reddits) and begin parsing and downloading any imgur links """

        for sub in self.client.rooms:
            current_feed = self.gather_reddit_rss(sub)
            entries_len = len(current_feed[ENTRIES_NAME])
            index = 0
            random_numbers = []

            for entry in current_feed[ENTRIES_NAME]:
                index += 1
                imgur_url = self.parse_imgur_links(entry[SUMMARY_NAME])
                image_title = re.sub('[^A-Za-z0-9 ]+', '', str(entry[TITLE_NAME]))

                #random, name and standard are options that are pulled and transfered from the settings.ini file (will affect the naming of the files)
                if self.client.type == "random":
                    selected_number = randint(0, self.client.max_random_numbers)

                    while selected_number in random_numbers:
                        selected_number = randint(0, self.client.max_random_numbers)

                    random_numbers.append(selected_number)
                    file_name = self.client.location + "%s.jpeg" % str(selected_number)

                if self.client.type == "name":
                    file_name = self.client.location + "%s.jpeg" % str(image_title)

                if self.client.type == "standard":
                    file_name = self.client.location + "#%s.jpeg" % str(self.image_count)

                if imgur_url != '':
                    self.image_count += 1
                    self.download_image(imgur_url, sub, file_name)
                if index >= entries_len:
                    print("Downloading Complete in subreddit: %s" % sub)

        return True
