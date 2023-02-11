
#解法1 
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            t = t.setdefault(w,{})
        t['$'] = None
    # search 和 startsWith  只差在判斷'$' 若'$' 代表以遍歷完該路程到表完全符合
    def search(self, word: str) -> bool:
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '$' in t:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)