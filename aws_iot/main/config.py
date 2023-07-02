# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from local_settings import AWS_CA, AWS_PORT, AWS_URL, AWS_KEY,AWS_CRT, CLIENT_ID
from time import sleep

class MqttClient:
    
    def __init__(self):
        self.myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
        self.__config()
        self.__start()
        

    def __config(self):
        try:
            self.myMQTTClient.configureEndpoint(AWS_URL, AWS_PORT)
            self.myMQTTClient.configureCredentials(AWS_CA, AWS_KEY , AWS_CRT)
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

    
        
        
        

