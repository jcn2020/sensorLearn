import os
import logging
import json

from st2reactor.sensor.base import Sensor

class sayHelloSensorClass(Sensor): 

    '''
    sample sensor to emit trigger-instance of sayhello_trigger
    '''
    def __init__(self, sensor_service, config):
        super(sayHelloSensorClass, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._poll_interval = 60

    def setup(self):
        pass

    def run(self):
        self._logger.debug("sayHelloSensorClass dispatching trigger-instance")
        payload = {}
        payload['x'] = "XXXX"
        payload['y'] = "YYYY"
        self.trigger_ref = "sample_sensor_automation.sayHelloTrigger"
        self.sensor_service.dispatch( trigger=self.trigger_ref, payload=payload )
    
    def cleanup(self):
        pass

    def update_trigger(self):
        pass

    def remove_trigger(self):
        pass

    def add_trigger(self):
        pass

