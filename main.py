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

def main():
    rest_client = RestClientCE(url)

    try:
        rest_client.login(username=username, password=password)
        res = rest_client.get_tenant_device_infos(page_size=10, page=0)

        logging.info("Device info:\n%r", res)

    except ApiException as e:
        logging.exception(e)


if __name__ == '__main__':
    main()
