# pylint: disable=W1401, C0301

class RedditClient:
    """ A basic reddit class to do some information gathering """

    def __init__(self, rooms, location, limit, room_type, page_type):
        self.rooms = rooms
        self.location = location
        self.limit = limit
        self.type = room_type
        self.page_type = page_type
        self.max_random_numbers = (limit * len(rooms) * 10)
