import errors
import requests


def get_quote():

    try:
        res = requests.get("https://dummyjson.com/quotes/random")
        data = res.json()
        print(data)
    except:
        errors.error("Could not recieve quote (Maybe you are not connected to the internet?)")
    return data