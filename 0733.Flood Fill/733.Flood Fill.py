# 解法1
# DFS 的寫法相對簡潔一些，首先判斷如果給定位置的顏色跟新的顏色相同的話，直接返回，否則就對給定位置調用遞歸函數。
# 在遞歸函數中，如果越界或者當前顏色跟起始顏色不同，直接返回。
# 否則就給當前位置賦上新的顏色，然後對周圍四個點繼續調用遞歸函數
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    if image[sr][sc] == color:
        return image
    helper(image, sr, sc, image[sr][sc], color)
    return image

def helper(image: list[list[int]], sr: int, sc: int, color: int, new_color: int):
    # 行列長度
    m, n = len(image), len(image[0])

    # 終止條件 越界 or image[sr][sc] != color
    if sr < 0 or sr >= m or sc < 0 or sc >= n or image[sr][sc] != color:
        return

    image[sr][sc] = new_color
    # 向上下左右遞規
    helper(image, sr - 1, sc, color, new_color)
    helper(image, sr + 1, sc, color, new_color)
    helper(image, sr, sc - 1, color, new_color)
    helper(image, sr, sc + 1, color, new_color)

