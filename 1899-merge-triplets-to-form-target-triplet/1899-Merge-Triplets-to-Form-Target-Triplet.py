class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        result = [float('-inf'), float('-inf'), float('-inf')]
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            result = [max(result[0], triplet[0]), max(result[1], triplet[1]), max(result[2], triplet[2])]

        return result == target