from dotenv import load_dotenv
import os

load_dotenv()

INFLUX_URL = os.environ.get("INFLUX_URL")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_ORG = os.environ.get("INFLUX_ORG")

THINGSBOARD_URL = os.environ.get("THINGSBOARD_URL")
THINGSBOARD_USERNAME = os.environ.get("THINGSBOARD_USERNAME")
THINGSBOARD_PASSWORD = os.environ.get("THINGSBOARD_PASSWORD")

POSGRES_HOST = "192.168.1.100"
POSGRES_USER = "postgres"
POSGRES_PASSWORD = "123456789"
POSGRES_DB = "IoT"
POSGRES_PORT = "5432"