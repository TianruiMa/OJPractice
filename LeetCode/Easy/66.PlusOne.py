class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carry = 0

        for i, d in enumerate(digits[::-1]):
            if i != 0 and carry == 0:
                return digits
            digits[len(digits) - 1 - i] = (d + 1) % 10
            carry = (d + 1) / 10

        if carry != 0:
            digits.insert(0, 1)
        return digits