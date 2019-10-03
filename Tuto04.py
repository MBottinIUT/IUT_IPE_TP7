# Importation des librairies utiles
from ColorCube import ColorCube
from PIL import Image

# Instanciation de l'objet color cube, en précisant d'éliminer les couleurs trop proches du blanc
cc = ColorCube(avoid_color=[255, 255, 255])

# Chargement d'une image et redimensionnement à la taille (100,100) pour
# rendre le temps de traitement plus rapide
# En diminuant la taille, on itensifie aussi la perception des couleurs dominantes
image = Image.open("images/lego-yellow-brick.jpg").resize((100,100))

# Traitement de l'image et extraction des couleurs
colors = cc.get_colors(image)

# Affichage des composantes de la couleur dominante
print ("couleur dominante R : {}".format(colors[0][0]))
print ("couleur dominante G : {}".format(colors[0][1]))
print ("couleur dominante B : {}".format(colors[0][2]))

