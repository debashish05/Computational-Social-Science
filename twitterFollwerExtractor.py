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
celebrity = api.get_user(screen_name = "_debashish_roy")
print(celebrity.id)


def FollowingIDs(user,api):
    """ Given user Id (int) return list of user id (int) of people whom
    given user id is following"""

    following = []
    
    try:
        for page in tweepy.Cursor(api.get_friend_ids, user_id=user).pages():
            following.extend(page) #extended add all elements of page in list
    except tweepy.TweepyException as e:
        print("error")
    
    return following


following_list=FollowingIDs(celebrity.id,api)
print("No. of user that",celebrity.id,"follows: ",len(following_list))


following_list.append(celebrity.id)         #adding main user as well

for i in range(len(following_list)):
    for j in range(i+1,len(following_list)):
        a=tweepy.Cursor(api.get_friend_ids, source_id=following_list[i], target_id=target_id[j])
        print(a)
        break




following_list.append(celebrity.id)         #adding main user as well
df = pd.DataFrame(columns=['source','target'])
edges=[["source"],["target"]]
#Our goal, therefore, is to create an edge DataFrame of user IDs with 
#two columns: source and target. For each row, the target follows the source

for i in range(len(following_list)):
    for j in range(i+1,len(following_list)):
        a=api.get_friendship(source_id=following_list[i],target_id=following_list[j])
        if a[0].following:  #will be True if j is follwing i
            edges.append([following_list[i],following_list[j]])            
        if a[1].following:    
            edges.append([following_list[i],following_list[j]])
        break
"""
df = pd.DataFrame(columns=['source','target']) #Empty DataFrame
df['target'] = follower_list[0] #Set the list of followers as the target column
df['source'] = 1210627806 #Set my user ID as the source 
"""
