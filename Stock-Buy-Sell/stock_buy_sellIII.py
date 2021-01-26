import builtins


class Solution:
    def __init__(self) -> None:
        self.valuesaved = dict()

    def maxProfit(self, prices: list) -> int:
        prices_len = len(prices)
        profit = 0
        if prices_len < 2:
            return profit
        else:
            profit = self.maxProfit0(prices, 0, 4, False)
            return profit

    def maxProfit0(self, prices: list, index: int, count: int, canSell: bool) -> int:
        if index >= len(prices) or count == 0:
            return 0
        else:
            if (index, count, canSell) in self.valuesaved:
                return self.valuesaved[(index, count, canSell)]
            else:
                # while index < len(prices)-1:
                #     if canSell and prices[index+1] > prices[index]:
                #         index += 1
                #     elif not canSell and prices[index+1] < prices[index]:
                #         index += 1
                #     else:
                #         break
                transtraction = self.maxProfit0(
                    prices, index, count-1, not canSell) + (prices[index] if canSell else -prices[index])

                skip = self.maxProfit0(prices, index+1, count, canSell)
                self.valuesaved[(index, count, canSell)] = max(
                    transtraction, skip)
                return self.valuesaved[(index, count, canSell)]


if __name__ == "__main__":
    test_prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    # test_prices.reverse()
    test_sol = Solution()
    profit = test_sol.maxProfit(test_prices)
    print(profit)
