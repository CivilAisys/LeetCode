# 解法1 遞迴求解  此題為演算法中的 Backtracking(回溯法) 窮舉
def generateParenthesis(n: int) -> list[str]:
    # 結果集
    result = []
    # 遞迴函式 窮舉

    def generate(left: int, right: int, string: str):
        # 結束條件為 left == n and right ===n
        if left == n and right == n:
            result.append(string)
            return

        # 左括弧持續條件為 < n 右括弧為 < n and < left
        if left < n:
            generate(left+1, right, f"{string}(")
        if left > right and right < n:
            generate(left, right+1, f"{string})")
        # 初始化
        generate(0, 0, "")

    return None
