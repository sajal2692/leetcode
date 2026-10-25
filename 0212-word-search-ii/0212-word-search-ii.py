class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        root = TrieNode()

        for word in words:
            curr = root
            for c in word: 
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.isWord = True

        ROWS, COLS = len(board), len(board[0])
        visited, results = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                results.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)

            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")

        return list(results) 