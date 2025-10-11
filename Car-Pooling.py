class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        capacity = 3
        [[2,1,5],[2,5,7],[1,3,6]]

        window_capacity = {
            (1, 5) : 0
            (5, 7) : 0
            (3, 6) : 2
        }
        '''
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True
