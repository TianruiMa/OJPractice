import random


class Codec:

    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.hash_map = dict()
        self.random_seed = random.random()
        self.key = None
        self.short_url_prefix = "http://tinyurl.com/"

    def get_rand_key(self):
        new_str = ""
        for i in range(0, 6):
            new_str += self.alphabet[random.randint(0, 61)]
        return new_str

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        print "okok"
        while self.key in self.hash_map:
            self.key = self.get_rand_key()
        self.hash_map[self.key] = longUrl
        return self.short_url_prefix + self.key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        print "not"
        print "n"
        return self.hash_map[shortUrl[-6:]]


codec = Codec()
print codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))