import requests


def get_quote():

    try:
        res = requests.get("https://dummyjson.com/quotes/random")
        data = res.json()
        print(data)
    except:
        data = ({
            "quote": "Random quote could not be retrieved (Maybe you are not connected to internet?)",
            "author": "Random quote could not be retrieved (Maybe you are not connected to internet?)"})
        return data
    return data