import time
from math import floor
import random
import json
from kafka import KafkaProducer
from faker import Faker

fake = Faker()

def get_tourist_detail():
    return {
        "name": fake.first_name(),
        "address": fake.address()
    }

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=json_serializer)

TOURISTS = 5
ARTS = 10

# while True:
for tourist in range(TOURISTS):
    publishableDataObject = get_tourist_detail()
    publishableDataObject["art"] = str(random.randint(1, ARTS))
    print(publishableDataObject)
    producer.send("messages", publishableDataObject) 
    time.sleep(10)