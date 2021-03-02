class UniqueNode:
    Letters = "abcdefghijklmnopqrstuvwxyz"
    LettersIndexMap = dict()
    for i in range(len(Letters)):
        LettersIndexMap[Letters[i]] = i

    def __init__(self):
        self.num = 26
        self.letter_map = dict()
        self.unique_num = 0
        self.unique_letters = list()
        self.visible = list()
        self.init_letter = '*'
        self.letters_count = 0

    def parse(self, letters):
        self.letters_count = len(letters)
        for i in range(len(letters)):
            letter = letters[i]
            if letter not in self.letter_map.keys():
                self.letter_map[letter] = list()
                self.unique_num += 1
            self.letter_map[letter].append(i)
        self.visible = [True for i in range(self.num)]
        for i in range(len(letters)):
            letter_to_add = letters[i]
            letter_to_add_index = self.getIndex(letter_to_add)
            # unique_letters contains the letter which is going to add
            if not self.visible[letter_to_add_index]:
                continue
            while len(self.unique_letters) > 0:
                compare_letter = self.unique_letters[-1]
                compare_letter_index = self.getIndex(compare_letter)
                # remove bigger and repulicated letter 
                if compare_letter > letter_to_add and self.letterAvaible(compare_letter, i):
                    self.visible[compare_letter_index] = True
                    self.unique_letters.pop()
                else:
                    break
            self.unique_letters.append(letter_to_add)
            self.visible[letter_to_add_index] = False

    def letterAvaible(self, letter, index):
        index_list = self.letter_map[letter]
        return index_list[-1] > index

    def getIndex(self, letter: str) -> int:
        return UniqueNode.LettersIndexMap[letter]


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        uniqueNode = UniqueNode()
        uniqueNode.parse(s)
        return "".join(uniqueNode.unique_letters)


if __name__ == "__main__":
    test_str = "cbacdcbc"
    test_sol = Solution()
    print(test_sol.removeDuplicateLetters(test_str))
