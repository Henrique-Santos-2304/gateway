import aws_iot.main.composers.mqtt_client as iot

from aws_iot.utils.iot_codes import IDP_MESSAGES
import local_settings

class SaveRssi:

    def __init__(self):
        self.radio_id = None
        

    def __split_rssi_response(self, rssi_response: bytes) -> float:
        try:
            '''Pega o index do cmd + 3, porque depois do cmd vem gateway1 e gateway2 e os rssi vem depois disso'''
            num_crcs = 6
            cmd_index = 2
            self.radio_id = rssi_response[0]

            array_int = [int(x) for x in rssi_response]
            id_cmd_and_gat = array_int[0:cmd_index]
            rssis = array_int[cmd_index:-num_crcs]

            

            media_rssi = sum(rssis) / len(rssis)
            return float(media_rssi)
        except Exception as error:
            message = "Erro ao separar Bytes response em array rssi"
            print(message)
            print(error)

    async def start(self, payload: bytes):
        media_rssi = self.__split_rssi_response(payload)
        
        idp = IDP_MESSAGES["rssi"]
        pivot_id = f"{local_settings.FARM_ID}_{self.radio_id}"
        message = "#" + f"{idp}-{pivot_id}-{media_rssi}$"
        iot.mqtt_publisher.start(local_settings.AWS_TOPIC_GATEWAY, message)
