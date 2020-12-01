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
            telemetryTopic = self.baseTopicConf + "/telemetry/" + sensor[1]
            self.mqttClient.subscribe(telemetryTopic)
            
    def __configDeviceTelemetry(self):
        configString = "Config|"
        for sensor in enumerate(self.sensorsList):
            configString = configString + sensor[1] + "|"
        self.mqttClient.publish(self.baseTopicConf,configString)