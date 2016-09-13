import evdev
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
device = evdev.InputDevice('/dev/input/event0')
arriba = False
abajo =False
derecha = False
izquierda = False
print(device)

for event in device.read_loop():
    if(event.code == 17 or event.code == 16):
        if(event.value == -1 and event.code == 17):
            arriba = not arriba
            GPIO.output(2, arriba)
            print("Arriba")
        if(event.value == 1 and event.code == 17):
            abajo = not abajo
            GPIO.output(3,abajo)
            print("abajo")
        if(event.value == 1 and event.code == 16):
            derecha = not derecha
            GPIO.output(17,derecha)
            print("Derecha")
        if(event.value == -1 and event.code == 16):
            izquierda = not izquierda
            GPIO.output(27,izquierda)
            print("Izquierda")
