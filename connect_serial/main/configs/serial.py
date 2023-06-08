from serial import Serial


class SerialConnect:

    def __init__(self):
        self.serial_connect = None
        self.port = None
        try:
            self.serial_connect = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=10, write_timeout=0)

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