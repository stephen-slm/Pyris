# pylint: disable=W1401, C0301

import re
import urllib.request
import feedparser

class Redditscraping:
    'Class built for ripping imgur images from a reddit feed (rss)'

    def __init__(self, reddit_rooms):
        self.reddit_rooms = reddit_rooms
        self.i = 1
        self.image_count = 0

    def gather_reddit_rss(self, room, limit):
        """ will a room name and limit, while then gathering the rss food upto that limit """

        reddit_url = "https://www.reddit.com/r/" + room + "/.rss?limit=" + str(limit) + "&after=0"
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

    def gather_images(self, folderpath, limit):
        """ goes through the provided array of rooms (sub reddits) and begin parsing and downloading any imgur links """

        for sub in self.reddit_rooms:
            current_feed = self.gather_reddit_rss(sub, limit)
            entries_len = len(current_feed["entries"])
            index = 0

            for entry in current_feed["entries"]:
                index += 1
                imgur_url = self.parse_imgur_links(entry["summary"])
                file_name = folderpath + (re.sub(r'[^\w]', '', entry['title']) + ".jpeg")
                if imgur_url != '':
                    self.image_count += 1
                    self.download_image(imgur_url, sub, file_name)
                if index >= entries_len:
                    print("Downloading Complete")
