from dotenv import load_dotenv
import os

load_dotenv()

INFLUX_URL = os.environ.get("INFLUX_URL")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_ORG = os.environ.get("INFLUX_ORG")
INFLUX_BUCKET = os.environ.get("INFLUX_BUCKET")

INFLUX_URL_2 = os.environ.get("INFLUX_URL_2")
INFLUX_TOKEN_2 = os.environ.get("INFLUX_TOKEN_2")
INFLUX_ORG_2 = os.environ.get("INFLUX_ORG_2")
INFLUX_BUCKET_2 = os.environ.get("INFLUX_BUCKET_2")

POSGRES_HOST = "192.168.1.100"
POSGRES_USER = "postgres"
POSGRES_PASSWORD = "123456789"
POSGRES_DB = "IoT"
POSGRES_PORT = "5432"