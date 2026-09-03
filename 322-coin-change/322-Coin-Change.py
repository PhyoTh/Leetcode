class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp_amount = [float('inf') for _ in range(amount + 1)]
        dp_amount[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp_amount[i] = min(dp_amount[i], dp_amount[i - coin] + 1)
        
        return dp_amount[amount] if dp_amount[amount] != float('inf') else -1