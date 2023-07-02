from datetime import datetime
from connect_serial.utils.codes_buffer import COMMANDS
from connect_serial.utils.get_date import get_date_now

class SendRssi:
    def __init__(self, handle_bytes, serial_write):
        self.__serial_write = serial_write
        self.__handle_bytes = handle_bytes
        self.__cmd = COMMANDS.get("CMD_READRSSI")[0]

    async def __write_serial(self, byt: bytearray) -> None:
        try:
            await self.__serial_write.start(byt)
        except Exception as error:
            message = "Erro ao gravar na porta serial..."
            print(f"{get_date_now()} -> {message}")
            print(error)

    async def start(self, radio_id) -> None:
        byte_response: bytearray = await self.__handle_bytes.start(self.__cmd, radio_id, [0])
        await self.__write_serial(byte_response)
        
