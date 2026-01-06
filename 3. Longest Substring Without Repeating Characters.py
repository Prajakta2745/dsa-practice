class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #to store unique char
        l = 0 #left pointer
        res = 0  #result var to store max len

        for r in range(len(s)):  # right pointer
            while s[r] in charSet:  #if char already in set move left pointer
                charSet.remove(s[l])  #remove char at leftpointer
                l += 1  #move left pointer to right
            charSet.add(s[r])  #add char at right pointer to set
            res = max(res, r - l + 1)  #update result with max len found
        return res   #return the result