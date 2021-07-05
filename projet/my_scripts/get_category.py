# IMPORTS
#################################################################
import os
import time
import os.path
import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path
import the_functions as tf
#################################################################
# instanciate route to avoid confusions
base_dir = Path(os.getcwd())
test_folder = base_dir / 'downloads/categories'

# L'utilisateur colle son url
url = input("Entrez l'url de la catégorie recherchée => ")


# déclarations des listes et d'un dictionnaire vides
the_list = []
the_cat_urls_list = []
new_list = []
books_link = []


# Condition to trigger the scripts
if 'https://books.toscrape.com/catalogue/category/books/' in url:

    # we go to the categories folder route
    os.chdir(test_folder)

    # Create the category folder, th
    requete = requests.get(url)
    soup_one = bs(requete.text, 'html.parser')
    titre_categorie = soup_one.find('h1').string.strip()
    titre_categorie = titre_categorie.replace(' ', '_')

    # Create the category folder
    try:
        if not os.path.exists(titre_categorie):
            os.mkdir(titre_categorie)
    except:
        pass

    os.chdir(titre_categorie)

    # Create the images sub folder
    try:
        os.mkdir('images')
    except:
        pass
    
    # Create the csv file
    cmd = f"echo product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;category;review_rating;image_url;product_description > infos.csv"
    os.system(cmd)
    
    tf.get_cat_book_link(url, the_list)

    for urls in the_list:
        tf.urx_treatments(urls, new_list)

    for item in new_list:
        tf.books_links(item, books_link)

    for book in books_link:
        tf.write_infos(tf.book_infos_from_cat_url(book))
        os.chdir('../')
    
    #display the number of downloaded books
    time.sleep(3)
    liste_livres = []
    for livres in os.listdir('images'):
        liste_livres.append(livres)
    print(f'Bravo, vous avez téléchargé {len(liste_livres)} livres, vous pouvez dès à présent les consulter depuis la rubrique downloads/categories')

else:
    print("par mesures de sécurité, Seule une url provenant du site 'bookstoscrape.com' est autorisée, veuillez recommencer\n")
    time.sleep(3)