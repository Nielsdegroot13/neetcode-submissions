class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Index = {}
        Count = {}

        for i in range(len(nums)):
            n = nums[i]
            if n not in Index: Index[n] = i
            elif (n + n) == target: return [Index[n],i]


        for i in range(len(nums)):
            n = nums[i]
            Needed = target - n

            if Needed in Index:
                if Index[Needed] != Index[n]:
                    return [Index[n],Index[Needed]]
                
 
       





