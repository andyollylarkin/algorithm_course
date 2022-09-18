class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [x for x in a[::-1]]
        b = [x for x in b[::-1]]
        len_longest = len(a if len(a) > len(b) else b)
        res = ''
        i = 0
        carry = False
        while i < len_longest or carry:
            a_val = a[i] if i <= len(a) - 1 else '0'
            b_val = b[i] if i <= len(b) - 1 else '0'
            val = int(a_val) + int(b_val)
            if carry:
                val += 1
                carry = False
            if val > 1:
                val -= 2
                carry = True
            res = res + str(val)
            i += 1
        return res[::-1]



sol = Solution()
sol.addBinary('1010', '1011')