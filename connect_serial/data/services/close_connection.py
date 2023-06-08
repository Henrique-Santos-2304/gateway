from typing import Union
from connect_serial.utils.get_date import get_date_now


class CloseConnection:

    def __init__(self, serial) -> None:
        self.serial = serial

    def close(self) -> any:
        try:
            print(f"{get_date_now()} -> Fechando comunicação Serial...")

            is_open = self.serial.isOpen()

            if is_open is True:
                self.serial.close()
                print("Comunicação Serial Encerrada")
            else:
                print(f"Comunicação Serial já estava Fechada")

            return True
        except Exception as error:
            message = "Erro ao Fechar Conexão Serial"
            print(f"{get_date_now()} -> {message} ")
            print(f"{error} \n")
