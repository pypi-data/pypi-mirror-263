import os

import yaml

# dirs
CDIR = os.getcwd() + "/"
DIR_IMAGES = CDIR + "images/"
DIR_RUNS = CDIR + "runs/"
DIR_USER = os.path.expanduser("~")
DIR_SETTINGS = f"{DIR_USER}/.custom_api_tools/"

# file names
FILE_NAME_SETTINGS_FILE = "settings"
FILE_NAME_CONFIG_TRAIN_MODEL = "data"

# file types
FILE_TYPE_SETTING = ".yaml"
FILE_TYPE_CONFIG_TRAIN_MODEL = ".yaml"
FILE_TYPE_GET_IMAGE = ".png"


# paths
PATH_SETTINGS_FILE = DIR_SETTINGS + FILE_NAME_SETTINGS_FILE + FILE_TYPE_SETTING

# getting config from 'settings.yaml'
if not os.path.exists(DIR_SETTINGS):
    os.mkdir(DIR_SETTINGS)

if not os.path.exists(PATH_SETTINGS_FILE):
    with open(PATH_SETTINGS_FILE, "w") as settings_file:
        data = {
            "api_server_port": 1024,
            "api_server_host": "127.0.0.1",
            "api_title": "AiYOLO-API",
            "api_version": "0.0.1",
            "api_open_url": "/aiYOLO-api.json",
            "api_docs_url": "/docs",
        }
        yaml.dump(data, settings_file, sort_keys=False)

with open(PATH_SETTINGS_FILE, "r") as settings_file:
    config: dict[str, int | str] = yaml.safe_load(settings_file)

# api
API_SERVER_PORT = config["api_server_port"]
API_SERVER_HOST = config["api_server_host"]
API_TITLE = config["api_title"]
API_VERSION = config["api_version"]
API_OPEN_URL = config["api_open_url"]
API_DOCS_URL = config["api_docs_url"]