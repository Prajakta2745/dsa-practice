class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] # initialize 1st value to maxsub
        
        curSum = 0
        for n in nums: # go through each number 
            if curSum < 0: #find negative value
                curSum = 0 # set negative value as a 0

            curSum += n #Adding current number to 0 position
            maxSub = max(maxSub, curSum) #update the maxsubarray
        return maxSub