import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "x-api-key": "live_HkJ5ZoxXSrivOlmXtihpTo7lHb706MjmAC69TOOM3QwTCL0NHjnTT6sdQA8znV8T"
    }
    resposta = requests.get(url ,headers=headers)

    return resposta.json()


def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)
    return resposta.json()[0]