class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Got = set()
        for i in range(0,len(nums)):
            if nums[i] not in Got:
                Got.add(nums[i])
            else:
                return True
        return False

        