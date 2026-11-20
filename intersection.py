class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        second = set(nums2)
        m = set(i for i in nums1 if i in second)

        return list(m)

