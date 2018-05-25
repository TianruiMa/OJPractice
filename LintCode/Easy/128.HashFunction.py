class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        if key is None or len(key) == 0:
            return 0
        hash_value = 0

        for k in key:
            hash_value = (hash_value * 33 + ord(k)) % HASH_SIZE
        return hash_value % HASH_SIZE
