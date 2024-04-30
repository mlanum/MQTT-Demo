import random
import time

import paho.mqtt.client as mqtt

# TCP Connection Parameters
broker = 'localhost'
port = 1883
topic = 'python/mqtt_demo'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'my_user'
# password = 'admin'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected with result code ' + str(rc))
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt.Client(client_id=client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"my counter: {msg_count}"
        result = client.publish(topic, msg, qos=1)
        # result = [0,1]
        status = result[0]
        if status ==0:
            print(f"Sent '{msg}' to topic '{topic}'")
        else:
            print(f"Failed to send message to topic '{topic}'")
        msg_count += 1
        if msg_count > 10:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()
