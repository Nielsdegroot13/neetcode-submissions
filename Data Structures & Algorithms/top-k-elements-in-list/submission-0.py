class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        MostK = 0
        Counter = dict()
        IndexCount = {}

        Ret = []

        for i in range(len(nums)):
            n = nums[i]

            #Count the numbers:
            Count = Counter.get(n,0) + 1
            Counter[n] = Count

            #Store K:
            if Count > MostK: Number = n; Mostk = Count

            #GetList:


            
        ranked = sorted(Counter, key=Counter.get, reverse=True)
       
        ReturnList = []

        for i in range(k):
            ReturnList.append(ranked[i])

        return ReturnList
        
