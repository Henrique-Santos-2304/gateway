import aws_iot.main.composers.mqtt_client as iot
from aws_iot.utils.iot_codes import IDP_MESSAGES
import local_settings

class ResponseComand:

    def __init__(self):
        self.radio_id = None

    def __mount_response(self, value: list) -> list:
        # Verificar resposta e pegar o radio_id
        self.radio_id = value[0]
        list_to_bytes = bytes(value)
        print(str(list_to_bytes))
        payload_received = str(list_to_bytes).split('#')[1]
        
        payload_list = payload_received.split('$')[0].split('-')[1:]
        payload = '-'.join(payload_list)
        
        
        return payload
        

    def start(self, data: bytes):
        response = self.__mount_response(data)
        idp = IDP_MESSAGES["status"]
        pivot_id = f"{local_settings.FARM_ID}_{self.radio_id}"
        message = "#" + f"{idp}-{response}$"
        
        print(f"Dados computados com sucesso, Status recebido -> {message}")

        iot.mqtt_publisher.start(local_settings.NEW_AWS_CLOUD, message)
        