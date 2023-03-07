import redis
from datetime import datetime
import json
from threading import Thread

r = redis.Redis(host="localhost",port=6379,db=0)

def Pub():
    print("publisher")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    temp  = [{'current_time':current_time},{'place':"Patna"},{"Status":"Pending"}]
    time = json.dumps(temp)
    r.publish("channel",time)


def Sub():
    print("Subscriber")
    p = r.pubsub()
    p.subscribe("channel")
    flag=1
    # count=0
    while flag:
        # print(count)
        # count=count+1
        msg = p.get_message()
        if msg:
            if type(msg['data'])!=type(1):
                received_data = json.loads(msg['data'])
                print(received_data)
                flag=0
        
# creating threads for pub and sub
t1 = Thread(target=Sub)
t2 = Thread(target=Pub)

# starting the threads
t1.start()
t2.start()

# waiting for both threads to join
t1.join()
t2.join()

print("exiting main thread")

