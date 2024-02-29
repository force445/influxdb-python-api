import paho.mqtt.client as mqtt
import time

from posgres import Posgres
from config import POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT

class MQTT():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.posgres = Posgres(POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT)
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.connect(self.host, self.port)
        self.client.loop_forever()

    def get_app_id_env(self):
        data = self.posgres.select_device_env_monitoring()
        if data["app_id"] == "0f50f6ff-338d-4dcd-a522-5cfd24f6ffe7":
            return data["app_id"]

    def get_dev_eui_env(self):
        data = self.posgres.select_device_env_monitoring()
        return data["deveui"]
    
    def get_app_id_iot_controller(self):
        data = self.posgres.select_device_iot_controller()
        if data["app_id"] == "18ab31a6-9a0d-4a38-a5e3-b3605a9a309f":
            return data["app_id"]
    
    def get_dev_eui_iot_controller(self):
        data = self.posgres.select_device_iot_controller()
        return data["deveui"]
    
    def get_app_id_mag_contract_switch(self):
        data = self.posgres.select_device_magnetic()
        if data["app_id"] == "c22e4c79-d61a-4e8e-bccd-e39384c913f9":
            return data["app_id"]
    
    def get_dev_eui_mag_contract_switch(self):
        data = self.posgres.select_device_magnetic()
        return data["deveui"]

    def get_app_id_pir(self):
        data = self.posgres.select_device_pir()
        if data["app_id"] == "b50618fe-3073-4e6c-acaf-b1b2ff3af9bf":
            return data["app_id"]
        
    def get_dev_eui_pir(self):
        data = self.posgres.select_device_pir()
        return data["deveui"]
    
    def get_app_id_portable_socket(self):
        data = self.posgres.select_device_portable_socket()
        if data["app_id"] == "99cedc9c-2c85-44a0-9889-63ac556fdeac":
            return data["app_id"]
        
    def get_dev_eui_portable_socket(self):
        data = self.posgres.select_device_portable_socket()
        return data["deveui"]

    def get_app_id_smart_button(self):
        data = self.posgres.select_device_smart_button()
        if data["app_id"] == "9d59b0e3-5210-4763-9fb3-a6fdc8d511f4":
            return data["app_id"]

    def get_dev_eui_smart_button(self):
        data = self.posgres.select_device_smart_button()
        return data["deveui"]
    
    def get_app_id_sound_level(self):
        data = self.posgres.select_device_sound_level()
        if data["app_id"] == "2b695811-907e-4e92-b1c7-00d2ca2dc3c7":
            return data["app_id"]

    def get_dev_eui_sound_level(self):
        data = self.posgres.select_device_sound_level()
        return data["deveui"]

    def on_message (self, client, userdata, message) :
        raw_message = str(message.payload.decode("utf-8"))
        topic = message.topic
        
        print(f"Received message '{raw_message}' on topic '{topic}'")

    def on_subscribe (self, client, obj, mid, granted_qos) :
        print("Subscribe Succeed")


    def on_connect(self, client, userdata, flags, rc):
        #Env
        app_id_env = self.get_app_id_env()
        dev_eui_env = self.get_dev_eui_env()
        print(f"application/{app_id_env}/device/{dev_eui_env}/event/up")
        client.subscribe(f"application/{app_id_env}/device/{dev_eui_env}/event/up")
        #Iot Controller
        app_id_iot_controller = self.get_app_id_iot_controller()
        dev_eui_iot_controller = self.get_dev_eui_iot_controller()
        print(f"application/{app_id_iot_controller}/device/{dev_eui_iot_controller}/event/up")
        client.subscribe(f"application/{app_id_iot_controller}/device/{dev_eui_iot_controller}/event/up")
        #Magnetic Contract switch
        app_id_mag_contract_switch = self.get_app_id_mag_contract_switch()
        dev_eui_mag_contract_switch = self.get_dev_eui_mag_contract_switch()
        print(f"application/{app_id_mag_contract_switch}/device/{dev_eui_mag_contract_switch}/event/up")
        client.subscribe(f"application/{app_id_mag_contract_switch}/device/{dev_eui_mag_contract_switch}/event/up")
        #PIR
        app_id_pir = self.get_app_id_pir()
        dev_eui_pir = self.get_dev_eui_pir()
        print(f"application/{app_id_pir}/device/{dev_eui_pir}/event/up")
        client.subscribe(f"application/{app_id_pir}/device/{dev_eui_pir}/event/up")
        #Portable_Socket
        app_id_portable_socket = self.get_app_id_portable_socket()
        dev_eui_portable_socket = self.get_dev_eui_portable_socket()
        print(f"application/{app_id_portable_socket}/device/{dev_eui_portable_socket}/event/up")
        client.subscribe(f"application/{app_id_portable_socket}/device/{dev_eui_portable_socket}/event/up")
        #Smart Button
        app_id_smart_button = self.get_app_id_smart_button()
        dev_eui_smart_button = self.get_dev_eui_smart_button()
        print(f"application/{app_id_smart_button}/device/{dev_eui_smart_button}/event/up")
        client.subscribe(f"application/{app_id_smart_button}/device/{dev_eui_smart_button}/event/up")
        #Sound level sensor
        app_id_sound_level = self.get_app_id_sound_level()
        dev_eui_sound_level = self.get_dev_eui_sound_level()
        print(f"application/{app_id_sound_level}/device/{dev_eui_sound_level}/event/up")
        client.subscribe(f"application/{app_id_sound_level}/device/{dev_eui_sound_level}/event/up")


mqtt = MQTT("52.220.91.130", 1883)
