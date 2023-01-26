# 解法1
# 二進位數相加，並且保存在 string 中，要注意的是如何將 string 和 int 之間互相轉換，
# 並且每位相加時，會有進位的可能，會影響之後相加的結果。
# 而且兩個輸入 string 的長度也可能會不同。
# 這時我們需要新建一個 string，它的長度是兩條輸入 string 中的較大的那個，
# 並且把較短的那個輸入 string 通過在開頭加字元 '0' 來補的較大的那個長度。這時候逐個從兩個 string 的末尾開始取出字元，然後轉為數位，
# 想加，如果大於等於 2，則標記進位標誌 carry，並且給新 string 加入一個字元 '0'
def addBinary(a: str, b: str) -> str:
    # new_string(結果) 進位
    new_string = ""
    carry = 0
    # 將ab長度較短的字串前面補0至長度兩者一致
    length_of_a = len(a)
    length_of_b = len(b)
    while length_of_a != length_of_b:
        if length_of_a > length_of_b:
            b = "0" + b
            length_of_b += 1
        elif length_of_a < length_of_b:
            a = "0" + a
            length_of_a += 1

    for index in range(len(a)-1, -1, -1):
        sum = int(a[index]) + int(b[index]) + carry
        new_string = str(sum % 2) + new_string
        carry = sum // 2

    # 可能最後還有進位  故需判斷carry是否>0
    if carry > 0:
        new_string = str(carry) + new_string

    return new_string
