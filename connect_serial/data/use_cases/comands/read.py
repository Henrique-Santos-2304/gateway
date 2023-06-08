import local_settings
from aws_iot.main.composers.mqtt_client import mqtt_publisher

class ResponseComand:

    def __init__(self, publisher):
        self.radio_id = None
        self.response_msg_checking = ''

    def __mount_response(self, value: list) -> list:
        # Verificar resposta e pegar o radio_id
        self.radio_id = value[0]
        list_to_bytes = bytes(value)
        [radio_data, payload_received] = str(list_to_bytes).split('#')
        [payload, crcs] = payload_received.split('$')
        
        self.response_msg_checking = payload

    def start(self, data: bytes):
        farm = local_settings.FARM
        self.__mount_response(data)
        """ Salvar dados ou não no banco de dados """
        print(f"Dados computados com sucesso, Status recebido -> {self.response_msg_checking}")
        return {
            "pivot_id": f"{farm_id}_{self.radio_id}",
            "payload": self.response_msg_checking.replace("'", ""),
        }