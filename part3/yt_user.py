import pika
import threading
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

choice = 0

name = sys.argv[1]
if len(sys.argv) == 2:
    choice=3
elif len(sys.argv) == 4:
    action = sys.argv[2]
    if action=="s":
        youtuber_name = sys.argv[3]
        choice=1
    elif action=="u":
        youtuber_name = sys.argv[3]
        choice=2
else:
    print("Invalid number of arguments.")



# Create two queues
channel.queue_declare(queue='component1_queue')
channel.queue_declare(queue='component2_queue')
channel.queue_declare(queue='component3_queue')
# Define an exchange
channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')
result = channel.queue_declare('pavit', exclusive=False)
queue_name = result.method.queue
channel.exchange_declare(exchange='topic_updates', exchange_type='topic')
channel.queue_bind(exchange='topic_updates', queue=queue_name, routing_key=name)

def consume(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    
    def callback(ch, method, properties, body):
        print("New Notification "+body.decode())
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


thread1 = threading.Thread(target=consume, args=(queue_name,))
thread1.start()




if choice==1:

    channel.basic_publish(exchange='direct_exchange', routing_key='component3', body=f"user {name} subscribe {youtuber_name}")
elif choice==2:

    channel.basic_publish(exchange='direct_exchange', routing_key='component3', body=f"user {name} unsubscribe {youtuber_name}")

elif choice==3:
    channel.basic_publish(exchange='direct_exchange', routing_key='component3', body=f"login from user {name}")



