from time import sleep
from typing import Union
from connect_serial.utils.get_date import get_date_now


class ReadPackageSerial:

    def __init__(self, serial) -> None:
        self.serial = serial

    def read(self, bytes: int | None = 50) -> any:
        try:
            sleep(3)
            ser_bytes = self.serial.in_waiting

            if ser_bytes and ser_bytes > 0:
                print(
                    f"\n{get_date_now()} ->Dados encontrados na porta serial, Iniciando Leitura... {ser_bytes}"
                )
                response = self.serial.read(ser_bytes)
                if not response or len(response) <= 0:
                    raise  Exception(
                        "Dados foram encontrados, mas nenhum dado foi lido.")
                else:
                    print(f"Recebido Pacote de dados Serial -> {response}\n")
                    return response
        except Exception as error:
            print(f"{get_date_now()} -> Erro na Leitura de dados  Serial")
            print(f"{error} \n")
