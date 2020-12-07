import uuid
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
            print("este pentru obiectul asta")
            self.__messageTelemetry(self,identDevice[3],message)
        else:
            print("mesajul este pentru alt obiect")

    def __messageTelemetry(self,sensor,message):
        #identDevice = topic.split("/")
        print("Mesajul:",message)
        pass
    
