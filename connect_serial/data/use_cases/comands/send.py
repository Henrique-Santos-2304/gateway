from datetime import datetime
from typing import Type, Union
from connect_serial.utils.codes_buffer import COMMANDS
from connect_serial.utils.get_date import get_date_now
from connect_serial.utils.transform_data import trasnform_data_to_ordinal
from aws_iot.utils.iot_codes import IDP_MESSAGES


class SendComands:

    def __init__(self, handle_bytes, serial_write):
        self.__serial_write = serial_write
        
        self.__infra = handle_bytes
        self.__cmd = COMMANDS.get("CMD_SENDTRANSP")[0]
        self.__send_msg = None
        self.__radio_id: int = None
        self.__intention: str = None

    def __config_class_params(self, radio_id, msg:str) -> None:
        ''' Config params received from request in class params'''
        [status, percent, timestamp, user] = msg.split('-')
        self.author = user
        self.__radio_id = radio_id 
        self.idp = IDP_MESSAGES["comands"]
        # self.__intention = f"#1-{radio}-{status}-{percent}-{timestamp}$" # Novo padrão
        self.__intention = f"#{self.idp}-{'-'.join([status, percent, timestamp])}$"
        
    def __reset_params(self) -> None:
        ''' Reset class parasm from a None datas'''
        self.__radio_id = None
        self.__intention = None
        self.__send_msg = None

    async def __write_serial(self, bytes_received: bytearray) -> None:
        try:
            await self.__serial_write.start(bytes_received)
        except Exception as error:
            print(f"{get_date_now()} -> Erro ao gravar na porta serial")
            print(error)
            raise SerialError

    async def start(self,radio_id, msg: str) -> None:
        ''' Config parameters for data global in this class'''
        self.__config_class_params(radio_id, msg)

        self.__send_msg = trasnform_data_to_ordinal(self.__intention)

        byte_received: bytearray = await self.__infra.start(self.__cmd, self.__radio_id, self.__send_msg)

        await self.__write_serial(byte_received)

        self.__reset_params()

