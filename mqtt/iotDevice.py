import uuid

class iotDevice:

    def __init__(self,deviceId,sensors,deviceIP):
        self.deviceId = deviceID
        self.sensors = sensors
        self.deviceIP = deviceIP
        self.__baseTopicConf = "events/"
        self.__baseTopicJoin = "events/join"
        self.__baseTopicValues = "values/"
        self.sensorsList = []
    
    def setSensorID(self,sensorIndex,sensorUUID):
        self.sensorsList.append[sensorUUID]
    
    def getTopicConf():
        return baseTopicConf+self.deviceID
    
    def getSensorID(sensorIndex):
        return  self.sensorsList[sensorIndex]
    
    def __setSensorID(self):
        for count in range(int(self.deviceParameters[1])):
            sensorId = self.deviceParameters[0]+self.deviceParameters[2]+str(count)
            sensorUUID = uuid.uuid5(uuid.NAMESPACE_DNS,sensorId)
            self.sensorsList.append(sensorUUID)