# IMPORTS
#################################################################
import os
import os.path
import time
import the_functions as tf
from pathlib import Path
import subprocess as sb
#################################################################

# instanciate route to avoid confusions
base_dir = Path(os.getcwd())
test_folder = base_dir / "downloads/books"

# Create the csv file and the images folder (try/except, for the next times we download another book)
try:
    os.chdir(test_folder)
    os.mkdir("images")
    cmd = f"echo product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;category;review_rating;image_url;product_description > infos.csv"
    os.system(cmd)
except:
    pass

# Here we get the user command
recherche = input("Mettez ici l'url du livre que vous rechercez => ")

# from this condition, launch the program or not
if "https://books.toscrape.com/catalogue/" in recherche and not "category" in recherche:
    url = recherche
    os.chdir(test_folder)

    # Take the given url then write the choosen informations coming from it into the csv file and the images folder
    tf.write_infos(tf.book_infos_from_cat_url(url))
    print(
        "Parfait, votre livre vient d'être téléchargé, rendez-vous dans le dossier 'downloads/books' pour le consulter\n"
    )
    time.sleep(3)
    os.chdir('../../../')
    sb.call('py menu_principal.py 1', shell=True) 
else:
    # If the given url doesn't fit the condition above, write this and break
    print(
        "par mesures de sécurité, Seule une url correspondant à un livre et provenant du site 'bookstoscrape.com' est autorisée, veuillez recommencer\n"
    )
    time.sleep(3)
