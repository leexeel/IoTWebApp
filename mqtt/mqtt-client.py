import paho.mqtt.client as mqtt
import time
from iotDevice import iotDevice

deviceList = []

############
def on_message(client, userdata, message):
    print("message topic=",message.topic.encode('ascii', 'ignore'),"value=",str(message.payload.decode("utf-8")))
    if message.topic.encode('ascii', 'ignore') == "events/join":
        #print(str(message.payload.decode("utf-8")))
        deviceParameters=str(message.payload.decode("utf-8")).split('|')
        deviceObj = iotDevice(deviceParameters[0],int(deviceParameters[1]),deviceParameters[2],mqttClient)
        deviceList.append(deviceObj)
        pubThread = "events/" + deviceParameters[0]
        welcomeString = "Welcome device "+deviceObj.deviceID+" from "+deviceObj.deviceIP
        mqttClient.publish(pubThread,welcomeString)
        mqttClient.subscribe(pubThread)
        print("Lista este:",deviceList)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
########################################
broker_address="192.168.10.66"

print("creating new instance")
mqttClient = mqtt.Client("ProcClients") #create new instance
mqttClient.on_message=on_message #attach function to callback
print("connecting to broker")
mqttClient.connect(broker_address) #connect to broker
print("Subscribing to topic","values/temperature")
mqttClient.subscribe("values/temperature")
print("Subscribing to topic","values/humidity")
mqttClient.subscribe("values/humidity")
print("Subscribing to topic","events/join")
mqttClient.subscribe("events/join")
mqttClient.on_publish = on_publish
mqttClient.loop_forever() #start the loop
