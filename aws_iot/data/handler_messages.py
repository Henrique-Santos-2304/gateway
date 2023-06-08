from aws_iot.utils.iot_codes import IDP_MESSAGES
from aws_iot.main.producer import AwsProducer
from connect_serial.utils.get_date import get_date_now
from connect_serial.main.composers.use_cases import  send_comands, send_noise, send_rssi, send_trace_route
import asyncio
import local_settings

class HandlerMessage:
    
    def __init__(self, publisher: AwsProducer):
        self.publisher = publisher
        
    def return_ack(self, msg: str) -> None:
        self.publisher.start(topic=local_settings.TOPIC_SEND, msg=msg)
        
    def print_message_received(self, type_msg: str) -> None:
        print(f"...              {get_date_now()}               ...")
        print(f"Nova mensagem recebida do tipo {type_msg} ")
    
    def send_ack(self, message: str, type: str) -> None:
        self.print_message_received(type)
        print(message)
        
        code = IDP_MESSAGES[type]
        
        if code == IDP_MESSAGES.get("comands"):
            [idp, pivot_num, status, percent, timestamp] = message.split('-')
            ack_message = f"{code}-{local_settings.FARM}_{pivot_num}-{timestamp}"
            self.return_ack(ack_message)
        else:
            ack_message = f"{code}-{local_settings.FARM}_{pivot_num}"
            self.return_ack(ack_message)
                     
    def start(self, message: str):
        [idp, pivot_num, rest] = message.split('-')
        
        if idp == IDP_MESSAGES.get("status"):
            self.send_ack(message=message, type="status")
            asyncio.run(send_comands.start(message))
        elif idp == IDP_MESSAGES.get("comands"):
            self.send_ack(message=message, type="comands")
            asyncio.run(send_comands.start(message))         
        elif idp == IDP_MESSAGES.get("rssi"):
            self.send_ack(message=message, type="rssi")
            asyncio.run(send_rssi.start(message))
        elif idp == IDP_MESSAGES.get("trace_route"):
            self.send_ack(message=message, type="trace_route")
            asyncio.run(send_trace_route.start(message))
        elif idp == IDP_MESSAGES.get("noise"):
            self.send_ack(message=message, type="noise")
            asyncio.run(send_noise.start(message))
        elif idp == IDP_MESSAGES.get("map"):
            self.send_ack(message=message, type="map") 
        else:
            print("Nenhum padrão encontrado")
        
        
        print("Ação finalizada.....")
        print()
        print()