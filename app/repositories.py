# app/repositories.py
# pylint: disable=missing-docstring

class TweetRepository:
    def __init__(self):
        self.__clear()

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1

    def get(self, id):
      for tweet in self.tweets:
          if tweet.id == id:
              return tweet
      return None

    def __clear(self):
      self.tweets = []
      self.next_id = 1

