from crud.models import Farm
import aws_iot.main.composers.mqtt_client as pub
from core.utils.save_initial_data import SaveInitialData
from time import sleep
import local_settings


class InitData:
    def __init__(self):
        self.received_data = True
        self.attempts = 1
    
    def dispatch(self, data):
        self.received_data = True
        self.attempts = 1

        SaveInitialData(data)
    
    def __check(self):
        sleep(5)
        
        if not self.received_data:
            self.attempts += 1
            self.__send()
            return
        
    def __send(self):
        self.received_data = False
        print(f"Salvando dados inciais... " if self.attempts == 1 else f"Tentativa de salvar dados iniciais n° {self.attempts}")
        message = "#" + f"1000-{local_settings.FARM_ID}$"
        pub.mqtt_publisher.start("newCloudHenrique", message)
        self.__check()
        
    def start(self):
        
        exist = Farm.objects.filter(farm_id=local_settings.FARM_ID).first()
        
        if not exist:
            self.__send()