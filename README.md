valores de local_settings.py

FARM_ID

SERIAL_PORT
BAUDRATE=9600
TIMEOUT=10
WRITE_TIMEOUT=0

""" AWS CONFIGS """
AWS_URL
AWS_PORT
AWS_CA="aws_iot/keys/amazon_ca.pem"
AWS_KEY="aws_iot/keys/private.pem.key"
AWS_CRT="aws_iot/keys/device.pem.crt"

CLIENT_ID
TOPIC_SEND
AWS_TOPIC_GATEWAY
SUB_TOPIC_OF_FARM
SUB_TOPIC_INITIAL_DATA

<!-- Liberar permission Denied no Linux ao configurar porta serial  -->

sudo dmesg | grep tty #Verifica as portas conectadas no dispositivo
sudo chmod a+rw /dev/ttyUSB0 #Trocar ttyUSB0 pela porta que esta conectado o radio
