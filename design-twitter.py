# https://leetcode.com/problems/design-twitter/

# Design a simplified version of Twitter where users can post tweets, follow/unfollow 
# another user and is able to see the 10 most recent tweets in the user's news feed. 
# Your design should support the following methods:

# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 
# Each item in the news feed must be posted by users who the user followed or by the 
# user herself. Tweets must be ordered from most recent to least recent.

# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.

# Example:

# Twitter twitter = new Twitter();

# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);

# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);

# // User 1 follows user 2.
# twitter.follow(1, 2);

# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);

# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.getNewsFeed(1);

# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);

# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);



from collections import defaultdict
from heapq import *

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        cands = self.followers[userId] | {userId}
        cands = [self.tweets[fid][-10:][::-1] for fid in cands]
        cands = [(ts[0], ts[1:]) for ts in cands if ts]
        heapify(cands)
        
        sols = []
        for _ in range(10):
            if not cands: break
            (time, tweet), row = heappop(cands)
            if row: heappush(cands, (row[0], row[1:]))
            sols.append(tweet)
        return sols

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)