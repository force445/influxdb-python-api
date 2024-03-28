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

POSGRES_HOST = os.environ.get("POSGRES_HOST")
POSGRES_USER = os.environ.get("POSGRES_USER")
POSGRES_PASSWORD = os.environ.get("POSGRES_PASSWORD")
POSGRES_DB = os.environ.get("POSGRES_DB")
POSGRES_PORT = os.environ.get("POSGRES_PORT")