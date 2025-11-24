class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        '''
        we are doing binary search on the answer (time)
        '''
        # precompute the LCM of recharge intervals
        import math
        lcm = math.lcm(r[0], r[1])
        def can_complete(time):
            '''
            we can calculate the number of recharging that drone ith needs, given time 
                -> time // r[i]
            then, we can get the number of deliveries that drone ith can do, given time
                -> time - (time // r[i])
            '''
            # number of deliveries that drone 1 can do, within given time
            slot1 = time - (time // r[0])

            # number of deliveries that drone 2 can do, within given time
            slot2 = time - (time // r[1])

            # number of deliveries that both drone 1 and drone 2 can accomplish without
            # overlapping the recharging hours (LCM of r[0] and r[1])
            slot3 = time - (time // lcm)

            return (slot1 >= d[0]) and (slot2 >= d[1]) and (slot3 >= d[0] + d[1])
        
        low = d[0] + d[1] # each delivery needs at least 1 hour (lower bound)
        high = 2 * low
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            if can_complete(mid): # this works, try smaller
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans