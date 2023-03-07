import redis 
import json

r = redis.Redis(host="localhost",port=6379,db=0)

p = r.pubsub()

# subscribing to a particular channel
p.subscribe("channel")

# creating an infinite loop to listen for publisher message
while True:
    # getting the message in msg variable
    msg = p.get_message()
    if msg:
        
        # checking if the type of data is int or not (for converting the msg['data'] back to the original type)
        if type(msg['data'])!=type(1):
            received_data = json.loads(msg['data'])
            print(received_data)
        