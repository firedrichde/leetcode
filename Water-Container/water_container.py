class WaterContainer(object):

    def makeArea(self, height: list) -> int:
        """
        Given n non-negative integers a1, a2, ..., an , 
        where each represents a point at coordinate (i, ai). 
        n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
        Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
        Notice that you may not slant the container.
        """
        if len(height) == 0:
            return 0
        return self.makeArea0(height, 0, len(height)-1)

    def makeArea0(self, height: list, start: int, end: int) -> int:
        area = 0
        left_index = start
        right_index = end
        while left_index < right_index:
            tmp = WaterContainer.getArea(
                height[left_index], height[right_index],
                right_index-left_index)
            if tmp > area:
                area = tmp
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return area

    @staticmethod
    def getArea(x, y, n):
        return min(x, y)*n


if __name__ == "__main__":
    test_height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test_water_container = WaterContainer()
    actual_area = test_water_container.makeArea(test_height)
    print(actual_area)
