# 解法1
# 走完環的前題為gas總量大於cost總量  設置起始點
# 當前的gas值大於cost值，就可以繼續前進，此時到下一個網站，剩餘的gas加上當前的gas再減去cost，看是否大於0，若大於0，
# 則繼續前進。當到達某一網站時，若這個值小於0了，則說明從起點到這個點中間的任何一個點都不能作為起點，
# 則把起點設為下一個點，繼續遍歷。當遍曆完整個環時，當前保存的起點即為所求(因題目有說若有解則只有唯一解)
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start = 0 # 起點索引
        tank = 0 # 當前剩餘油量
        total = 0 # 油量 與 消耗 相減的總量

        # 遍歷站點 
        for i in range(len(gas)):
            # 剩餘油量 + gas[i] - cost[i] < 0 則起始點移至i+1 並將剩餘油量歸零
            if tank + gas[i] - cost[i] < 0:
                start = i + 1 
                tank = 0
            else:
                tank += gas[i] - cost[i]
            total += gas[i] - cost[i]
        # 若總消耗大於總油量 不可能跑完整個環
        return -1 if total < 0 else start
