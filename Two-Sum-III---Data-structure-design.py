class TwoSum:
    def __init__(self):
        self.seen_nums = {}  # {num : count}

    def add(self, number: int) -> None:
        self.seen_nums[number] = self.seen_nums.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.seen_nums:
            diff = value - num
            if diff == num:
                if diff in self.seen_nums and self.seen_nums[diff] > 1:
                    return True
            else:
                if diff in self.seen_nums:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)