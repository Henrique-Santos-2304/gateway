from aws_iot.main.config import MqttClient
from aws_iot.main.subscribe import AwsSubscribe
from aws_iot.main.producer import AwsProducer
from aws_iot.presentation.handle_message import HandlerMessage
from connect_serial.main.composers.use_cases import send_comands, send_noise, send_rssi, send_trace_route


handler_messages = HandlerMessage(send_comands=send_comands, send_noise=send_noise, send_route=send_trace_route, send_rssi=send_rssi)
mqtt_client = MqttClient().get_client()
mqtt_subscribe = AwsSubscribe(client=mqtt_client, handler_messages=handler_messages)
mqtt_publisher = AwsProducer(client=mqtt_client)