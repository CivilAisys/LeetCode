# 解法1  Union Find 
# 解析 首先遍歷每個帳戶和其中的所有郵箱，先將每個郵箱的 root 映射為其自身，然後將 owner 賦值為使用者名。
# 然後開始另一個迴圈，遍曆每一個帳號，首先對帳號的第一個郵箱調用 find 函數，得到其父串p，
# 然後遍歷之後的郵箱，對每個遍歷到的郵箱先調用 find 函數，將其父串的 root 值賦值為p，這樣做相當於將相同帳號內的所有郵箱都連結起來了。
# 接下來要做的就是再次遍歷每個帳戶內的所有郵箱，先對該郵箱調用 find 函數，找到父串，然後將該郵箱加入該父串映射的集合匯總，這樣就就完成了合併。
# 最後只需要將集合轉為字串數位，加入結果 res 中，通過 owner 映射找到父串的使用者名，加入字串數位的首位置
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 結果數組 root數組映射自身  owner附值使用者名
        result = []
        root = {}
        owner = {}
        map = {}
        # 先將root建立為郵件映射自身 owner為郵件key對應使用者value
        for account in accounts:
            for i in range(1,len(account)):
                root[account[i]] = account[i]
                owner[account[i]] = account[0]
        # 將同帳號的郵箱連結起來 key為 account[1] value為account[i] i > 1
        for account in accounts:
            p = self.find(account[1], root)
            for i in range(2,len(account)):
                root[self.find(account[i], root)] = p
        # map為將該郵箱加入該父串映射的集合匯總 使用set去重  結果需要轉回list
        for account in accounts:
            for i in range(1,len(account)):
                map.setdefault(self.find(account[i], root), set()).add(account[i])
        # 遍歷 map
        for a in map.values():
            # 將set轉回list
            mail_list = sorted(list(set(a)))
            # 將對應mail擁有者插入list的頭及完成合併
            mail_list.insert(0, owner[mail_list[0]])
            result.append(mail_list)
        
        return result
    
    def find(self, s: str, root: list[list[str]])-> str:
        return s if root[s] == s else self.find(root[s],root)
    
test = Solution()
test.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])