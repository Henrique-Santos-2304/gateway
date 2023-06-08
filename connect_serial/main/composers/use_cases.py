from connect_serial.main.composers.services_serial import send_pack, serial_write
from connect_serial.data.use_cases.comands.send import SendComands
from connect_serial.data.use_cases.read_async import ReadAsyncTask
from connect_serial.data.use_cases.rssi.send import SendRssi
from connect_serial.data.use_cases.trace_route.send import SendTraceRoute
from connect_serial.data.use_cases.noise.send import SendNoise
from connect_serial.data.use_cases.gps import ResponseGps



send_comands = SendComands(handle_bytes=send_pack, serial_write=serial_write)
send_rssi = SendRssi(handle_bytes=send_pack, serial_write=serial_write)
send_trace_route = SendTraceRoute(handle_bytes=send_pack, serial_write=serial_write)
send_noise = SendNoise(handle_bytes=send_pack, serial_write=serial_write)
send_gps = ResponseGps(handle_bytes=send_pack, serial_write=serial_write, send_comands=send_comands)



read_async = ReadAsyncTask()