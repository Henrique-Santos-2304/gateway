# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep

class MqttClient:
    
    def __init__(self):
        self.myMQTTClient = AWSIoTMQTTClient("agri_henri_0")
        self.__config()
        self.__start()
        

    def __config(self):
        try:
            self.myMQTTClient.configureEndpoint('a19mijesri84u2-ats.iot.us-east-1.amazonaws.com', 8883)
            self.myMQTTClient.configureCredentials("aws_iot/keys/amazon_ca.pem", "aws_iot/keys/private.pem.key", "aws_iot/keys/device.pem.crt")
            self.myMQTTClient.configureOfflinePublishQueueing(-1)  
            self.myMQTTClient.configureDrainingFrequency(2) 
            self.myMQTTClient.configureConnectDisconnectTimeout(10) 
            self.myMQTTClient.configureMQTTOperationTimeout(5)
        except Exception as error:
            print("Erro ao configurar broker mqtt")
            print(error)
            sleep(1)
            self.__config()
            
        
    def __start(self):
        try:
            self.myMQTTClient.connect()
        except Exception as error:
            print("Erro ao Conectar Broker Aws")
            print(error)
            sleep(1)
            self.__start()
        
    def get_client(self):
        if not self.myMQTTClient.connect:
            self.__start()
        return self.myMQTTClient

    
        
        
        

