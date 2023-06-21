# 使用字典樹進行字串的插入及搜索
# 字典樹的主要特點是，具有相同前綴的字符串在樹中共享相同的前綴路徑。
# 這使得字典樹非常適合用於存儲大量的字符串集合，並且能夠在這些字符串中高效地執行搜索、插入和刪除操作。
# 字典樹中，每個節點代表一個字符 is_word的作用判斷該字符結尾是否為一完整字串
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        # 保存根結點的引用
        self.root = TrieNode()

    # 新增時都由根結點開始
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            # 改變node節點為下一字元
            node = node.children[char]
        # 迴圈結束表示到尾端  表示完整字元(is_word為True)
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)

    def searchHelper(self, word: str, node: TrieNode) -> bool:
        for i in range(len(word)):
            char = word[i]
            # 需判斷該字元是否為 "."
            if char == '.':
                for child in node.children.values():
                    # 遞規對子節點進行查詢 並截斷該字元"."
                    if self.searchHelper(word[i+1:], child):
                        return True
                return False
            elif char not in node.children:
                return False
            else:
                # 該字元若在其子節點內則改變該node指向為下一節點
                node = node.children[char]
        # 迴圈結束  返回is_word判定是否為完整字串
        return node.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
