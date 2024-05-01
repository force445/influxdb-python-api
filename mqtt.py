import paho.mqtt.client as mqtt
import time
import json


from influxdb_client import InfluxDBClient, WritePrecision, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from posgres import Posgres
from config import POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT


class MQTT():
    def __init__(self, host, port, url, token, org, bucket, url_2, token_2, org_2, bucket_2):
        self.host = host
        self.port = port
        self.posgres = Posgres(POSGRES_HOST, POSGRES_USER, POSGRES_PASSWORD, POSGRES_DB, POSGRES_PORT)
        self.client = mqtt.Client()
        self.url = url
        self.token = token
        self.org = org
        self.bucket = bucket
        self.url_2 = url_2
        self.token_2 = token_2
        self.org_2 = org_2
        self.bucket_2 = bucket_2
        self.influxclient = InfluxDBClient(url=self.url, token=self.token, org=self.org, timeout=30000)
        self.influxclient_2 = InfluxDBClient(url=self.url, token=self.token, org=self.org, timeout=30000)
        self.write_api = self.influxclient.write_api(write_options=SYNCHRONOUS)
        self.write_api_2 = self.influxclient_2.write_api(write_options=SYNCHRONOUS)
        self.check_influx_connection()
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.connect(self.host, self.port)
        self.client.loop_forever()

    def get_app_id_env(self):
        data = self.posgres.select_device_env_monitoring()
        if data["app_id"] == "0f50f6ff-338d-4dcd-a522-5cfd24f6ffe7":
            return "0f50f6ff-338d-4dcd-a522-5cfd24f6ffe7"

    def get_dev_eui_env(self):
        data = self.posgres.select_device_env_monitoring()
        return data["deveui"]
    
    def get_app_id_iot_controller(self):
        data = self.posgres.select_device_iot_controller()
        if data["app_id"] == "18ab31a6-9a0d-4a38-a5e3-b3605a9a309f":
            return "18ab31a6-9a0d-4a38-a5e3-b3605a9a309f"
    
    def get_dev_eui_iot_controller(self):
        data = self.posgres.select_device_iot_controller()
        return data["deveui"]
    
    def get_app_id_mag_contract_switch(self):
        data = self.posgres.select_device_magnetic()
        if data["app_id"] == "c22e4c79-d61a-4e8e-bccd-e39384c913f9":
            return "c22e4c79-d61a-4e8e-bccd-e39384c913f9"
    
    def get_dev_eui_mag_contract_switch(self):
        data = self.posgres.select_device_magnetic()
        return data["deveui"]

    def get_app_id_pir(self):
        data = self.posgres.select_device_pir()
        if data["app_id"] == "b50618fe-3073-4e6c-acaf-b1b2ff3af9bf":
            return "b50618fe-3073-4e6c-acaf-b1b2ff3af9bf"
        
    def get_dev_eui_pir(self):
        data = self.posgres.select_device_pir()
        return data["deveui"]
    
    def get_app_id_portable_socket(self):
        data = self.posgres.select_device_portable_socket()
        if data["app_id"] == "99cedc9c-2c85-44a0-9889-63ac556fdeac":
            return "99cedc9c-2c85-44a0-9889-63ac556fdeac"
        
    def get_dev_eui_portable_socket(self):
        data = self.posgres.select_device_portable_socket()
        return data["deveui"]

    def get_app_id_smart_button(self):
        data = self.posgres.select_device_smart_button()
        if data["app_id"] == "9d59b0e3-5210-4763-9fb3-a6fdc8d511f4":
            return "9d59b0e3-5210-4763-9fb3-a6fdc8d511f4"

    def get_dev_eui_smart_button(self):
        data = self.posgres.select_device_smart_button()
        return data["deveui"]
    
    def get_app_id_sound_level(self):
        data = self.posgres.select_device_sound_level()
        if data["app_id"] == "2b695811-907e-4e92-b1c7-00d2ca2dc3c7":
            return "2b695811-907e-4e92-b1c7-00d2ca2dc3c7"

    def get_dev_eui_sound_level(self):
        data = self.posgres.select_device_sound_level()
        return data["deveui"]

    def on_message (self, client, userdata, message) :
        raw_message = str(message.payload.decode("utf-8"))
        raw_message = json.loads(raw_message)
        topic = message.topic
        
        if topic == "application/0f50f6ff-338d-4dcd-a522-5cfd24f6ffe7/device/24e124136d156431/event/up":
            if not raw_message["object"]:
                raw_message["object"]["humidity"] = 0
                raw_message["object"]["temperature"] = 0

                point = {
                    "measurement": "env_monitoring",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],

                    },
                    "fields": {
                        "humidity": raw_message["object"]["humidity"],
                        "temperature": raw_message["object"]["temperature"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)
                
            elif "battery" in raw_message["object"]:
                pass
            elif "humidity" and "temperature" in raw_message["object"]:
                point = {
                    "measurement": "env_monitoring",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],

                    },
                    "fields": {
                        "humidity": raw_message["object"]["humidity"],
                        "temperature": raw_message["object"]["temperature"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)

        if topic == "application/18ab31a6-9a0d-4a38-a5e3-b3605a9a309f/device/24e124445d186700/event/up":
            if "battery" in raw_message["object"]:
                pass
            else:
                if "gpio_out_1" in raw_message["object"]:
                    point = {
                        "measurement": "iot_controller",
                        "tags": {
                            "deviceName":raw_message["deviceInfo"]["deviceName"],
                            "devEUI": raw_message["deviceInfo"]["devEui"],
                            "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                        },
                        "fields": {
                            "gpio_out_1": raw_message["object"]["gpio_out_1"],
                        }
                    }

                    self.write_api.write(self.bucket, self.org, point)
                elif "gpio_out_2" in raw_message["object"]:
                    point = {
                        "measurement": "iot_controller",
                        "tags": {
                            "deviceName":raw_message["deviceInfo"]["deviceName"],
                            "devEUI": raw_message["deviceInfo"]["devEui"],
                            "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                        },
                        "fields": {
                            "gpio_out_2": raw_message["object"]["gpio_out_2"],
                        }
                    }

                    self.write_api.write(self.bucket, self.org, point)

        if topic == "application/c22e4c79-d61a-4e8e-bccd-e39384c913f9/device/24e124141d223816/event/up":
            if "install" in raw_message["object"]:
                pass
            elif "battery" in raw_message["object"]:
                pass
            else:
                if raw_message["object"]["state"] == "open":
                    raw_message["object"]["state"] = 1
                elif raw_message["object"]["state"] == "close":
                    raw_message["object"]["state"] = 0

                point = {
                    "measurement": "magnetic_contract_switch",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                    },
                    "fields": {
                        "magnetic_contract": raw_message["object"]["state"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)

        if topic == "application/b50618fe-3073-4e6c-acaf-b1b2ff3af9bf/device/24e124538d222160/event/up":
            if "battery" in raw_message["object"]:
                pass
            else:
                if raw_message["object"]["pir"] == "normal":
                    raw_message["object"]["pir"] = 0
                elif raw_message["object"]["pir"] == "trigger":
                    raw_message["object"]["pir"] = 1

                point = {
                    "measurement": "pir",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                    },
                    "fields": {
                        "pir": raw_message["object"]["pir"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)

        if topic == "application/99cedc9c-2c85-44a0-9889-63ac556fdeac/device/24e124148c406038/event/up":
            if "battery" in raw_message["object"]:
                pass
            else:
                if "factor" in raw_message["object"]:
                    point = {
                        "measurement": "portable_socket",
                        "tags": {
                            "deviceName":raw_message["deviceInfo"]["deviceName"],
                            "devEUI": raw_message["deviceInfo"]["devEui"],
                            "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                        },
                        "fields": {
                            "factor": raw_message["object"]["factor"],
                            "current": raw_message["object"]["current"],
                            "state": raw_message["object"]["state"],
                        }
                    }

                    self.write_api.write(self.bucket, self.org, point)

                elif "powersum" in raw_message["object"]:
                    point = {
                        "measurement": "portable_socket",
                        "tags": {
                            "deviceName":raw_message["deviceInfo"]["deviceName"],
                            "devEUI": raw_message["deviceInfo"]["devEui"],
                            "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                        },
                        "fields": {
                            "powersum": raw_message["object"]["powersum"],
                            "voltage": raw_message["object"]["voltage"],
                        }
                    }

                    self.write_api.write(self.bucket, self.org, point)

                elif "power" in raw_message["object"]:
                    point = {
                        "measurement": "portable_socket",
                        "tags": {
                            "deviceName":raw_message["deviceInfo"]["deviceName"],
                            "devEUI": raw_message["deviceInfo"]["devEui"],
                            "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                        },
                        "fields": {
                            "power": raw_message["object"]["power"],
                        }
                    }

                    self.write_api.write(self.bucket, self.org, point)

        if topic == "application/9d59b0e3-5210-4763-9fb3-a6fdc8d511f4/device/24e124535d229796/event/up":
            if "battery" in raw_message["object"]:
                pass
            else:
                point = {
                    "measurement": "smart_button",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                    },
                    "fields": {
                        "press": raw_message["object"]["press"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)

        if topic == "application/2b695811-907e-4e92-b1c7-00d2ca2dc3c7/device/24e124743d015542/event/up":
            if "battery" in raw_message["object"]:
                pass
            else:
                point = {
                    "measurement": "sound_level_sensor",
                    "tags": {
                        "deviceName":raw_message["deviceInfo"]["deviceName"],
                        "devEUI": raw_message["deviceInfo"]["devEui"],
                        "deviceClassEnabled": raw_message["deviceInfo"]["deviceClassEnabled"],
                    },
                    "fields": {
                        "laeq": raw_message["object"]["laeq"],
                    }
                }

                self.write_api.write(self.bucket, self.org, point)

    def on_subscribe (self, client, obj, mid, granted_qos) :
        print("Subscribed topic: "+str(mid))


    def on_connect(self, client, userdata, flags, rc):
        #Env
        app_id_env = self.get_app_id_env()
        dev_eui_env = self.get_dev_eui_env()
        app_id_iot_controller = self.get_app_id_iot_controller()
        dev_eui_iot_controller = self.get_dev_eui_iot_controller()
        app_id_mag_contract_switch = self.get_app_id_mag_contract_switch()
        dev_eui_mag_contract_switch = self.get_dev_eui_mag_contract_switch()
        app_id_pir = self.get_app_id_pir()
        dev_eui_pir = self.get_dev_eui_pir()
        app_id_portable_socket = self.get_app_id_portable_socket()
        dev_eui_portable_socket = self.get_dev_eui_portable_socket()
        app_id_smart_button = self.get_app_id_smart_button()
        dev_eui_smart_button = self.get_dev_eui_smart_button()
        app_id_sound_level = self.get_app_id_sound_level()
        dev_eui_sound_level = self.get_dev_eui_sound_level()
        topics = [(f"application/{app_id_env}/device/{dev_eui_env}/event/up",0), (f"application/{app_id_iot_controller}/device/{dev_eui_iot_controller}/event/up",0), (f"application/{app_id_mag_contract_switch}/device/{dev_eui_mag_contract_switch}/event/up",0), (f"application/{app_id_pir}/device/{dev_eui_pir}/event/up",0), (f"application/{app_id_portable_socket}/device/{dev_eui_portable_socket}/event/up",0), (f"application/{app_id_smart_button}/device/{dev_eui_smart_button}/event/up",0), (f"application/{app_id_sound_level}/device/{dev_eui_sound_level}/event/up",0)]

        for topic in topics:
            self.client.subscribe(topic)

    def check_influx_connection(self):
        try:
            self.influxclient = InfluxDBClient(url=self.url, token=self.token, org=self.org, timeout=30000)
            self.write_api = self.influxclient.write_api(write_options=SYNCHRONOUS)
            print("InfluxDB Connection Succeed")
            return True
        except Exception as e:
            return False
        