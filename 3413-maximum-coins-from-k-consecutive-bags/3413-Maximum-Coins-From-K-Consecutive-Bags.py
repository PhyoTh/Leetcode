from bisect import bisect_right
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        def solve(segments) -> int:
            n = len(segments)
            
            sorted_segments = sorted(segments)
            starting_positions = [l for l, _, _ in sorted_segments]
            prefix_sum = [0 for _ in range(n + 1)]

            for i in range(1, n + 1):
                l, r, c = sorted_segments[i - 1]
                prefix_sum[i] = prefix_sum[i - 1] + (r - l + 1) * c
            
            best = 0
            for i, (l, _, _) in enumerate(sorted_segments):
                end = l + k - 1
                j = bisect_right(starting_positions, end) - 1
                total = prefix_sum[j] - prefix_sum[i]
                
                lj, rj, cj = sorted_segments[j]
                total += (min(rj, end) - lj + 1) * cj
                best = max(best, total)
                
            return best
        
        mirrored = [[-r, -l, c] for l, r, c in coins]
        return max(solve(coins), solve(mirrored))