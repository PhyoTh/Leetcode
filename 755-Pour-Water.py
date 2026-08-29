class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        while volume > 0:
            local_min = k
            for i in range(k - 1, -1, -1):
                if heights[i] > heights[i + 1]:
                    break
                
                if heights[i] < heights[local_min]:
                    local_min = i
            
            if local_min == k:
                for i in range(k + 1, len(heights)):
                    if heights[i] > heights[i - 1]:
                        break
                    
                    if heights[i] < heights[local_min]:
                        local_min = i
            
            heights[local_min] += 1
            volume -= 1
        return heights