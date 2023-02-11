
#解法1 
#對每個結點開一個字母集大小的陣列，
#對應的下標是兒子所表示的字母，內容則是這個兒子對應在大數位上的位置，即標號

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            t = t.setdefault(w,{})
        t['$'] = None
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