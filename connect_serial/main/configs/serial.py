from serial import Serial
from local_settings import SERIAL_PORT, BAUDRATE, TIMEOUT, WRITE_TIMEOUT


class SerialConnect:

    def __init__(self):
        self.serial_connect = None
        self.port = None
        try:
            self.serial_connect = Serial(
                port=SERIAL_PORT, baudrate=BAUDRATE, timeout=TIMEOUT, write_timeout=WRITE_TIMEOUT)

            if self.serial_connect is not None and not self.serial_connect.is_open:
                self.serial_connect.open()

            print(self.serial_connect)
        except Exception as e:
            if self.serial_connect is not None and self.serial_connect.is_open:
                self.serial_connect.close()

            print(f"Erro ao configurar porta serial..")
            print(e)


    def get(self):
        return self.serial_connect