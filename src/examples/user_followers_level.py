from InstagramAPI import InstagramAPI
import time
import json

level =  0;
queue_of_user = [('484345208','ramosj_noah')]
list_of_added_user = []

outfile = open('follower_level.txt', 'w')
userlist_outfile = open('all_userid.txt', 'w')

def getFollowerFromUser(userId):
	follower_json = []
	follower = []
	next_max_id = True
	while next_max_id:
	    #first iteration hack
	    if next_max_id == True: next_max_id=''
	    time.sleep(5)
	    _ = API.getUserFollowers(userId,maxid=next_max_id)
	    follower_json.extend ( API.LastJson.get('users',[]))
	    next_max_id = API.LastJson.get('next_max_id','')
	for f in follower_json:
		follower.append(f['username'])
		#print f['username']
		if ((f['pk'], f['username']) not in queue_of_user) and (f['username'] not in list_of_added_user):
			queue_of_user.append((f['pk'], f['username']))
	return follower

username = ''
pwd = ''
user_id  = ''

API = InstagramAPI(username,pwd)
API.login()

API.getUsernameInfo(user_id)
API.LastJson

while level<3:
	print level
	copy_of_queue = list(queue_of_user)
	#print copy_of_queue
	for (userid, username) in copy_of_queue:
		#print user
		if username not in list_of_added_user:
			follower = getFollowerFromUser(userid)
			list_of_added_user.append(username)
			userlist_outfile.write("%s\n" % username)
			outfile.write("%s" % username)
			outfile.write(":")
			outfile.write("\n")
			for f in follower:
				outfile.write("%s\n" % f)
				if ((level == 2) and (f not in list_of_added_user)):
					userlist_outfile.write("%s\n" % f)
		queue_of_user.remove((userid, username))
	level = level + 1
