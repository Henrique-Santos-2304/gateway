from connect_serial.main.composers.services_serial import serial_read, serial_check, serial_connect
from connect_serial.utils.codes_buffer import COMMANDS
from time import sleep
from typing import Dict, Type


class ReadAsyncTask:
    cmds = [
            COMMANDS["CMD_READRSSI"][1],
            COMMANDS["CMD_TRACEROUTE"][1],
            COMMANDS["CMD_SENDTRANSP"][1],
            COMMANDS["CMD_READNOISE"][1],
            COMMANDS["CMD_READGPRS"][1]
        ]
    
    def __init__(self): 
        self.cmd_index = 2
        self.__response_for_check_crc = []
        self.response_msg_checking = None
        self.response_serial = None
        self.list_response = None


    async def start(self):
        try:
            to_have_connection_serial = await serial_check.check()
            if to_have_connection_serial == True:
                self.response = serial_read.read()

                if self.response:
                    print(f"Leitura serial recebida: {self.response}")
                    self.list_response = [int(x) for x in self.response]
                    
                    """ return await self.__check_duplicate_response() """
                return
            else:
                print("Conexão fechada...")
                return 
        except Exception as e:
            print(f"Error Read Async Task : {e}")



"""     async def more_response(self):
        if len(self.list_response) > 0:
            print(
                    f"\nForam encontrados mais de uma resposta na porta serial ")
            await self.__check_duplicate_response()
        return
    
    async def split_trace_route(self):
        len_lis = len(self.list_response)
        exist_only_message = len(self.list_response) < 8
        if exist_only_message:
            trace_route_msg = self.list_response[0: 8]
            print(f"Trace route message -> {trace_route_msg}")
            response = await self.save_trace_route_service.start(trace_route_msg)            
            return self.publish_into_topic("RESPONSE_TRACE_ROUTE", response)
        else:
            exist_more = False
            for i,x in enumerate(self.list_response):
                if i > 7:
                    new_serial_reading = x in self.cmds
                    if new_serial_reading:
                        indice_start_new_message = i - 2
                        first_message = self.list_response[0: indice_start_new_message]
                        self.list_response = self.list_response[indice_start_new_message: len(self.list_response) + 1  ]
                        exist_more = True
                        response = await self.save_trace_route_service.start(first_message)            
                        self.publish_into_topic("RESPONSE_TRACE_ROUTE", response)
                        return await self.more_response()
                        break

            if not exist_more:
                trace_route_msg = self.list_response[0: len(self.list_response) + 1]
                print(f"Trace route message -> {trace_route_msg}")
                response = await self.save_trace_route_service.start(trace_route_msg)            
                return self.publish_into_topic("RESPONSE_TRACE_ROUTE", response)
                
    async def split_rssi(self):
        rssi_msg = self.list_response[0: 13]
        
        self.list_response = self.list_response[13:len(self.list_response)]
        
        response = await self.save_rssi_service.start(rssi_msg)
        return await self.more_response()

    async def split_read_noise(self):
        noise_msg = self.list_response[0: 8]
        self.list_response = self.list_response[8:len(self.list_response)]
        
        response = await self.save_noise_service.start(noise_msg)
        self.publish_into_topic("RESPONSE_NOISE", response)
        return await self.more_response()
        
    async def split_serial_transparent(self):
        counter = 0
        index_last_splited = 0
        for i,x in enumerate(self.list_response):
            if x == 36:
                index_last_splited = i
                break
        first_response = self.list_response[0: index_last_splited + 2]
        self.list_response = self.list_response[index_last_splited + 3:len(self.list_response)]
        return await self.handle_gps_or_comands_event(first_response)
        # rssi_msg = self.list_response[0: 13]
        # self.send_message(rssi_msg)

    async def handle_gps_or_comands_event(self, message):
        array = str(bytes(message))
        is_message_gps = "GPS" in array
        if is_message_gps:
            await self.save_gps_service.start(message)
        else:
            response = self.save_comands_service.start(message)
            self.publish_into_topic("RESPONSE_COMANDS", response)
        return await self.more_response()
            
    async def __check_duplicate_response(self):
        
        response_is_comands = self.list_response[2] == self.cmds[2]
        if response_is_comands:
            return await self.split_serial_transparent()
        else:
            for i, v in enumerate(self.list_response):
                if v == self.list_response[2] == self.cmds[0]:
                    return await self.split_rssi()
                elif v == self.list_response[2] == self.cmds[3]:
                    return await self.split_read_noise()
                elif v == self.list_response[2] == self.cmds[1]:
                    return await self.split_trace_route()
                if i > 2 and v in self.cmds:
                    print(
                        f"Foram encontrados mais de uma resposta na porta serial ")
                    return i
                    
            return
        print("\n \n")
         """