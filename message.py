from tags import Hashtag
from grammer import *
import random


class Message:


    hash_library = Hashtag(hashes)

    def __init__(self):
        hashtags = self.hash_library.get_random_tags(3)
        self.body = "{:s} {:s} {:s} {:s}".format(hashtags[0], hashtags[2], nsfw, random.choice(phrases))
