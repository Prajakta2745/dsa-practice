class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 #initialize left pointer at index 1

        for r in range(1, len(nums)): #iterate r pointer from index 1 to end of array
            if nums[r] != nums[r - 1]:  #if current r pointer value is not equal to previous value
                nums[l] = nums[r]  #assign current r pointer value to l pointer index
                l += 1  # increment l pointer
        return l   #return modified lenght of array without duplicates S
