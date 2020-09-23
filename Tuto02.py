# Importation des librairies
import os
# git clone https://github.com/gurugaurav/bing_image_downloader
# sudo python3 setup.py install
# Lien vers doc API : pypi.org/project/bing-image-downloader
from bing_image_downloader import downloader

# Nombre d'images à télécharger
NB_IMG = 15

# Creation du dossier 'bing_search' s'il n'existe pas
if not os.path.exists("bing_search") :
    os.makedirs("bing_search")

# Demande des mots clefs à l'utilisateur
mots_clefs = input("Quels mots clefs souhaitez-vous pour votre recherche ? ")

# Récupération des images du résultat de la recherche
downloader.download(mots_clefs,limit=NB_IMG,output_dir="bing_search",force_replace=True)

