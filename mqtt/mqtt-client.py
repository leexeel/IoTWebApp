import paho.mqtt.client as mqtt
import time
#from iotDevice import iotDevice
import uuid

deviceList = []

class iotDevice:
    
    def __init__(self,deviceID,sensors,deviceIP,mqttClient):
        self.mqttClient = mqttClient
        self.deviceID = deviceID
        self.sensors = sensors
        self.deviceIP = deviceIP
        self.baseTopicConf = "events/"+deviceID
        self.sensorsList = []
        self.__setSensorID()
        self.setTelemetryTopic()
        self.__configDeviceTelemetry()
    
    def __setSensorID(self):
        count = 1
        while count <= self.sensors:
            tempSensorId = self.deviceID + str(self.sensors) + str(count)
            sensorUUID = uuid.uuid5(uuid.NAMESPACE_DNS,tempSensorId)
            self.sensorsList.append(str(sensorUUID))
            count = count+1

    def setTelemetryTopic(self):
        for sensor in enumerate(self.sensorsList):
            telemetryTopic = "values/" + self.deviceID + "/telemetry/" + sensor[1]
            #print(telemetryTopic)
            self.mqttClient.subscribe(telemetryTopic)
            
    def __configDeviceTelemetry(self):
        configString = "Config|"
        for sensor in enumerate(self.sensorsList):
            configString = configString + sensor[1] + "|"
        configString = configString + "end"
        self.mqttClient.publish(self.baseTopicConf,configString)
    
    def procMessage(self,topic,message):
        print("In obiect am primit mesajul:",message," pe topicul:",topic)
        identDevice = topic.split("/")
        if self.deviceID == identDevice[1]:
            print("este pentru obiectul asta",identDevice[1]," ",identDevice[3])
            self.messageTelemetry(self,identDevice[3],message)
        else:
            print("mesajul este pentru alt obiect")

    def messageTelemetry(self,sensor,message):
        #identDevice = topic.split("/")
        print("Mesajul:",message)


############
def on_message(client, userdata, message):
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
    else:
        #print("message topic=",message.topic.encode('ascii', 'ignore'),"value=",str(message.payload.decode("utf-8")))
        for device in enumerate(deviceList):
            print("**************:",device," ",device[1])
            device[1].procMessage(message.topic.encode('ascii', 'ignore'),str(message.payload.decode("utf-8")))

def on_publish(client,userdata,result):             #create function for callback
    #print("data published \n")
    pass
########################################
broker_address="192.168.10.66"
print("creating new instance")
mqttClient = mqtt.Client("ProcClients") #create new instance
mqttClient.on_message=on_message #attach function to callback
print("connecting to broker")
mqttClient.connect(broker_address) #connect to broker
mqttClient.subscribe("events/join")
mqttClient.on_publish = on_publish
mqttClient.loop_forever() #start the loop
