from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counter = Counter(tasks)
        max_count = max(tasks_counter.values())
        max_nums = sum(1 for c in tasks_counter.values() if c == max_count)

        interval = (max_count - 1) * (n + 1) + max_nums
        return interval if interval > len(tasks) else len(tasks)