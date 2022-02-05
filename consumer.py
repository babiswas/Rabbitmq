import pika, sys, os


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
def callback(ch, method, properties, body):
   print(f"{body}")
channel.basic_consume(queue='notify', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()