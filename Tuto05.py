# ATTENTION THONNY OU LE SCRIPT PYTHON DOIT ETRE LANCE EN 'SUDO'

# Importation des librairies nécessaires
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel
from time import sleep
from random import randint

# Déclaration du nombre de LEDs à piloter
NOMBRE_LEDS = 2

# Instanciation de l'objet LED
LED_NEOPIXEL = neopixel.NeoPixel(board.D18, NOMBRE_LEDS)

while True :
	try :
		# Affichage d'une couleur aléatoire sur les 2 LEDs Neopixel
		R = randint(0, 255)
		V = randint(0, 255)
		B = randint(0, 255)
		LED_NEOPIXEL[0] = (R,V,B)
		LED_NEOPIXEL[1] = (R,V,B)
		sleep(1)
	except KeyboardInterrupt :
		LED_NEOPIXEL[0] = (0,0,0)
		LED_NEOPIXEL[1] = (0,0,0)
		break

