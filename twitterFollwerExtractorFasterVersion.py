import tweepy
import pandas as pd

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#kpmaurya1
#_debashish_roy
celebrity = api.get_user(screen_name = "kpmaurya1")
print(celebrity.id)


user_list = [celebrity.id]
follower_list = []

for user in user_list:
    followers = []
    try:
        for page in tweepy.Cursor(api.get_friend_ids, user_id=user).pages():
            followers.extend(page)
    except tweepy.TweepyException as e:
        print("error")
        continue
    follower_list.append(followers)


df = pd.DataFrame(columns=['source','target']) #Empty DataFrame
df['target'] = follower_list[0] #Set the list of followers as the target column
df['source'] = celebrity.id #Set my user ID as the source 


user_list = list(df['target']) #Use the list of followers we extracted in the code above i.e. my 450 followers
count=2
for userID in user_list:
    print(count," :",userID)
    count+=1
    followers = []
    follower_list = []

    try:
        for page in tweepy.Cursor(api.get_friend_ids, user_id=userID).pages():
            #followers.extend(page)
            for member in page:
                if member in user_list or member==celebrity.id:
                    followers.append(member)

            if len(followers) >= 1000: #Only take first 5000 followers
                break
    except tweepy.TweepyException as e:
        print("error")
        continue

    follower_list.append(followers)
    temp = pd.DataFrame(columns=['source', 'target'])
    temp['target'] = follower_list[0]
    temp['source'] = userID
    df = df.append(temp)
    #df.con

df.to_csv("debashish.csv")
# source will direct to target
