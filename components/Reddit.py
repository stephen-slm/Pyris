# pylint: disable=W1401, C0301

import re
import feedparser

class Reddit:
    """ A basic reddit class to do some information gathering """

    def __init__(self):
        self.reddit_core_url = "https://www.reddit.com/"

    def gather_frontpage_sub_gathering(self):
        """ Gather all the front page reddit sub reddits names """
        reddit_subs_core = []
        reddit_rss_feed = feedparser.parse(self.reddit_core_url + ".rss?limit=100")
        for entry in reddit_rss_feed["entries"]:
            entry_sub = re.search("(?P<url>https?://www.reddit.com/r/([A-z0-9\-]+))(\?[[^/]+)?", entry["summary"])
            reddit_subs_core.append(entry_sub.group(2))
        return reddit_subs_core
