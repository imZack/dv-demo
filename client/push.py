#!/usr/bin/python

from influxdb import InfluxDBClient
from datetime import datetime
from random import randint
import socket
from time import sleep


def generate_data(value):
    return [
        {
            "measurement": "watt",
            "tags": {
                "host": socket.gethostname(),
            },
            "time": datetime.utcnow().isoformat(),
            "fields": {
                "value": float(value)
            }
        }
    ]

client = InfluxDBClient('192.168.1.4', 8086, 'root', 'root', 'thingspro')

while True:
    client.write_points(generate_data(randint(0, 9)))
    sleep(1)
    print (".")

# result = client.query('select value from watt;')

# print ("Result: {0}".format(result))
