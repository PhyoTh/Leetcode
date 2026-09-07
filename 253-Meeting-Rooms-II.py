class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort()

        for start, end in intervals:
            inserted = False
            for i in range(len(rooms)):
                if rooms[i][-1][1] <= start:
                    rooms[i].append([start, end])
                    inserted = True
                    break
            
            if not inserted:
                rooms.append([[start, end]])
        
        return len(rooms)