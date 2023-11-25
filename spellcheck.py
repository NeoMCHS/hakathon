import requests
from requests.exceptions import HTTPError
import json

def t9(text: str) -> str:
    speller_url = r"https://speller.yandex.net/services/spellservice.json/checkText"
    try:
        response = requests.get(speller_url, params={'text' : text})
    except HTTPError as e:
        print(f"An HTTP error has occured: {e}")
        return ""

    decoded: list = json.loads(response.text)

    output = text

    for error in decoded:
        pos = len(output) - (len(text) - error['pos'])
        slen = error['len']
        repl = error['s'][0]

        output = output[:pos] + repl + output[pos+slen:]

    return output
