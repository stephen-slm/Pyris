# pylint: disable=W1401, C0301

import re
from feedparser import parse as feedparser

class Reddit:
    """ A basic reddit class to do some information gathering """

    def __init__(self):
        self.reddit_core_url = "https://www.reddit.com/"
        self.frontpage = self.gather_frontpage()

    def gather_frontpage(self):
        """ Gather all the front page reddit sub reddits names """
        subreddits = []
        reddit_rss_feed = feedparser(self.reddit_core_url + ".rss?limit=100")
        for entry in reddit_rss_feed["entries"]:
            entry_sub = re.search("(?P<url>https?://www.reddit.com/r/([A-z0-9\-]+))(\?[[^/]+)?", entry["summary"])
            if entry_sub.group(2) not in subreddits:
                subreddits.append(entry_sub.group(2))
        return subreddits
