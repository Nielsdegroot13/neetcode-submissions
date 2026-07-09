class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        MostK = 0

        Counter = dict()
        IndexCount = {}

        BinList = [[] for _ in range(len(nums) + 1)]
        RetList = []

        for i in range(len(nums)):
            n = nums[i]

            #Count the numbers:
            Count = Counter.get(n,0) + 1
            Counter[n] = Count

            #Store K:
            if Count > MostK:  MostK = Count

            #GetList:

        for Cn in Counter:
            Index = Cn #Get the idex?
            Bin = Counter.get(Cn , 0) #Get the Freq to deside its bin
            BinList[Bin].append(Index + 1000)

      
        StoredK = 0
        for i in range(MostK,0,-1):
            for n in range(len(BinList[i])):
                if BinList[i][n] > 0 :
                    RetList.append(BinList[i][n] - 1000)
                    StoredK += 1

                    if StoredK >= k:
                        return RetList
        return RetList

        
