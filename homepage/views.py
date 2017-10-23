from operator import attrgetter

import sys
from django.shortcuts import render
from twitter import Twitter, OAuth
from .models import User, Tweet

token = '2963340618-4Wm7Ke69lIO1OI40uAQt2keQHzCpIkytvz2qISL'
token_secret = '123456789'
consumer_key = 'U3Z85uVP2lj7mAE4aSv5eulfn'
consumer_secret = '123456789'
twitter_auth = OAuth(token=token, token_secret=token_secret, consumer_key=consumer_key,
                     consumer_secret=consumer_secret)
t_conn = Twitter(auth=twitter_auth)


def homepage(request):
    t_home_timeline = t_conn.statuses.home_timeline()
    for tweet_items in t_home_timeline:
        save_tweet_flag = 0
        save_user_flag = 0
        user_id = ''
        user_name = ''
        screen_name = ''
        profile_pic_norm = ''
        followers_count = ''
        created_at = ''
        tweet_id = ''
        tweet_text1 = ''
        tweet_text2 = ''
        tweet_text_link = ''
        tweet_type = ''
        retweets = 0
        favorite = 0
        get_user = None
        for item in tweet_items.items():
            if item[0] == 'created_at':
                created_at = item[1]
            elif item[0] == 'id_str':
                tweet_id = item[1]
                try:
                    get_tweet = Tweet.objects.get(tweet_id=tweet_id)
                    save_tweet_flag = 0
                    # break
                # except Tweet.DoesNotExist:
                except:
                    save_tweet_flag = 1
                    # return render(request, 'homepage/error_check.html',
                    #               context={'error_vallue': sys.exc_info()[0]})

            elif item[0] == 'text':
                tweet_text_raw = item[1]
                check_link = tweet_text_raw.find('http')
                if check_link == 0:
                    check_link_pos = tweet_text_raw.find(' ')
                    if check_link_pos == -1:
                        tweet_type = 'URL'
                        tweet_text_link = tweet_text_raw
                    else:
                        tweet_type = 'URL_TWT'
                        tweet_elements = tweet_text_raw.split(' ', maxsplit=1)
                        tweet_text_link = tweet_elements[0]
                        tweet_text1 = tweet_elements[1]
                elif check_link == -1:
                    tweet_type = 'TWT'
                    tweet_text1 = tweet_text_raw
                else:
                    tweet_elements = tweet_text_raw.split(sep='http', maxsplit=1)
                    check_link_pos = tweet_elements[1].find(' ')
                    if check_link_pos == -1:
                        tweet_type = 'TWT_URL'
                        tweet_text1 = tweet_elements[0]
                        tweet_text_link = 'http' + tweet_elements[1]
                    else:
                        tweet_type = 'TWT_URL_TWT'
                        tweet_text1 = tweet_elements[0]
                        tweet_text2_and_link = tweet_elements[1].split(' ', maxsplit=1)
                        # print(tweet_text2_and_link)
                        tweet_text2 = tweet_text2_and_link[1]
                        tweet_text_link = 'http' + tweet_text2_and_link[0]
            elif item[0] == 'user':
                user_id = item[1]['id_str']
                user_name = item[1]['name']
                screen_name = item[1]['screen_name']
                profile_pic_norm = item[1]['profile_image_url_https']
                # profile_pic = ''.join(profile_pic_norm.split(sep='_normal'))
                followers_count = str(item[1]['followers_count'])
                try:
                    get_user = User.objects.get(user_id=user_id)
                    save_user_flag = 0
                # except User.DoesNotExist:
                except:
                    save_user_flag = 1
            elif item[0] == 'retweet_count':
                retweets = item[1]
            elif item[0] == 'favorite_count':
                favorite = item[1]

        if save_user_flag == 1:
            s = User(user_id=user_id, screen_name=screen_name, user_name=user_name, profile_pic=profile_pic_norm,
                     followers=followers_count)
            s.save()
        elif save_user_flag == 0 and user_id != '':
            s = get_user
            s.followers = followers_count
            s.save()

        if save_tweet_flag == 1:
            t2 = Tweet(tweet_op=s, tweet_id=tweet_id, tweet_type=tweet_type, tweet_text=tweet_text1,
                       tweet_text2=tweet_text2, tweet_text_url=tweet_text_link, retweets=retweets, favourites=favorite,
                       created_at=created_at)
            t2.save()
        elif save_tweet_flag == 0 and tweet_id != '':
            get_tweet.retweets = retweets
            get_tweet.favourites = favorite
            get_tweet.save()

    all_tweets = Tweet.objects.all()
    all_tweets_sorted = sorted(all_tweets, key=attrgetter('created_at'), reverse=True)
    all_users = User.objects.all()
    return render(request, 'homepage/home.html', context={'all_tweets': all_tweets_sorted, 'all_users': all_users})


def post_tweet(request):
    tweet_text = request.POST['tweet']
    t_conn.statuses.update(status=tweet_text)
    context = {'tweeted': tweet_text}
    return render(request, 'homepage/home.html', context=context)
