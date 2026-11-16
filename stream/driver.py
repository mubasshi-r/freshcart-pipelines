import pika
import json
import sys

if len(sys.argv) < 3:
    print("Usage: python driver.py <DRIVER_NAME> <BINDING_PATTERN>")
    sys.exit(1)

driver_name = sys.argv[1]
binding_pattern = sys.argv[2]

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='rapido-dispatch', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='rapido-dispatch', queue=queue_name, routing_key=binding_pattern)

print(f"Driver {driver_name} waiting for messages with pattern '{binding_pattern}'...")

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"[{driver_name}] Received request {data} on key '{method.routing_key}'")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
channel.start_consuming()