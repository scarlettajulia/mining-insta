from InstagramAPI import InstagramAPI
import time
import json
from datetime import datetime

username = ''
pwd = ''
user_id  = ''

level = 3;

API = InstagramAPI(username,pwd)
API.login()

API.getUsernameInfo(user_id)
API.LastJson
follower  = []
next_max_id = True
while next_max_id:
    print next_max_id
    #first iteration hack
    if next_max_id == True: next_max_id=''
    _ = API.getUserFollowers('4133879197',maxid=next_max_id)
    follower.extend ( API.LastJson.get('users',[]))
    next_max_id = API.LastJson.get('next_max_id','')

for f in follower:
	print f['username']

len(follower)
unique_follower= {
    f['pk'] : f
    for f in follower
}
len(unique_follower)

with open('follower.txt', 'w') as outfile:
    json.dump(unique_follower, outfile)

#outfile = open('follower.txt', 'w')
