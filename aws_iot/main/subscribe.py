from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import asyncio

class AwsSubscribe:
    
    def __init__(self, client: AWSIoTMQTTClient):
        self.client = client

    def callback_subscribe(self, client, userdata, message):
        try:
            to_json_string = message.payload.decode("utf-8")
            print(to_json_string)

            asyncio.run(send_comands.start({"id": 1, "intention": to_json_string})) 
        except Exception as error:
            print("Erro ao tratar mensagem recebida")
            print(error)
            
    def start(self):
    
        self.client.subscribe("agrishow_0", 1, self.callback_subscribe)
        
    
