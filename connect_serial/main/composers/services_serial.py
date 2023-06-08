from connect_serial.data.services import send_pack, check_connection, open_connection, close_connection, read_package, write_packages
from connect_serial.main.configs.serial import SerialConnect

serial_connect = SerialConnect().get()
serial_open = open_connection.OpenConnection(serial_connect)
serial_check = check_connection.CheckConnection(serial_connect, serial_open=serial_open)
serial_close = close_connection.CloseConnection(serial_connect)
serial_read = read_package.ReadPackageSerial(serial_connect)
serial_write = write_packages.WriteDataSerial(serial_connect, serial_check)
send_pack = send_pack.SendPackage()