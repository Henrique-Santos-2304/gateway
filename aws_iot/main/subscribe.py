from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from local_settings import SUB_TOPIC_OF_FARM, SUB_TOPIC_INITIAL_DATA
from aws_iot.utils.iot_codes import IDP_MESSAGES
from core.main.composers.init_data import init_data
from connect_serial.main.composers.use_cases import send_comands
import json
import asyncio

class AwsSubscribe:
    
    def __init__(self, client: AWSIoTMQTTClient, handler_messages):
        self.client = client
        self.handler_message = handler_messages
        
    def __cb_initial_data(self, client, userdata, message ):
        to_json_string = message.payload.decode("utf-8")
        
        if "404" in str(to_json_string):
            print("Fazenda não encontrada! Favor verifique o id da fazenda fornecido")
            return
        
        to_object = json.loads(to_json_string)
        init_data.dispatch(to_object)
        self.client.unsubscribe(SUB_TOPIC_INITIAL_DATA)

    def callback_subscribe(self, client, userdata, message):
        print(f"Nova mensagem recebida no tópico {SUB_TOPIC_OF_FARM} ")
        
        to_json_string = message.payload.decode("utf-8")
        print(str(to_json_string))
        asyncio.run(self.handler_message.handler(str(to_json_string))) 

            
    def start(self):
        try:
            self.client.subscribe(SUB_TOPIC_OF_FARM, 0, self.callback_subscribe)
            self.client.subscribe(SUB_TOPIC_INITIAL_DATA, 0, self.__cb_initial_data)
        except Exception as error:
            print("Erro no recebimento da mensagem ")
            print(error)
        
        
    
