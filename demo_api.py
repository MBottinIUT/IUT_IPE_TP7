# Importation des librairies utiles
import os
# sudo pip3 install gTTS
# sudo apt-get install mpg321
from gtts import gTTS
# sudo pip3 install wikipedia
import wikipedia

# Initialisation de wikipedia en français
wikipedia.set_lang("fr")

# Demande de l'objet de la recherche à l'utilisateur
requete = input("De quoi voulez-vous que je vous parle ? ")

# Récupération des deux premières phrases de la page wikipedia
reponse = wikipedia.summary(requete, sentences=2)
# Affichage de la réponse
print(reponse)

# Lecture de la réponse par la synthèse vocale de Google en ligne
tts = gTTS(text=reponse, lang='fr')
tts.save("reponse.mp3")
os.system("mpg321 reponse.mp3")