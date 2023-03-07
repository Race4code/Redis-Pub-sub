import redis 
import json
from datetime import datetime

# creating an instance of redis
r = redis.Redis(host="localhost",port=6379,db=0)

print("publisger")
# Creating message to be publish on channel
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
temp  = [{'current_time':current_time},{'place':"Patna"},{"Status":"Pending"}]

# converting the list of dict into json
time = json.dumps(temp)

# publishing the message
r.publish("channel",time)