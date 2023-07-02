import aws_iot.main.composers.mqtt_client as iot

from aws_iot.utils.iot_codes import IDP_MESSAGES
import local_settings

class SaveTraceRoute:

    def __init__(self):
        self.radio_id = None

    def __turns_response_into_father(self, list_num) -> str:
        try:
            ''' save bytes into list and converto to int'''
            cmd_type = list_num[2]
            self.radio_id = list_num[0]
            ''' separate filter some routes of the list '''
            without_id_crc = list_num[3:-2]

            ''' Organize the list into a groups of 2, Origin and destiny'''
            list_of_groups = list(zip(*(iter(without_id_crc),) * 2))
            list_of_groups.reverse()
            len_list = len(list_of_groups) - 1

            ''' Mount response to string'''
            string_list = ''
            for i, v in enumerate(list_of_groups):
                if i == 0:
                    string_list += f"{v[1]}, {v[0]}, "
                elif i != len_list:
                    string_list += f"{v[0]}, "
                else:
                    string_list += f"{v[0]}"

            return string_list
        except Exception as error:
            message = "Erro ao separar Bytes response em array rssi"
            print(message)
            print(error)

    async def start(self, message_serial):
        response_string = self.__turns_response_into_father(message_serial)
        
        idp = IDP_MESSAGES["trace_route"]
        pivot_id = f"{local_settings.FARM_ID}_{self.radio_id}"
        message = "#" + f"{idp}-{pivot_id}-{response_string}$"
        iot.mqtt_publisher.start(local_settings.AWS_TOPIC_GATEWAY, message)
