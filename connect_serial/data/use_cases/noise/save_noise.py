import aws_iot.main.composers.mqtt_client as iot

from aws_iot.utils.iot_codes import IDP_MESSAGES
import local_settings


class SaveNoise:

    def __init__(self):
        self.radio_id: None
        
        
    def __split_noise_response(self, noise_response: bytes) -> float:
        try:

            array_int = [int(x) for x in noise_response]
            self.radio_id = array_int[0]
            noise_cmd = array_int[2]
            noise_min = float(array_int[3])  # noise mín
            noise_max = float(array_int[5])  # noise max
            media_noise = float(array_int[4])

            return media_noise

        except Exception as error:
            message = "Erro ao separar Bytes response em array rssi"
            print(message)
            print(error)

    async def start(self, payload: bytes):
        media_noise = self.__split_noise_response(payload)
        
        idp = IDP_MESSAGES["noise"]
        pivot_id = f"{local_settings.FARM_ID}_{self.radio_id}"
        message = "#" + f"{idp}-{pivot_id}-{media_noise}$"
        iot.mqtt_publisher.start(local_settings.AWS_TOPIC_GATEWAY, message)
        