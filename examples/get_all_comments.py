from InstagramAPI import InstagramAPI
import time
import json
from datetime import datetime, date

username = ''
pwd      = ''
media_id = ''

#stop conditions, the script will end when first of them will be true
until_date = date(2017, 8, 27)
count      = 1000


API = InstagramAPI(username,pwd)
API.login()
API.getUsernameInfo()
has_more_comments = True
max_id            = ''
comments          = []


while has_more_comments:
    _ = API.getMediaComments(media_id,max_id=max_id)
    #comments' page come from older to newer, lets preserve desc order in full list
    for c in reversed(API.LastJson['comments']):
        comments.append(c)
    has_more_comments = API.LastJson.get('has_more_comments',False)
    #evaluate stop conditions
    if count and len(comments)>=count:
        comments = comments[:count]
        #stop loop
        has_more_comments = False
        print "stopped by count"
    if until_date:
        older_comment = comments[-1]
        dt=datetime.utcfromtimestamp(older_comment.get('created_at_utc',0))
        #only check all records if the last is older than stop condition
        if dt.isoformat()<=until_date.isoformat():
            #keep comments after until_date
            comments = [
                c
                for c in comments
                if datetime.utcfromtimestamp(c.get('created_at_utc',0)).date() > until_date
            ]
            #stop loop
            has_more_comments = False
            print "stopped by until_date"
    #next page
    if has_more_comments:
        max_id = API.LastJson.get('next_max_id','')
        time.sleep(2)

with open('data.txt', 'w') as outfile:
    json.dump(comments, outfile)

