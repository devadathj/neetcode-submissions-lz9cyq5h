class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check_split(mid):
            cur_total = 0
            cur_segments = 1
            for num in nums:
                if cur_total + num <= mid:
                    cur_total += num
                else:
                    if cur_segments >= k:
                        return False
                    else:
                        cur_total = num
                        cur_segments += 1
            return True
            

        l = max(nums)
        r = sum(nums)

        output = r
        while l <= r:
            mid = (l + r) // 2

            if check_split(mid):
                output = mid
                r = mid - 1
            else:
                l = mid + 1

        return output