from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=1000)
    followers = models.CharField(max_length=100)

    def __str__(self):
        return self.screen_name

class Tweet(models.Model):
    tweet_op = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_id = models.CharField(max_length=30)
    tweet_type = models.CharField(max_length=15)
    tweet_text = models.CharField(max_length=150)
    tweet_text2 = models.CharField(max_length=150)
    tweet_text_url = models.CharField(max_length=150)
    retweets = models.IntegerField()
    favourites = models.IntegerField()
    created_at = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tweet_text_url)