from mqtt import MQTT
from config import INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET

from influxdb_client import InfluxDBClient, WritePrecision, Point
from influxdb_client.client.write_api import SYNCHRONOUS


mqtt = MQTT("52.220.91.130", 1883, INFLUX_URL, INFLUX_TOKEN, INFLUX_ORG, INFLUX_BUCKET)