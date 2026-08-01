from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.timestamp = 1
        self.user_tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_tweets and userId not in self.following:
            return []
        
        print(self.user_tweets)
        print(self.timestamp)
        heap = []
        if self.user_tweets[userId]:
            timestamp, tweetId = self.user_tweets[userId][-1]
            heapq.heappush(heap, (-timestamp, userId, len(self.user_tweets[userId]) - 1, tweetId))
        
        for followeeId in self.following[userId]:
            if self.user_tweets[followeeId]:
                timestamp, tweetId = self.user_tweets[followeeId][-1]
                heapq.heappush(heap, (-timestamp, followeeId, len(self.user_tweets[followeeId]) - 1, tweetId))
        
        result = []
        while heap:
            _, userId, index, tweetId = heapq.heappop(heap)
            result.append(tweetId)
            if len(result) == 10:
                break

            if index > 0:
                timestamp, tId = self.user_tweets[userId][index - 1]
                heapq.heappush(heap, (-timestamp, userId, index - 1, tId))
            
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following or followeeId not in self.following[followerId]:
            return

        self.following[followerId].remove(followeeId)
        if len(self.following[followerId]) == 0:
            del self.following[followerId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)