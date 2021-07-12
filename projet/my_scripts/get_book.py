# IMPORTS
#################################################################
import os
import os.path
import time
import the_functions as tf
from pathlib import Path
import subprocess as sb
#################################################################

# instancie le dossier qui contiendra les livres téléchargées
base_dir = Path(os.getcwd())
test_folder = base_dir / "downloads/books"

# crée le fichier csv qui contiendra les informations du livre
try:
    os.chdir(test_folder)
    os.mkdir("images")
    cmd = f"echo product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;category;review_rating;image_url;product_description > infos.csv"
    os.system(cmd)
except:
    pass

recherche = input("Mettez ici l'url du livre que vous rechercez => ")

# condition pour lancer la suite du script
if "https://books.toscrape.com/catalogue/" in recherche and not "category" in recherche:
    url = recherche
    os.chdir(test_folder)

    tf.write_infos(tf.book_infos_from_cat_url(url))
    print(
        "Parfait, votre livre vient d'être téléchargé, rendez-vous dans le dossier 'downloads/books' pour le consulter\n"
    )
    time.sleep(3)
    os.chdir('../../../')
    sb.call('py menu_principal.py 1', shell=True) 
else:
    print(
        "par mesures de sécurité, Seule une url correspondant à un livre et provenant du site 'bookstoscrape.com' est autorisée, veuillez recommencer\n"
    )
    time.sleep(3)
