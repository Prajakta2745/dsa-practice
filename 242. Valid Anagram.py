class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s) # sort charachter in string s
        sorted_t = sorted(t)  #sort charachter in string t
        return sorted_s == sorted_t #compare both sorted strings
        