import json

f = open('follower.txt', 'r')
x = f.read().split('\n')

print x

a = 'a'
data = {}
json_data = json.dumps(data)
data[a] = ['b', 'c', 'd']

print data