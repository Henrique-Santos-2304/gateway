

import os
from django.core.wsgi import get_wsgi_application
from threading import Thread
from connect_serial.main.composers.use_cases import read_async
from time import sleep
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

class ReadSync(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        while True:
            asyncio.run(read_async.start())
            sleep(6)
            
    
application = get_wsgi_application()
ReadSync().start()
