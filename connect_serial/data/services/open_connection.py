from typing import Union
from connect_serial.utils.get_date import get_date_now


class OpenConnection:

    def __init__(self, serial) -> None:
        self.serial = serial

    async def open(self) -> any:
        try:
            print(f"{get_date_now()} -> Tentando abrir conexão serial")
            is_open = self.serial.isOpen()

            if is_open is False:
                self.serial.open()
                print(f"Comunicação Serial Aberta")
            else:
                print(f"Comunicação Serial já estava Aberta")

            print("...")
            return True
        except Exception as error:
            message = "Erro ao tentar abrir conexão serial"
            print(f"{get_date_now()} -> {message} ")
            print(f"{error} \n")
