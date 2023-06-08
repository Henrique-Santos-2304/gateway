'''
    Códigos de comunicação Lora Mesh
'''

MAX_PAYLOAD_SIZE = 232  # Tamanho Máximo de payload trafegado
MAX_BUFFER_SIZE = 237  # Tamanho máximo do Buffer

'''
    Comandos aceitos pelo Radio Enge

    CMD_LORAPARAMETER = Leitura e escrita de parametros da modulação(*Configuração de modulação*)
    CMD_LOCALREAD = Leitura dos parametros do módulo conectado via UART(*Leitura da modulação*)
    CMD_REMOTEREAD = Leitura dos parametros qualquer módulo na rede
    CMD_WRITECONFIG = Escrita dos parametros de rede no dispositivo(* net e id *)
    CMD_GPIOCONFIG = Configura le e envia estado dos pinos GPIO
    CMD_DIAGNOSTICS =  Adquiri informação de operação de um nó especificado
    CMD_READNOISE =  Le nivel de ruido canal atual
    CMD_READRSSI = Le as potencias de sinal RSSI entre nó indicado e nó vizinho(*Mesh*)
    CMD_TRACEROUTE = Traça rota necessaria para o mestre comunicar com o nó especifico
    CMD_SENDTRANSP = Envia o pacote de dados para interface serial transparente do destino(* envia os dados *)

'''
COMMANDS = {
    "CMD_LORAPARAMETER": [0xD6, 214],
    "CMD_LOCALREAD": [0xE2, 226],
    "CMD_REMOTEREAD": [0xD4, 212],
    "CMD_WRITECONFIG": [0xCA, 202],
    "CMD_GPIOCONFIG": [0xC2, 194],
    "CMD_DIAGNOSTICS": [0xE7, 231],
    "CMD_READNOISE": [0xD8, 216],
    "CMD_READRSSI": [0xD5, 213],
    "CMD_TRACEROUTE": [0xD2, 210],
    "CMD_SENDTRANSP": [0x28, 40],
    "CMD_READGPRS": [0x38, 56],
    
}
# GPIOS = {
#     "GPIO2": 0,
#     "GPIO3": 1,
#     "GPIO4": 2,x'
#     "GPIO5": 3,
#     "GPIO6": 4,
#     "GPIO7": 5,
#     "GPIO8": 6
# }

# PULL = {
#     "PULL_OFF": 0,
#     "PULLUP": 1,
#     "PULLDOWN": 2
# }


'''
    Comando para saber se o rede a mesh está ligado ou desligado
'''
MESHSTATUS = {
    "MESH_OK": 0,
    "MESH_ERROR": 1
}
