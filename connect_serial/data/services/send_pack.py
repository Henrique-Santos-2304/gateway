from typing import List, Union
from connect_serial.utils.get_date import get_date_now
from connect_serial.utils.codes_buffer import MAX_BUFFER_SIZE, COMMANDS
from connect_serial.utils.calc_crc import crc


class SendPackage:
    buffer = [None] * MAX_BUFFER_SIZE

    def __init__(self) -> None:
        self.send: bytearray = None
        self.cmd: int = None
        self.radio_id: int = None
        self.msg: List[int] = None

    async def __create_array_byte(self,  rest_date: list = []) -> None:
        id_lsb = int(self.radio_id) % 256
        id_msb = int(self.radio_id) / 256
        self.send: bytearray = None
        self.send = bytearray([int(id_lsb), int(id_msb), self.cmd])
        [self.send.append(int(x)) for x in self.msg]


        if rest_date and len(rest_date)> 0:
            for x in rest_date:
                if x == 'x00':
                    self.send.append(0)

        crc_calc = crc((self.send), len(self.send))
        # separa o CRC calculado em byte LSB #print(crc_lsb)
        crc_lsb = crc_calc % 256
        # separa o CRC calculado em byte MSB
        crc_msb = int(crc_calc / 256) & 0xFF
        self.send.append(int(crc_lsb))
        self.send.append(int(crc_msb))

    def __print_message_with_cmd(self) -> None:
        if self.cmd in COMMANDS.get('CMD_READNOISE'):
            print(f"{get_date_now()} -> Pedindo SNR para: radio_{self.radio_id}")

        elif self.cmd in COMMANDS.get('CMD_READRSSI'):
            print(f"{get_date_now()} -> Pedindo RSSI para: radio_{self.radio_id}")

        elif self.cmd in COMMANDS.get('CMD_TRACEROUTE'):
            print(f"{get_date_now()} -> Tracando rota de: radio_{self.radio_id}")
            
        elif self.cmd in COMMANDS.get('CMD_READGPRS'):
            print(f"{get_date_now()} -> Enviando Gprs para o  radio_{self.radio_id}")

        elif self.cmd in COMMANDS.get('CMD_SENDTRANSP'):
            txt_send = str(list(map(lambda y: chr(y), self.msg)))
            print(
                f"{get_date_now()} -> Enviando Pacotes de dados para o radio_{self.radio_id}")

        elif self.cmd in COMMANDS.get('CMD_TRACEROUTE'):
            print(
                f"{get_date_now()} -> Traçando rota para o radio_{self.radio_id}")

        else:
            print(
                f"{get_date_now()} -> Comando {self.cmd} Inválido para o radio_{self.radio_id} ")

    def __config_params(self, cmd: int, request_id: int, msg: List[int]) -> None:
        self.cmd = cmd
        self.radio_id = request_id
        self.msg = msg

    def __reset_params(self) -> None:
        self.cmd = None
        self.radio_id = None
        self.msg = None

    async def start(self, cmd: int, request_id: int, msg: List[int], rest_date: list = []) -> Union[None, bytearray]:
        try:
            self.__config_params(cmd, request_id, msg)
            await self.__create_array_byte(rest_date)

            if self.send and len(self.send) > 0:
                self.__print_message_with_cmd()
                return self.send
            else:
                raise Exception("Não foi possíveis criar bytes")
        except Exception as error:
            message = "Error ao criar Bytes..."
            print(f"{get_date_now()} -> {message}")
            print(error)
            raise Exception("Error to create byte array")
        finally:
            self.__reset_params()
