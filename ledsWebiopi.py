import evdev
import requests
import base64
url = 'http://10.33.8.140:8000/GPIO/'
username = 'webiopi'
password = 'raspberry'
userPass = username + ':' + password
userPass = base64.b64encode(userPass)
print(userPass)
device = evdev.InputDevice('/dev/input/event0')
arriba = False
abajo =False
derecha = False
izquierda = False
print(device)
r = requests.post(url + '2/function/out', headers={'Authorization':'Basic ' +userPass})
r = requests.post(url + '3/function/out', headers={'Authorization':'Basic ' +userPass})
r = requests.post(url + '17/function/out', headers={'Authorization':'Basic ' +userPass})
r = requests.post(url + '27/function/out', headers={'Authorization':'Basic ' +userPass})

for event in device.read_loop():
    if(event.code == 17 or event.code == 16):
        if(event.value == -1 and event.code == 17):
            rg = requests.get(url + '2/value')
            arriba = bool(int(rg.text))
            arriba = not arriba
            r = requests.post(url + '2/value/'+ str(int(arriba)), headers={'Authorization':'Basic ' +userPass})
            print('arriba')
        if(event.value == 1 and event.code == 17):
            rg = requests.get(url+'3/value')
            abajo = bool(int(rg.text))
            abajo = not abajo
            r = requests.post(url + '3/value/'+ str(int(abajo)), headers={'Authorization':'Basic ' +userPass})
            print("abajo")
        if(event.value == 1 and event.code == 16):
            rg = requests.get(url+'17/value')
            derecha = bool(int(rg.text))
            derecha = not derecha
            r = requests.post(url + '17/value/'+ str(int(derecha)), headers={'Authorization':'Basic ' +userPass})
            print("Derecha")
        if(event.value == -1 and event.code == 16):
            rg = requests.get(url+'27/value')
            izquierda= bool(int(rg.text))
            izquierda = not izquierda
            r = requests.post(url + '27/value/'+ str(int(izquierda)), headers={'Authorization':'Basic ' +userPass})
            print("Izquierda")
