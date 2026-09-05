class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #it is a classic example of the 2 pointers method:
        i = m - 1 #poniter for the last number in arr 1
        j = n - 1 #poniter for the last number in arr 2
        k = m + n -1 #poniter for the last number in merged array aa1 and aar2

        #merger for the end
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-= 1
            else:
                nums1[k] = nums2[j]
                j-= 1
            k-= 1