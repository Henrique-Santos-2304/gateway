from time import sleep
from typing import Generic, TypeVar, Union
from connect_serial.utils.get_date import get_date_now

T = TypeVar("T")


class WriteDataSerial:

    def __init__(self, serial: any, serial_check: any) -> None:
        self.serial = serial
        self.serial_check = serial_check
        self.read_is_empty = False
        self.actions_writes = []

    async def start(self, data: Generic[T]) -> any:
        try:
            await self.serial_check.check()
            
            if not self.serial:
                print("Nenhuma conexão serial aberta")
                return
            
            self.serial.reset_input_buffer()
            print(
                f"\n{get_date_now()} -> Gravando dados na porta serial... \n{data}")

            self.serial.write(data)
            print("Dados gravados com sucesso....\n")

        except Exception as error:
            print(f"{get_date_now()} -> Erro na gravação de dados  Serial")
            print(f"{error} \n")
