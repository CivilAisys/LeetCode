# 解法1
# 自定義排序方法，按照離原點的距離從小到大排序，注意這裡我們並不需要求出具體的距離值，
# 只要知道互相的大小關係即可，所以並不需要開方。排好序之後，返回前k個點即可
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    # 依照距離排序 
    points.sort(key=lambda x: x[0] * x[0] + x[1] * x[1])

    return points[:k]

print(kClosest([[1,3],[-2,2]],1))
