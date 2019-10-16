import paho.mqtt.client as mqtt
import settings
host = settings.IP_ADDRESS
port = settings.PORT

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected.")
    print("Connected with result code "+str(rc))
    client.subscribe("room")

def on_message(client, userdata, msg):
    print(msg.payload.decode("utf-8", "strict"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port)
client.loop_forever()

