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
                    return Solution.Interval([self.start, max(self.end, interval.end)])

        def toList(self):
            return [self.start, self.end]

    def merge(self, intervals: list) -> list:
        """
        docstring
        """
        intervals = [self.Interval(item) for item in intervals]
        if not self.isSorted(intervals):
            self.sort(intervals)
        new_intervals = self.merge0(
            intervals, 0, len(intervals)-1)
        result = []
        for interval in new_intervals:
            result.append(interval.toList())
        return result

    def merge0(self, intervals: list, low: int, high: int) -> list:
        if low == high:
            ret = list()
            ret.append(self.Interval(
                [intervals[low].start, intervals[low].end]))
            return ret
        else:
            mid = (low+high)//2
            left = self.merge0(intervals, low, mid)
            right = self.merge0(intervals, mid+1, high)
            overlap_ret = left[-1].overlap(right[0])
            ret = list()
            if overlap_ret == None:
                for elem in left:
                    ret.append(elem)
                for elem in right:
                    ret.append(elem)
                return ret
            else:
                left_index = len(left)-1
                tmp = None
                while left_index >= 0:
                    tmp = overlap_ret
                    overlap_ret = overlap_ret.overlap(left[left_index])
                    if overlap_ret is None:
                        break
                    left_index -= 1
                if overlap_ret is None:
                    ret.extend(left[0:left_index+1])
                    overlap_ret = tmp
                right_index = 0
                while right_index < len(right):
                    tmp = overlap_ret
                    overlap_ret = overlap_ret.overlap(right[right_index])
                    if overlap_ret is None:
                        break
                    right_index += 1
                if overlap_ret is None:
                    ret.append(tmp)
                    ret.extend(right[right_index:])
                else:
                    ret.append(overlap_ret)
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
        intervals_len = len(intervals)
        for i in range(intervals_len):
            min_index = i
            for j in range(i+1, intervals_len):
                if intervals[j].compareTo(intervals[min_index]) < 0:
                    min_index = j
            tmp = intervals[min_index]
            intervals[min_index] = intervals[i]
            intervals[i] = tmp


if __name__ == "__main__":
    test_sol = Solution()
    # intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    print(test_sol.merge(intervals))
