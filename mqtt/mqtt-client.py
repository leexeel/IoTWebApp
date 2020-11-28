import paho.mqtt.client as mqtt
import time

deviceList = []

############
def on_message(client, userdata, message):
    #print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic.encode('ascii', 'ignore'),"value=",str(message.payload.decode("utf-8")))
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
    if message.topic.encode('ascii', 'ignore') == "events/join":
        print(str(message.payload.decode("utf-8")))
        deviceParameters=str(message.payload.decode("utf-8")).split('|')
        deviceList.append(deviceParameters[0])
        pubThread = "events/" + deviceParameters[0]
        print("Comunicam pe topicul:",pubThread)
        welcomeString = "Bine ai venit"
        client.publish(pubThread,welcomeString)
        print("Lista este:",deviceList)

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
########################################
broker_address="192.168.10.66"

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","values/temperature")
client.subscribe("values/temperature")
print("Subscribing to topic","values/humidity")
client.subscribe("values/humidity")
print("Subscribing to topic","events/join")
client.subscribe("events/join")
client.on_publish = on_publish
client.loop_forever() #start the loop
