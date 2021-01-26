import builtins


class Solution:
    def maxProfit(self, prices: list) -> int:
        prices_len = len(prices)
        profit = 0
        if prices_len < 2:
            return profit
        else:
            buy_index = 0
            sell_index = 0
            while buy_index < prices_len - 1 and sell_index < prices_len:
                while buy_index < prices_len - 2 and prices[buy_index] > prices[buy_index+1]:
                    buy_index += 1
                sell_index = buy_index + 1
                while sell_index < prices_len - 1 and prices[sell_index] < prices[sell_index+1]:
                    sell_index += 1
                if prices[sell_index] > prices[buy_index]:
                    profit += prices[sell_index] - prices[buy_index]
                buy_index = sell_index + 1
            return profit


if __name__ == "__main__":
    test_prices = [1,2,3,4,5,6,7]
    test_prices.reverse()
    test_sol = Solution()
    profit = test_sol.maxProfit(test_prices)
    print(profit)
