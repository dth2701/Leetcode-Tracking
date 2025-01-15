class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a : 3
        # n : 1
        # g : 2
        # r : 1
        if len(s) != len(t):
            return False

        dictS, dictT = {}, {}
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        # for letter in s:
        #     if dictS.get(letter) !=  dictT.get(letter):
        #         return False
        return dictS == dictT