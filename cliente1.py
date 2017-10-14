import requests,json

def getGame():
    try:
        request = requests.post("http://10.2.3.195:5000/iniciaJuego",data={'id': 1})
    except requests.RequestException:
        print("Error")

getGame()