class Solution(object):
    def simplifyPath(self, path: str) -> str:
        if path == '':
            return ''
        else:
            canonical_list = list()
            path_splits = path.split('/')
            for elem in path_splits:
                if elem == '.':
                    continue
                elif elem == '..':
                    if len(canonical_list) != 0:
                        canonical_list.pop()
                elif elem == '':
                    continue
                else:
                    canonical_list.append(elem)
            if len(canonical_list) == 0:
                return '/'
            else:
                return '/'+'/'.join(canonical_list)


if __name__ == "__main__":
    test_sol = Solution()
    test_path = '/a/./b/../../c/'
    print(test_sol.simplifyPath(test_path))
