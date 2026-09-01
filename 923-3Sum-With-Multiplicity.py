class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()

        count = 0
        for left in range(len(arr)):
            mid, right = left + 1, len(arr) - 1
            while mid < right:
                total = arr[left] + arr[mid] + arr[right]

                if total == target:
                    if arr[mid] != arr[right]:
                        mid_count = 1
                        mid_dup = mid + 1
                        while mid_dup < right and arr[mid_dup - 1] == arr[mid_dup]:
                            mid_count += 1
                            mid_dup += 1
                        
                        right_count = 1
                        right_dup = right - 1
                        while mid < right_dup and arr[right_dup + 1] == arr[right_dup]:
                            right_count += 1
                            right_dup -= 1
                        
                        mid = mid_dup
                        right = right_dup
                        count += mid_count * right_count
                    else:
                        dups = right - mid + 1
                        count += dups * (dups - 1) // 2
                        break

                elif total < target:
                    mid += 1
                elif total > target:
                    right -= 1
        return count % (10**9 + 7)