from connect_serial.utils.get_date import get_date_now
from serial import Serial
from time import sleep



class CheckConnection:

    def __init__(self, serial: Serial, serial_open) -> None:
        self.serial = serial
        self.serial_open = serial_open
        self.attempts = 0

    async def __try_open_connect(self):
        sleep(1)
        await self.serial_open.open()
        self.attempts += 1
        await self.check()

    async def check(self) -> bool:
        try:

            if(self.attempts >= 3):
                raise Exception("Não existe Conexão com porta serial")
            else:
                is_open = self.serial.is_open()
                if not is_open:
                    print("Conexão serial está fechada")
                    await self.__try_open_connect()
                else:
                    return True
        except Exception as error:
            print(error)
            print("Erro na comunicação serial")
        finally:
            self.attempts = 0

    