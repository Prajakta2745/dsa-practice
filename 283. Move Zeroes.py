class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 #set left ponter to 0 index
        for r in range(len(nums)): #iterate r pointer through the array
            if nums[r]: #if r pointer is not zero
                nums[l], nums[r] = nums[r], nums[l] #swap values at l and r pointer
                l += 1 #increment l pointer
        return nums # return modified array
             
        