from connect_serial.utils.codes_buffer import COMMANDS

class SendTraceRoute:
    
    def __init__(self, handle_bytes, serial_write):
        self.__serial_write = serial_write
        self.__handle_bytes = handle_bytes
        self.__cmd = COMMANDS.get("CMD_TRACEROUTE")[0]
        
    async def start(self, message: str) -> None:
        [idp, radio_id] = message.split('-')
        byte_response: bytearray = await self.handle_bytes.start(self.cmd, radio_id, [0])

        await self.__serial_write.start(byte_response)