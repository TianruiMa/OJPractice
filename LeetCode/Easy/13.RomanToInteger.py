class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        levels = [1000, 500, 100, 50, 10, 5, 1]
        int_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        roman = ""
        l = 0
        while l < len(levels):
            print("value", levels[l])
            if num == 0:
                return roman
            elif num >= levels[l]:
                print("find perfect")
                roman += int_dict[levels[l]]
                num -= levels[l]
            else:
                for d in levels[l+1:][::-1]:
                    print("d",d)
                    if num >= levels[l] - d:
                        roman += int_dict[d] + int_dict[levels[l]]
                        num -= (levels[l] - d)
                        break
                l += 1

        return roman

a = 4
print(Solution().intToRoman(a))