from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # secret_dict, guess_dict = defaultdict(int), defaultdict(int)
        # bull, cow = 0, 0
        #
        # for index in range(len(guess)):
        #     if secret[index] == guess[index]:
        #         bull += 1
        #         continue
        #
        #     if guess_dict[secret[index]] > 0:
        #         cow += 1
        #         guess_dict[secret[index]] -= 1
        #     else:
        #         secret_dict[secret[index]] += 1
        #
        #     if secret_dict[guess[index]] > 0:
        #         cow += 1
        #         secret_dict[guess[index]] -= 1
        #     else:
        #         guess_dict[guess[index]] += 1
        # return ("%dA%dB" % (bull, cow))


        bulls, cows = 0, 0
        for s,g in zip(secret, guess):
            if s == g:
                bulls += 1
        tot = sum(min(secret.count(digit),guess.count(digit)) for digit in '0123456789')
        res = str(bulls) + 'A' + str(tot - bulls) + 'B'
        return res