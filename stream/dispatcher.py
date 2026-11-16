import pika
import json
import random
import time

cities = ["bangalore", "chennai"]
zones_map = {
    "bangalore": ["koramangala", "indiranagar", "whitefield"],
    "chennai": ["tnagar", "adyar", "velachery"]
}
types = ["ride", "food"]

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='rapido-dispatch', exchange_type='topic')

print("Dispatcher started. Publishing messages...")
try:
    msg_id = 1
    while True:
        city = random.choice(cities)
        zone = random.choice(zones_map[city])
        order_type = random.choice(types)

        routing_key = f"{city}.{zone}.{order_type}"
        message = {
            "id": msg_id,
            "city": city,
            "zone": zone,
            "type": order_type,
            "ts": time.time()
        }

        channel.basic_publish(
            exchange='rapido-dispatch',
            routing_key=routing_key,
            body=json.dumps(message)
        )
        print(f"Dispatched [Key: {routing_key}]: {message}")

        msg_id += 1
        time.sleep(2)
except KeyboardInterrupt:
    connection.close()