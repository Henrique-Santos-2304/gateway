from connect_serial.utils.codes_buffer import COMMANDS

class SendNoise:
    
    def __init__(self, handle_bytes, serial_write):
        self.__serial_write = serial_write
        self.__handle_bytes = handle_bytes
        self.__cmd = COMMANDS.get("CMD_READNOISE")[0]
        
    async def start(self, radio_id) -> None:
        byte_response: bytearray = await self.__handle_bytes.start(self.__cmd, radio_id, [0])

        await self.__serial_write.start(byte_response)