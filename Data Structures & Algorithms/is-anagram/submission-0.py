class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count = {}

        if len(s) != len(t):
            return False

        for n in s:
            Count[n] = Count.get(n,0) + 1

        for m in t:
            if m not in Count:
                return False

            Count[m] -= 1
            if Count[m] < 0:
                return False

        return True


        
        