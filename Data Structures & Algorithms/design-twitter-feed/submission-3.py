class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = {userId}

        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []

        i = -1
        while -1 * i <= len(self.tweets) and len(output) < 10:
            if self.tweets[i][1] in self.follows[userId]:
                output.append(self.tweets[i][0])
            i -= 1

        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, {followerId}).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)

