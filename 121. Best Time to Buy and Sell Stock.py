class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #initialize l pointer at index 0 and r pointer at index 1   l:buy ,r:sell
        maxP = 0  # initialize max profit variable

        while r < len(prices):   #iterate r pointer from index 1 to end of array
            if prices[l] < prices[r]:  #if current l pointer value is less than r pointer value
                profit = prices[r] - prices[l]  #calculate profit
                maxP = max(maxP, profit)  #update max profit if current proit is greater
            else: 
                l = r  #move l pointer to r if l is greater than or equal to r
            r += 1  #increment r pointer
        return maxP #return max profit found