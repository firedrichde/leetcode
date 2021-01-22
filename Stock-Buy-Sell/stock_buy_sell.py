from functools import total_ordering


class Solution:
    def __init__(self) -> None:
        self.profit = list()
        self.count = 0

    def maxProfit(self, prices: list) -> int:
        prices_len = len(prices)
        low = 0
        high = prices_len - 1
        self.maxProfit0(prices, low, high)
        print("call count %d" % self.count)
        if len(self.profit) == 0:
            return 0
        else:
            return max(self.profit)

    def maxProfit0(self, prices: list, low: int, high: int):
        if low >= high:
            return
        buy_index = self.getMinBuyPriceIndex(prices, low, high)
        sell_index = self.getMaxSellPriceIndex(prices, low, high)
        if buy_index < sell_index:
            self.profit.append(prices[sell_index]-prices[buy_index])
            return
        elif buy_index == sell_index:
            return
        else:
            if len(self.profit) >= 1 and self.profit[0] >= prices[sell_index]-prices[buy_index]:
                return
            self.maxProfit0(prices, buy_index, high)
            self.maxProfit0(prices, low, sell_index)
            self.maxProfit0(prices, sell_index+1, buy_index-1)

    def getMaxSellPriceIndex(self, prices: list, low: int, high: int) -> int:
        self.count += 1
        max_sell_price_index = low
        for i in range(low, high+1):
            if prices[max_sell_price_index] < prices[i]:
                max_sell_price_index = i
        return max_sell_price_index

    def getMinBuyPriceIndex(self, prices: list, low: int, high: int) -> int:
        self.count += 1
        min_buy_price_index = low
        for i in range(low, high+1):
            if prices[i] < prices[min_buy_price_index]:
                min_buy_price_index = i
        return min_buy_price_index


if __name__ == "__main__":
    prices = [0, 3, 9, 1, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
