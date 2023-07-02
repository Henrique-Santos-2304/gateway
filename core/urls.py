from django.contrib import admin
from django.urls import path
from aws_iot.main.composers.mqtt_client import mqtt_subscribe
from django.contrib.auth import get_user_model
from core.main.composers.init_data import init_data
from crud.models import SoilUser

urlpatterns = [
    path("admin/", admin.site.urls),
]

mqtt_subscribe.start()
init_data.start()   
