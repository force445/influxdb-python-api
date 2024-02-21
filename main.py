import logging

from dotenv import load_dotenv
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException

from config import THINGSBOARD_URL, THINGSBOARD_USERNAME, THINGSBOARD_PASSWORD

load_dotenv()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

url = THINGSBOARD_URL

username = THINGSBOARD_USERNAME
password = THINGSBOARD_PASSWORD

rest_client = RestClientCE(url)
rest_client.login(username=username, password=password)
def fetch_device():

    try:
        res = rest_client.get_tenant_device_infos(page_size=10, page=0)

        logging.info("Device info:\n%r", res)

    except ApiException as e:
        logging.exception(e)


def manage_device():

    try:
        device = Device(name="Test Device", type="default", label="Test Device")
        res = rest_client.save_device(device)

        logging.info("Device info:\n%r", res)

    except ApiException as e:
        logging.exception(e)

if __name__ == '__main__':
    fetch_device()