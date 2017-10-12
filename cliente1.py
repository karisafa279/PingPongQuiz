import requests,json

def getGame():
    try:
        request = requests.get("http://192.168.0.10:5000/iniciaJuego")
        gameJSONResponse = json.dumps(request.json)
        parsedJSON = json.loads(gameJSONResponse)
        print(parsedJSON)
    except requests.exception.RequestException:
        print("Error")


