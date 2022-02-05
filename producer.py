import pika
import json
import requests

def task():
  connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
  channel=connection.channel()
  data=requests.get("http://127.0.0.1:5000/api/alltest/1")
  mydata=data.json()
  while mydata:
     chunk=mydata.pop()
     channel.basic_publish(exchange='order',routing_key='order.notify',body=chunk["resourcePath"])
     print("Sent a message to the exchange")
  connection.close()

if __name__=="__main__":
   task()

  
