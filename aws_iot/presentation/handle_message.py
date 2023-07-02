from aws_iot.utils.iot_codes import IDP_MESSAGES

class HandlerMessage:
    idp = None
    radio_id = None
    payload = None
    
    def __init__(self, send_comands, send_rssi, send_noise, send_route):
        self.send_comands = send_comands
        self.send_rssi = send_rssi
        self.send_noise = send_noise
        self.send_route = send_route
    
    async def switch_cases(self):
        if self.idp == IDP_MESSAGES["comands"]:
            print(f"Enviando comando para radio {self.radio_id}")
            return await self.send_comands.start(self.radio_id, self.payload)
        elif self.idp == IDP_MESSAGES["rssi"]:
            print(f"Buscando RSSI para radio {self.radio_id}")
            return await self.send_rssi.start(self.radio_id)
        elif self.idp == IDP_MESSAGES["trace_route"]:
            print(f"Buscando ROTAS do radio {self.radio_id}")
            return await self.send_route.start(self.radio_id)
        elif self.idp == IDP_MESSAGES["noise"]:
            print(f"Verificando RUÍDO do radio {self.radio_id}")
            return await self.send_noise.start(self.radio_id)
    
    def split_message(self, message: str):
        list_msg = message.split('#')[1].split('$')[0].split('-')
        
        self.idp = list_msg[0]
        self.radio_id = list_msg[1]
        self.payload = '-'.join(list_msg[2:])
        
    async def handler(self, message):
        self.split_message(message)
        await self.switch_cases()
        print("Ação finalizada com sucesso")