class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchHelper(curr, word)

    def searchHelper(self, start: TrieNode, remaining_word: str):
        curr = start
        for c in remaining_word: 
            if c == ".":
                return any([self.searchHelper(child, remaining_word[1:]) for child in curr.children.values()])
            elif c not in curr.children:
                return False
            curr = curr.children[c]
            remaining_word = remaining_word[1:]
        return True if curr.word else False
            




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)