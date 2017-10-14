import requests,json, time


def getGame():
    post()
    time.sleep(5)
    post()
    get()


def get():
    try:
        result = requests.get("http://192.168.0.8:5000/resultadoJuego/2")
        getJSON = json.dumps(result.json())
        parsedGET = json.loads(getJSON)
        print(parsedGET)
    except requests.RequestException as e:
        post()
        print(e)


def post():
    try:
        request = requests.post("http://192.168.0.8:5000/iniciaJuego", data={'id': 2})
        postJSON = json.dumps(request.json())
        parsedPOST = json.loads(postJSON)
        print(parsedPOST)
    except requests.RequestException as e:
        print(e)
        post()

getGame()