import requests,json,time

class Cliente():
    def __init__(self,id):
            self.id = id

    def getGame(self):
        self.post()
        time.sleep(5)
        self.post()
        self.get()


    def get(self):
        try:
            result = requests.get("http://192.168.0.8:5000/resultadoJuego/1")
            getJSON = json.dumps(result.json())
            parsedGET = json.loads(getJSON)
            print(parsedGET)
        except requests.RequestException as e:
            self.post()
            print(e)


    def post(self):
        try:
            request = requests.post("http://192.168.0.8:5000/iniciaJuego", data={'id': self.id})
            postJSON = json.dumps(request.json())
            parsedPOST = json.loads(postJSON)
            print(parsedPOST)
        except requests.RequestException as e:
            print(e)
            self.post()



cliente1 = Cliente(1)
cliente2 = Cliente(2)


cliente1.getGame()
cliente2.getGame()
