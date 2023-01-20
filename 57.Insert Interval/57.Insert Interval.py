#解法1 思維同56  
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    #將newInterval插入intervals
    intervals.append(newInterval)
    #將intervals依照intervals[i][0]排序
    intervals = sorted(intervals, key=lambda x:x[0])
    
    #結果集
    merge_result = []

    for interval in intervals:
        #若merge_result內沒有值 或是當前的頭大於merge_result內最後一個的尾 就將當前加入merge_result
        if not merge_result or interval[0] > merge_result[-1][1]:
            merge_result.append(interval)
        else:
        #更新merge_result內最後一個的尾
            merge_result[-1][1] = max(merge_result[-1][1], interval[1])

    return merge_result