import paho.mqtt.client as mqtt
import settings
host = settings.IP_ADDRESS
port = settings.PORT
client = mqtt.Client()
client.connect(host, port)
client.publish("room","shout mqtt")
