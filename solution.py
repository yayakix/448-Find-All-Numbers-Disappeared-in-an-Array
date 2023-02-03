class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        rangeMap = {}
        numsMap = {}
        for x in range(1,len(nums) + 1):
            rangeMap[x] = True
        for num in nums:
            if num not in numsMap:
                numsMap[num] = True
        for x in rangeMap:
            if x not in numsMap:
                missing.append(x)
        return missing
