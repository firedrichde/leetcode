from functools import total_ordering


@total_ordering
class Tweet:
    def __init__(self, id=-1,  index=-1, next=None):
        self.id = id
        self.index = index
        self.next = next

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Tweet) and o.index == index:
            return True
        else:
            return False

    def __lt__(self, o: object):
        return self.index > o.index


class LinkedTweet:
    def __init__(self):
        self.head = Tweet()

    def insert(self, tweet: Tweet):
        tweet.next = self.head.next
        self.head.next = tweet


class Twitter:
    RECTENT_NUMBER = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweets = dict()
        self.user_follows = dict()
        self.tweet_index = 0
        self.id_list = list()

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            # cam't follow yourself
            return
        if not self.containsUser(followerId):
            self.initUser(followerId)
        if not self.containsUser(followeeId):
            self.initUser(followeeId)
        if followeeId not in self.user_follows[followerId]:
            self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if not self.containsUser(followeeId):
            return
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if tweetId in self.id_list:
            # id can't used more than twice
            return
        tweet = Tweet(tweetId, self.tweet_index)
        self.tweet_index += 1
        if not self.containsUser(userId):
            self.initUser(userId)
        self.user_tweets[userId].insert(tweet)

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = list()
        if not self.containsUser(userId):
            return tweets
        if userId in self.user_tweets:
            posts = self.getNewsFeedFromUser(userId)
            for post in posts:
                tweets.append(post)
        if len(self.user_follows[userId]) == 0:
            return [elem.id for elem in tweets]
        else:
            followee_set = self.user_follows[userId]
            for followee in followee_set:
                follow_posts = self.getNewsFeedFromUser(followee)
                for post in follow_posts:
                    tweets.append(post)
            tweets.sort()
            tweets = [elem.id for elem in tweets]
            if len(tweets) > 10:
                tweets = tweets[0:10]
            return tweets

    def getNewsFeedFromUser(self, userId: int) -> list:
        tweets = list()
        if userId not in self.user_tweets:
            return tweets
        num = 0
        node = self.user_tweets[userId].head
        while node.next is not None and num < Twitter.RECTENT_NUMBER:
            tweets.append(node.next)
            node = node.next
            num += 1
        return tweets

    def containsUser(self, userId: int) -> bool:
        return userId in self.user_tweets

    def initUser(self, userId: int) -> None:
        self.user_tweets[userId] = LinkedTweet()
        self.user_follows[userId] = set()

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


if __name__ == "__main__":
    test_obj = Twitter()
    test_obj.postTweet(1, 1)
    test_obj.follow(2, 1)
    # test_obj.postTweet(2, 6)
    print(test_obj.getNewsFeed(1))
    print(test_obj.getNewsFeed(2))
    test_obj.unfollow(2, 1)
    print(test_obj.getNewsFeed(1))
    print(test_obj.getNewsFeed(2))
