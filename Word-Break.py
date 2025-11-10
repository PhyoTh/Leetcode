class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordSet = set(wordDict)

    #     # top-down with caching
    #     def rollout(start: int, seen: dict()) -> bool:
    #         if start == len(s):
    #             return True
    #         if start in seen:
    #             return seen[start]

    #         for end in range(start + 1, len(s) + 1):
    #             if s[start: end] in wordSet:
    #                 if rollout(end, seen):
    #                     seen[start] = True
    #                     return True

    #         seen[start] = False
    #         return False

    #     return rollout(0, {})


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up
        # dp[i] = is it possible to build up to substring 0 to i using worddict
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]
