import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
import threading
# Create two queues
choice = 0

name = sys.argv[1]
video_name = " ".join(sys.argv[2:])
choice=1

result = channel.queue_declare('navvrat', exclusive=False)
queue_name = result.method.queue
channel.exchange_declare(exchange='topic_updates', exchange_type='topic')
channel.queue_bind(exchange='topic_updates', queue=queue_name, routing_key=name)


# Define an exchange
channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

# Bind queues to the exchange with routing keys
channel.queue_bind(exchange='direct_exchange', queue='component1_queue', routing_key='component1')
channel.queue_bind(exchange='direct_exchange', queue='component2_queue', routing_key='component2')




if choice==1:

        channel.basic_publish(exchange='direct_exchange', routing_key='component2', body=f"youtuber {name} {video_name}")

def consume(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    
    def callback(ch, method, properties, body):
        print(body.decode())
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


thread1 = threading.Thread(target=consume, args=(queue_name,))
thread1.start()