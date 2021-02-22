class LetterNode:
    MAP = dict()
    letters = "abcdefghijklmnopqrstuvwxyz"
    NUM = len(letters)
    for i in range(NUM):
        MAP[letters[i]] = i

    def __init__(self, value=None):
        # if value is not None, path which from root node to current node 
        # represents a word is stored
        self.value = value
        self.next_array = [None for i in range(LetterNode.NUM)]

    def getNextNodeIndex(self, letter: str) -> int:
        index = LetterNode.MAP[letter]
        return index


class WordDictionary:

    def __init__(self):
        self.rootNode = LetterNode()
        self.dot = '.'
        self.value = 0

    def addWord(self, word: str) -> None:
        self.rootNode = self.addWord0(self.rootNode, word, 0)

    def addWord0(self, node: LetterNode, word: str, index: int) -> LetterNode:
        if node is None:
            node = LetterNode()

        if len(word) == index:
            # assign value to store the word
            node.value = self.value
            self.value += 1
            return node
        else:
            letter = word[index]
            next_node_index = node.getNextNodeIndex(letter)
            node.next_array[next_node_index] = self.addWord0(
                node.next_array[next_node_index], word, index+1)
            return node

    def search(self, word: str) -> bool:
        return self.search0(self.rootNode, word, 0)

    def search0(self, node: LetterNode, word: str, index: int) -> bool:
        tmp_node = node
        for i in range(index, len(word)):
            letter = word[i]
            if letter == self.dot:
                for next_node in tmp_node.next_array:
                    if next_node is not None and self.search0(next_node, word, i+1):
                        return True
                return False
            else:
                next_node_index = tmp_node.getNextNodeIndex(letter)
                next_node = tmp_node.next_array[next_node_index]
                if next_node is not None:
                    tmp_node = next_node
                else:
                    return False
        return self.isASolution(tmp_node)

    def isASolution(self, node: LetterNode):
        return node is not None and node.value is not None


if __name__ == "__main__":
    test_word_dictionary = WordDictionary()
    test_word_dictionary.addWord("bad")
    test_word_dictionary.addWord("dad")
    test_word_dictionary.addWord("mad")
    # print(test_word_dictionary.search("bd"))
    print(test_word_dictionary.search("b.d"))
