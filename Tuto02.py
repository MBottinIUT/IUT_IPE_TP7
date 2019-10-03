# Importation des librairies
import os
# sudo pip3 install google_images_download
# http:www.github.com/hardikvasa/google-images-download  pour un lien vers la doc de l'API
from google_images_download import google_images_download

# Nombre d'images à télécharger
NB_IMG = 15

# Creation du dossier 'google_search' s'il n'existe pas
if not os.path.exists("google_search") :
    os.makedirs("google_search")

# Effacement de tous les fichiers du dossier 'google_search'
try :
    fichiers_presents = [ f for f in os.listdir("google_search")]
    for f in fichiers_presents:
        os.remove(os.path.join("google_search", f))
except FileNotFoundError :
    print("...")

# Instantiation de l'objet 'google'
reponse = google_images_download.googleimagesdownload()

# Demande des mots clefs à l'utilisateur
mots_clefs = input("Quels mots clefs souhaitez-vous pour votre recherche ? ")

# Récupération des images du résultat de la recherche
absolute_image_paths = reponse.download({"keywords":mots_clefs,"limit":NB_IMG,"format":"jpg","output_directory":"google_search","no_directory":'1'})

# renommer les images en changeant le nom web en index uniquement (ex: '8.jpg')
i=0
for f in os.listdir("google_search") :
    os.rename("google_search/"+f,"google_search/"+str(i)+".jpg")
    i+=1
