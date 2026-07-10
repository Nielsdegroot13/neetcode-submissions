class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Sorted = {}
        AnList = []

        for s in strs:
            Can = {}
            for ns in s:
                Can[ns] = Can.get(ns,0) + 1
            Idx = tuple(sorted(Can.items()))
            if Idx not in Sorted:
                Sorted[Idx] = []

            Sorted[Idx].append(s)

        for an in Sorted:
            AnL = Sorted[an] #Gets the string that are anagrams.
            AnList.append(AnL) # Puts in to retrurn


        return AnList


            





