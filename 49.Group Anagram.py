from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)  # to store grouped anagram
        for s in strs: # iterate through each string
            count = [0] * 26 # 
            for c in s: #count frequency of each char
                count[ord(c) - ord('a')] += 1  #increment count for char

            key = tuple(count)  #use tuple of count as key
            anagrams_dict[key].append(s)  #append string to correspondig anagram group

        return list(anagrams_dict.values())  #return grouped anagrams as list of list
