from dotenv import load_dotenv
import os

load_dotenv()

INFLUX_URL = os.environ.get("INFLUX_URL")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")

THINGSBOARD_URL = os.environ.get("THINGSBOARD_URL")
THINGSBOARD_USERNAME = os.environ.get("THINGSBOARD_USERNAME")
THINGSBOARD_PASSWORD = os.environ.get("THINGSBOARD_PASSWORD")