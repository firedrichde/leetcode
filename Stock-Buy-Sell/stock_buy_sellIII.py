import builtins


class Solution:

    def maxProfit(self, prices: list) -> int:
        min_value = -pow(10, 5)
        profit_index_transaction2_unhold = 0
        profit_index_transaction2_hold = min_value
        profit_index_transaction1_unhold = 0
        profit_index_transaction1_hold = min_value
        for price in prices:
            profit_index_transaction2_unhold = max(profit_index_transaction2_unhold,profit_index_transaction2_hold+price)
            profit_index_transaction2_hold = max(profit_index_transaction2_hold,profit_index_transaction1_unhold-price)
            profit_index_transaction1_unhold = max(profit_index_transaction1_unhold, profit_index_transaction1_hold+price)
            profit_index_transaction1_hold = max(profit_index_transaction1_hold, -price)
        return profit_index_transaction2_unhold


if __name__ == "__main__":
    test_prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    # test_prices.reverse()
    test_sol = Solution()
    profit = test_sol.maxProfit(test_prices)
    print(profit)
