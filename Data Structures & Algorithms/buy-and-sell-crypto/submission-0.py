class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Appraoch 1: Brute Force: Calc profit e.g. buy day 1 and then iterate thorugh rest of array to calc the potential profit, take the max there. approx. less than O(n2)
        # Approach 2: 2 Pointers both start from beginning, if pointer B is lower than pointer A, B becomes A. If A is higher than B, the pointer stays. 
        left, right = 0, 1
        max_profit = 0
        while left < right:
            if right == len(prices):
                break
            buy_price = prices[left]
            sell_price = prices[right]
            if sell_price < buy_price:
                left = right
                right += 1
                continue
            if buy_price < sell_price:
                profit = sell_price - buy_price
                max_profit = max(profit, max_profit)
            right += 1
        return max_profit



        