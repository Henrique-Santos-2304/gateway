
from django.contrib import admin
from django.urls import path
from aws_iot.main.composers.mqtt_client import mqtt_subscribe


urlpatterns = [
    path('admin/', admin.site.urls),
]

mqtt_subscribe.start()
