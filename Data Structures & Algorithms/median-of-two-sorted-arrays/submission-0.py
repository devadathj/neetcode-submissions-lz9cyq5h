class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        half = (len(nums1) + len(nums2)) // 2

        l = 0
        r = len(nums1) - 1
        
        while True:
            mid = (l + r) // 2
            mid2 = half - mid - 2

            left1 = nums1[mid] if mid >= 0 else float("-inf")
            right1 = nums1[mid + 1] if mid + 1 < len(nums1) else float("inf")
            left2 = nums2[mid2] if mid2 >= 0 else float("-inf")
            right2 = nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)

            if left1 > right2:
                r = mid - 1
            else:
                l = mid + 1
