import functools


class Solution(object):
    class Interval(object):
        def __init__(self, item: list):
            self.start = item[0]
            self.end = item[1]

        def __str__(self):
            return '['+self.start+', '+self.end+']'

        def compareTo(self, interval) -> int:
            """
            compare with another interval
            """
            if self.start == interval.start:
                return self.end - interval.end
            else:
                return self.start-interval.start

        def overlap(self, interval):
            if self.compareTo(interval) > 0:
                interval.overlap(self)
            else:
                if self.end < interval.start:
                    return None
                else:
                    return Solution.Interval(
                        [self.start, max(self.end, interval.end)])

        def toList(self):
            return [self.start, self.end]

        @staticmethod
        def compare(x, y) -> int:
            """
            docstring
            """
            if x.start == y.start:
                return x.end - y.end
            else:
                return x.start-y.end

    def merge(self, intervals: list) -> list:
        """
        docstring
        """
        intervals = [self.Interval(item) for item in intervals]
        if not self.isSorted(intervals):
            intervals = self.sort(intervals)
        new_intervals = self.merge0(
            intervals, 0, len(intervals)-1)
        result = []
        for interval in new_intervals:
            result.append(interval.toList())
        return result

    def merge0(self, intervals: list, low: int, high: int) -> list:
        ret = list()
        if low == high:
            ret.append(self.Interval(
                [intervals[low].start, intervals[low].end]))
            return ret
        else:
            mid = (low+high)//2
            left = self.merge0(intervals, low, mid)
            right = self.merge0(intervals, mid+1, high)
            for i in range(len(left)-1):
                ret.append(left[i])
            current_interval = left[-1]
            index = 0
            while index <= len(right)-1:
                tmp = current_interval.overlap(right[index])
                if tmp is None:
                    ret.append(current_interval)
                    current_interval = right[index]
                else:
                    current_interval = tmp
                index += 1
            ret.append(current_interval)
            return ret

    def isSorted(self, intervals: list) -> list:
        intervals_len = len(intervals)
        if intervals_len <= 1:
            return True
        else:
            for i in range(1, intervals_len):
                if intervals[i].compareTo(intervals[i-1]) < 0:
                    return False
            return True

    def sort(self, intervals: list):
        # print(intervals)
        return sorted(intervals, key=functools.cmp_to_key(self.Interval.compareTo))
        # intervals_len = len(intervals)
        # for i in range(intervals_len):
        #     min_index = i
        #     for j in range(i+1, intervals_len):
        #         if intervals[j].compareTo(intervals[min_index]) < 0:
        #             min_index = j
        #     tmp = intervals[min_index]
        #     intervals[min_index] = intervals[i]
        #     intervals[i] = tmp
        # print(intervals)


if __name__ == "__main__":
    test_sol = Solution()
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18],[1,20]]
    intervals = [[4, 5], [2, 4], [4, 6], [
        3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]
    # intervals = [[1, 4], [4, 5]]
    print(test_sol.merge(intervals))
