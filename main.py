import requests
from requests_ntlm import HttpNtlmAuth
import configparser

def main():
    config = get_configs("config.cfg")
    url = get_config_section(config,"library")["url"]
    user = get_config_section(config,"credential")["user"]
    password = get_config_section(config,"credential")["password"]

    response = requests.get(url, verify=False, auth=HttpNtlmAuth(user, password))
    print(response.text)

def get_config_section(config, section):
    return dict(config.items(section))

def get_configs(file_path):
    config = configparser.RawConfigParser()
    config.read(file_path)
    return config

if __name__ == "__main__":
    main()
