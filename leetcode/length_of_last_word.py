class Solution:
    """ O(n) """
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        space = 0
        for i in s:
            # if symbol is space -> count space and continue
            if i == ' ':
                space += 1
                continue
            # if next the space has another word -> drop count and count word letters again
            if i != ' ' and space != 0:
                count = 0
                space = 0
            count += 1
        return count

    




a = Solution()
print(a.lengthOfLastWord('luffy is still joyboy           a'))