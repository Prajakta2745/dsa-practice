class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O( n log n ) to sort the array
        n = len(nums)  # O(n) to get lenght of the array
        for i in range(1, n):  #loop through the array O(n)
            if nums[i] == nums[i-1]:  # check if current element is equal to previous element O(1)
                return True  #if duplicate found

        return False #if no duplicate found

