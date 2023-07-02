from connect_serial.main.composers.services_serial import send_pack, serial_write
from connect_serial.data.use_cases.comands.send import SendComands
from connect_serial.data.use_cases.read_async import ReadAsyncTask
from connect_serial.data.use_cases.rssi.send import SendRssi
from connect_serial.data.use_cases.trace_route.send import SendTraceRoute
from connect_serial.data.use_cases.noise.send import SendNoise
from connect_serial.data.use_cases.gps import ResponseGps

from connect_serial.data.use_cases.comands.response_comand import ResponseComand
from connect_serial.data.use_cases.noise.save_noise import SaveNoise
from connect_serial.data.use_cases.rssi.save_rssi import SaveRssi
from connect_serial.data.use_cases.trace_route.save_trace_route import SaveTraceRoute






send_comands = SendComands(handle_bytes=send_pack, serial_write=serial_write)
send_rssi = SendRssi(handle_bytes=send_pack, serial_write=serial_write)
send_trace_route = SendTraceRoute(handle_bytes=send_pack, serial_write=serial_write)
send_noise = SendNoise(handle_bytes=send_pack, serial_write=serial_write)
send_gps = ResponseGps(handle_bytes=send_pack, serial_write=serial_write, send_comands=send_comands)

save_comands = ResponseComand()
save_rssi = SaveRssi()
save_noise = SaveNoise()
save_trace_route = SaveTraceRoute()


read_async = ReadAsyncTask(save_comands_service=save_comands, save_noise_service=save_noise, save_rssi_service=save_rssi, save_trace_route_service=save_trace_route, save_gps_service=send_gps)