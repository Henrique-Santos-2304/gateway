from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import aws_iot.main.composers.mqtt_client as client
from connect_serial.main.composers.use_cases import send_comands
import json
import asyncio

class AwsProducer:
    
    def __init__(self, client: AWSIoTMQTTClient):
        self.client = client

            
    def start(self, topic: str, msg: str):
        try:
            self.client.publish(topic=topic, payload=msg, QoS=0)
        except:
            print("Erro ao publicar ack...")
        
    
