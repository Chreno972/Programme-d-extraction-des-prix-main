# IMPORTS
#################################################################
import os
import time
import os.path
import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path
import the_functions as tf
import subprocess as sb
#################################################################
# instancie le dossier qui contiendra les catégories téléchargées
base_dir = Path(os.getcwd())
test_folder = base_dir / "downloads/categories"

# L'utilisateur colle son url
url = input("Entrez l'url de la catégorie recherchée => ")


# déclarations des listes et d'un dictionnaire vides
the_list = []
the_cat_urls_list = []
new_list = []
books_link = []


# Condition pour déclencher le reste du programme
if "https://books.toscrape.com/catalogue/category/books/" in url:

    # le programme se place dans le dossier où sont téléchargées les catégories
    os.chdir(test_folder)

    # récupère et nettoie le nom de la catégorie
    requete = requests.get(url)
    soup_one = bs(requete.text, "html.parser")
    titre_categorie = soup_one.find("h1").string.strip()
    titre_categorie = titre_categorie.replace(" ", "_")

    # crée le dossier portant le nom de la catégorie
    try:
        if not os.path.exists(titre_categorie):
            os.mkdir(titre_categorie)
    except:
        pass

    os.chdir(titre_categorie)

    # crée le sous dossier images
    try:
        os.mkdir("images")
    except:
        pass

    # crée un fichier csv
    cmd = f"echo product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;category;review_rating;image_url;product_description > infos.csv"
    os.system(cmd)

    tf.get_cat_book_link(url, the_list)

    for urls in the_list:
        tf.urx_treatments(urls, new_list)

    for item in new_list:
        tf.books_links(item, books_link)

    for book in books_link:
        tf.write_infos(tf.book_infos_from_cat_url(book))
        os.chdir("../")

    # affiche le nombre d'images présent dans le dossier de catégorie
    time.sleep(3)
    liste_livres = []
    for livres in os.listdir("images"):
        liste_livres.append(livres)
    print(
        f"Bravo, vous avez téléchargé {len(liste_livres)} livres, vous pouvez dès à présent les consulter depuis la rubrique downloads/categories\n"
    )
    time.sleep(3)
    os.chdir('../../../')
    sb.call('py menu_principal.py 1', shell=True)

else:
    print(
        "par mesures de sécurité, Seule une url de catégorie et provenant du site 'bookstoscrape.com' est autorisée, veuillez recommencer\n"
    )
    time.sleep(3)
