class Solution(object):
    """
    docstring
    """

    def __init__(self):
        self.address_list = []

    def restoreIpAddress(self, s: str) -> list:
        """
        docstring
        """
        if len(s)>12:
            return list()
        ip = list()
        ip.append(s)
        self.solvable(ip)
        result = self.buildIpStr()
        return result

    def solvable(self, ip: list):
        """
        docstring
        """
        # print(ip)
        if self.ipSolved(ip):
            self.address_list.append(ip)
        else:
            last_item = ip[-1]
            if len(last_item) <= 1:
                return
            else:
                for i in range(1, len(last_item)):
                    new_ip = self.makeIp(ip, i)
                    if(self.solvable(new_ip)):
                        self.address_list.append(new_ip)

    def ipSolved(self, ip: list):
        if len(ip) != 4:
            return False
        for elem in ip:
            if len(elem) > 1 and elem[0] == '0':
                return False
            num = int(elem)
            if num < 0 or num > 255:
                return False
        return True

    def makeIp(self, items: list, index: int):
        newIp = list()
        for i in range(len(items)-1):
            newIp.append(items[i])
        last_item = items[-1]
        left = last_item[0:index]
        right = last_item[index:]
        newIp.append(left)
        newIp.append(right)
        return newIp

    def buildIpStr(self):
        result = list()
        for elem in self.address_list:
            result.append(".".join(elem))
        return result


if __name__ == "__main__":
    # test_str = "25525511135"
    test_str ="010010"
    test_sol = Solution()
    ret = test_sol.restoreIpAddress(test_str)
    print(ret)
