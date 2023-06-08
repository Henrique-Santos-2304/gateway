from aws_iot.main.config import MqttClient
from aws_iot.main.subscribe import AwsSubscribe
from aws_iot.main.producer import AwsProducer

mqtt_client = MqttClient().get_client()
mqtt_subscribe = AwsSubscribe(client=mqtt_client)
mqtt_publisher = AwsProducer(client=mqtt_client)