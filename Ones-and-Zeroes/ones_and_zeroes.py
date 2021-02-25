from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, values) -> None:
        self.value = values
        self.length = len(values)
        self.ones = 0
        self.zeroes = 0
        for value in self.value:
            if value == '0':
                self.zeroes += 1
            elif value == '1':
                self.ones += 1

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Node):
            return False
        else:
            return self.length == o.length and self.ones == o.ones and self.zeroes == o.zeroes

    def __lt__(self, o) -> bool:
        if self.length < o.length:
            return True
        elif self.length == o.length:
            return self.zeroes > o.zeroes
        else:
            return False

    def __str__(self):
        return self.value

    def __repr__(self) -> str:
        return self.value


class Solution:
    def __init__(self):
        self.size = 0
        self.filter_node_list = list()
        self.result_node_list = None

    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        node_list = list()
        for binary_strings in strs:
            node_list.append(Node(binary_strings))
        node_list.sort()
        print(node_list)
        for node in node_list:
            if node.length > m+n:
                break
            if node.zeroes > m:
                continue
            if node.ones > n:
                continue
            else:
                self.filter_node_list.append(node)
        if len(self.filter_node_list) == 0:
            return 0
        else:
            zeroes = 0
            ones = 0
            result_node_list = list()
            self.search(result_node_list, m, n, 0, 0, 0)
            print(self.result_node_list)
            return self.size

    def search(self, nodes: list, m: int, n: int, zeroes: int, ones: int, start_index: int) -> None:
        if len(nodes) + len(self.filter_node_list)-start_index < self.size:
            return
        if zeroes > m or ones > n:
            if len(nodes)-1 > self.size:
                self.result_node_list = [node for node in nodes]
                self.result_node_list.pop()
                self.size = len(nodes)-1
            return
        if start_index >= len(self.filter_node_list):
            if len(nodes) > self.size:
                self.result_node_list = [node for node in nodes]
                self.size = len(nodes)
            return
        else:
            if len(nodes) > self.size:
                self.size = len(nodes)
            for i in range(start_index, len(self.filter_node_list)):
                node = self.filter_node_list[i]
                # if node.zeroes+zeroes > m or node.ones+ones > n:
                    # continue
                nodes.append(node)
                self.search(nodes, m, n, zeroes +
                            node.zeroes, ones+node.ones, i+1)
                nodes.pop()


if __name__ == "__main__":
    test_values = ["10", "1", "0"]
    test_values = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
    test_m =9 
    test_n = 80
    test_sol = Solution()
    print(test_sol.findMaxForm(test_values, test_m, test_n))
