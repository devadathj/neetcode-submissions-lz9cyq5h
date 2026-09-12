class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        array_len = mountainArr.length()
        self.tracker = [-1] * array_len

        def array_val(index):
            if self.tracker[index] == -1:
                self.tracker[index] = mountainArr.get(index)

            return self.tracker[index]
        

        l = 1
        r = array_len - 2

        while l <= r:
            mid = (l + r) // 2

            if array_val(mid - 1) < array_val(mid) < array_val(mid + 1):
                l = mid + 1
            elif array_val(mid - 1) > array_val(mid) > array_val(mid + 1):
                r = mid - 1
            else:
                peak = mid
                break

        l = 0
        r = peak

        while l <= r:
            mid = (l + r) // 2

            if array_val(mid) < target:
                l = mid + 1
            elif array_val(mid) > target:
                r = mid - 1
            else:
                return mid
                
        l = peak
        r = array_len - 1

        while l <= r:
            mid = (l + r) // 2

            if array_val(mid) > target:
                l = mid + 1
            elif array_val(mid) < target:
                r = mid - 1
            else:
                return mid

        return -1
            