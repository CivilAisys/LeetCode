# 解法1
# 由於我們知道兩個陣列內分別都是排序好的數字，因此可以分別利用參數m與n，從陣列的最後一個數字開始進行兩兩比對，
# 如果比較大的就將其直接放進nums1的尾巴，如果比較小的數就繼續留著等待比對，最多經過m+n次的迴圈後，就一定能將兩個陣列合併
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # 從後面開始比對
    for i in range(1, m+n+1):
        # nums2已經都移動至num1中  可跳離迴圈
        if n == 0:
            break
        # num1沒有值 依序將nums2的值塞入num1
        if m == 0:
            nums1[-i] = nums2[n-1]
            n -= 1
            continue
        
        if nums1[m-1] <nums2[n-1]:
            nums1[-i] = nums2[n-1]
            n-=1
        else:
            nums1[-i] = nums1[m-1]
            m-=1

merge([1,2,3,0,0,0],3,[2,5,6],3)