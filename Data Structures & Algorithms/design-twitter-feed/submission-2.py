import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.follower = {}
        self.posts = {}
        self.time = 0
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.addUserToSystem(userId)
        self.posts[userId][tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        news_feed = []

        for user in self.following[userId]:
            for key, value in self.posts[user].items():
                heapq.heappush_max(maxheap, (value, key))
        
        if userId not in self.following[userId]:
            for key, value in self.posts[userId].items():
                heapq.heappush_max(maxheap, (value, key))
        
        for _ in range(10):
            if maxheap:
                news_feed.append(heapq.heappop_max(maxheap)[1])
            else:
                break
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.addUserToSystem(followerId)
        self.addUserToSystem(followeeId)
        self.follower[followeeId].add(followerId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.addUserToSystem(followerId)
        self.addUserToSystem(followeeId)
        self.follower[followeeId].discard(followerId)
        self.following[followerId].discard(followeeId)
        
    def addUserToSystem(self, userId: int) -> None:
        if userId not in self.follower:
            self.follower[userId] = set()
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.posts:
            self.posts[userId] = {}