# pylint: disable=W1401, C0301

import os
import re
import urllib.request
import feedparser

class Redditscraping:
    """ Class built for ripping imgur images from a reddit feed (rss) """

    def __init__(self, reddit_rooms, file_location, limit):
        self.reddit_rooms = reddit_rooms
        self.file_location = file_location
        self.limit = limit
        self.i = 1
        self.image_count = 1

        if not os.path.exists(self.file_location):
            os.makedirs(self.file_location)

    def gather_reddit_rss(self, room):
        """ will a room name and limit, while then gathering the rss food upto that limit """

        reddit_url = "https://www.reddit.com/r/" + room + "/.rss?limit=" + str(self.limit) + "&after=0"
        feed = feedparser.parse(reddit_url)
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
            print("Failed to download image: %s, error: %s" % (url, str(err)))

    def gather_images(self):
        """ goes through the provided array of rooms (sub reddits) and begin parsing and downloading any imgur links """

        for sub in self.reddit_rooms:
            current_feed = self.gather_reddit_rss(sub)
            entries_len = len(current_feed["entries"])
            index = 0

            for entry in current_feed["entries"]:
                index += 1
                imgur_url = self.parse_imgur_links(entry["summary"])
                file_name = self.file_location + "#%s.jpeg" % str(self.image_count) # self.image_count was (re.sub(r'[^\w]', '', self.image_count)
                if imgur_url != '':
                    self.image_count += 1
                    self.download_image(imgur_url, sub, file_name)
                if index >= entries_len:
                    print("Downloading Complete in subreddit: %s" % sub)
