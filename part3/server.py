import pika
import threading

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#youtuber to videolist
videos = {}
#user to youtuberlist
subscriptions = {}

# Create two queues
#component 1 is for youtuber outgoing requests
#component 2 is for youtuber incoming requests
#component 3 is for user incoming requests
channel.queue_declare(queue='component1_queue')
channel.queue_declare(queue='component2_queue')
channel.queue_declare(queue='component3_queue')

channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')
channel.exchange_declare(exchange='topic_updates', exchange_type='topic')
channel.queue_bind(exchange='direct_exchange', queue='component1_queue', routing_key='component1')
channel.queue_bind(exchange='direct_exchange', queue='component2_queue', routing_key='component2')
channel.queue_bind(exchange='direct_exchange', queue='component3_queue', routing_key='component3')


def notify(topic,message):
    for username in subscriptions:
        if topic in subscriptions[username]:
            topii=username
            channel.basic_publish(
            exchange='topic_updates',
            routing_key=topii,
            body=message)
    

def consume_user_requests(strlist):
    username=strlist[1]
    action=strlist[2]
    if(action=="subscribe"):
        youtuber=strlist[3]
        if username in subscriptions:
            subscriptions[username].append(youtuber)
        else:
            subscriptions[username]=[youtuber]
    elif(action=="unsubscribe"):
        youtuber=strlist[3]
        subscriptions[username].remove(youtuber)
    channel.basic_publish(
            exchange='topic_updates',
            routing_key=username,
            body="Successfully carried out request")




def consume_youtuber_requests(strlist):
    youtuber_name=strlist[1]
    video_name=" ".join(strlist[2:])
    if youtuber_name in videos:
        videos[youtuber_name].append(video_name)
    else:
        videos[youtuber_name]=[video_name]
    channel.basic_publish(
            exchange='topic_updates',
            routing_key=youtuber_name,
            body="New Video Uploaded Successfully")
    notify(youtuber_name,f"{youtuber_name} uploaded new video {video_name}")
    

def consume(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue=queue_name)
    

    def callback(ch, method, properties, body):
        print(body.decode())
        strlist=body.decode('utf-8').split()
        if strlist[0]=="user":
            consume_user_requests(strlist)
        elif strlist[0]=="youtuber":
            consume_youtuber_requests(strlist)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    

    channel.start_consuming()

# Start two concurrent consumers
#for youtuber
thread1 = threading.Thread(target=consume, args=('component2_queue',))
#for user
thread2 = threading.Thread(target=consume, args=('component3_queue',))
thread1.start()
thread2.start()
