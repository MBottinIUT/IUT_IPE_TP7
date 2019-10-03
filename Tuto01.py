# Importation des librairies
import requests
import pprint

# www.open-notify.org
# Récupération d'un fichier JSON correspondant au nombre de personne dans l'ISS
url = 'http://api.open-notify.org/astros.json'
personnes_ISS = requests.get(url)

# Récupération de flux JSON au sein de la requête effectuée et affichage
personnes_ISS_JSON = personnes_ISS.json()
print ("FICHIER JSON : ")
print (personnes_ISS_JSON)
print (" ")

# pprint permet juste un affichage plus aéré et mieux organisé dans la console
print ("AFFICHAGE ORGANISE DES DONNEES : ")
pprint.pprint(personnes_ISS_JSON)
print (" ")

# Affichage du nombre de personnes dans la station internationale en ce moment
print ("nombre de personnes dans l'ISS : {}".format(personnes_ISS_JSON['number']))

# Affichage du nom de chaque personne
for chacun in personnes_ISS_JSON['people'] :
    print ("nom : {}".format(chacun['name']))
	
