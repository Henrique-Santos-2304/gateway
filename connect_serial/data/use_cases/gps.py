from connect_serial.utils.get_date import get_date_now
from connect_serial.utils.codes_buffer import COMMANDS


class ResponseGps:

    def __init__(self, handle_bytes, serial_write, send_comands):
        self.cmd = COMMANDS.get("CMD_SENDTRANSP")[0]
        self.__serial_write = serial_write
        self.__handle_bytes = handle_bytes
        self.send_gps_comand = send_comands
        self.radio_id = None
        self.response_msg_checking = ''

    async def __write_serial(self, bytes_received: bytearray) -> None:
        try:
            await self.__serial_write.start(bytes_received)
        except Exception as error:
            print(f"{get_date_now()} -> Erro ao gravar na porta serial")
            print(error)
            
    async def __mount_response(self, value: list) -> None:
        self.radio_id = value[0] - 100
        list_to_bytes = bytes(value)

        [radio_data, payload_received] = str(list_to_bytes).split('#')
        [gps_data, timestamp_with_crc] = payload_received.split('-')
        [timestamp, crcs] = timestamp_with_crc.split('$')
        [gps_text, gps_value] = gps_data.split("GPS")

        self.response_msg_checking = f"#GPS{float(gps_value)}-{timestamp}$"
        
    async def start_send(self):
        send_msg = trasnform_data_to_ordinal(self.response_msg_checking)

        byte_received: bytearray = await self.__infra.start(self.cmd, self.radio_id, send_msg)

        await self.__write_serial(byte_received)
        
    async def start(self, data: bytes):
        await self.__mount_response(data)
        print(f"Gravando Status GPS recebido -> {self.response_msg_checking}")
        await self.start_send()
