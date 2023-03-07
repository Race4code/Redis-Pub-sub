import json
import redis
from datetime import datetime
import time
from multiprocessing import Process
r = redis.Redis(host="localhost",port=6379,db=0)

def Pub():
    print("Publisher")
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
    while flag:
        msg = p.get_message()
        if msg:
            if type(msg['data'])!=type(1):
                received_data = json.loads(msg['data'])
                print(received_data)
                flag=0


if __name__ == "__main__":
    # creating two different process for pub and sub
    p1 = Process(target=Sub)
    p2 = Process(target=Pub)
    
    # starting sub and pub
    p1.start()
    time.sleep(1)
    p2.start()
    
    
    # wait till join
    p1.join()
    p2.join()
    
    print("exiting the main process")