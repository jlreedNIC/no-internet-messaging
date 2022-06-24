# weird install path for python
import sys
sys.path.append("/home/jreed/.local/lib/python3.7/site-packages")
import time
import datetime

print("Starting messaging program...")

try:
    import paho.mqtt.client as paho
    from paho import mqtt
except Exception as e:
    # print(f"error with import: {e}")
    print("Error: please install 'paho.mqtt.client' module.")
else:
    print("paho module is installed.")

message_queue = []

# callbacks

def on_connect(client, userdata, flags, rc, properties=None) :
    print(f"CONNACK received with code {rc}")

def on_subscribe(client, userdata, mid, granted_qos, properties=None) :
    print(f'Subscribed: {mid} {granted_qos}')

def on_publish(client, userdata, mid, properties=None) :
    print(f'mid: {mid}')

def on_message(client, userdata, msg) :
    # print("message received")
    # print(f"topic: {msg.topic} message:\n{msg.payload}")
    timestamp = datetime.datetime.now()
    message_string = msg.payload.decode("ascii")
    temp_message = [message_string, timestamp]
    message_queue.append(temp_message)

    print_messages()
    print_instr()

def on_disconnect(client, userdata, rc, properties=None) :
    if rc == paho.MQTT_ERR_SUCCESS  :
        print("Disconnected successfully")
    else :
        print("Unexpected disconnect")

# ---------- connecting

def connect_local_MQTT() :
    print("start connecting")
    client_id = "jordan's laptop" # put in config file
    localMQTT = paho.Client(client_id)

    # set up call backs
    localMQTT.on_connect = on_connect
    ip_addr = "192.168.1.11"
    port = 1883
    # connect
    localMQTT.connect(host=ip_addr, port=port)

    # more callbacks
    localMQTT.on_message = on_message
    localMQTT.on_subscribe = on_subscribe
    localMQTT.on_disconnect = on_disconnect
    localMQTT.on_publish = on_publish

    return localMQTT    

def publishMessage(topic, message) :
    print("starting to publish")
    # client = connect_local_MQTT()

    # client.loop_start()
    clientname = client._client_id
    clientname = clientname.decode(("ascii"))
    new_msg = f"{clientname}: {message}"
    client.publish(topic, new_msg, qos=1)

    # client.loop_stop()

    # client.disconnect()


# client = connect_local_MQTT()

# -- loop --
# client.subscribe('#', qos=1)

# for i in range(4) :
#     timestamp = datetime.datetime.now()
#     message = f"test message {i} sent at {timestamp:%H:%M:%S}"
#     publishMessage("test", message)
#     time.sleep(5)
def print_messages() :
    global message_queue
    size = len(message_queue)
    print(size)
    # clear screen?
    print("-----messages------")
    for i in range(size) :
        # print(i)
        # print(message_queue[i])
        if i > 0 and message_queue[i][1].day == message_queue[i-1][1].day and message_queue[i][1].month == message_queue[i-1][1].month :
            print("      ", end="")
        else:
            print(f"{message_queue[i][1]:%m/%d} ", end="")

        print(f"{message_queue[i][1]:%H:%M:%S} ", end="")

        print(f"{message_queue[i][0]}") # maybe put into dictionary format??
    
    print("-----messages------")

def print_instr() :
    print("\nWhat would you like to do?")
    print(" (1) Send message \n (0) Exit \n")

client = connect_local_MQTT()
client.subscribe("#")

client.loop_start()
answer = True
print_instr()
while answer :
    
    # print_messages()
    

    choice = input()
    if choice == "0":
        answer = False
        client.disconnect()
    elif choice == "1" :
        print("starting publish")
        timestamp = datetime.datetime.now()
        message = f"test message sent at {timestamp:%H:%M:%S}"
        publishMessage("test", message)

client.loop_stop()
    