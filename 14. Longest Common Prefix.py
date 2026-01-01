class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""   #initiaize result string

        for i in range(len(strs[0])):  #loop thriught each character of first string
            for s in strs:  #loop throught each string in the array
                if i == len(s) or s[i] != strs[0][i]:  #check if index exceeds lenght of current  stringof charater orcurrent charater is not equal to find
                    return res # return result if mismatch found
            res += strs[0][i]  #append current charachter to result if all string have same charachter at current index

        return res  #return result after completing all charaters of first string
