
# IMPORTS
#################################################################
import os
import os.path
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import the_functions as tf
#################################################################

# standardised used paths
base_dir = Path(os.getcwd())
test_folder = base_dir / 'downloads/tout_le_site'

the_cat_urls_list = []
cat_list_links = []
the_new_list = []
lien_livres = []
book_all_the_site_links = []
cat_list_titles = []

# fonction utile pour remplacer plusieurs caractères d'une string
def cls(str_to_clean, replacement_items_array, replace_by): 
    for item in replacement_items_array:
        if item in str_to_clean:
            str_to_clean = str_to_clean.replace(item, replace_by)
            new_str = str_to_clean
    return(new_str)


url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'

response = requests.get(url)
if response.ok:
    cat_soup = BeautifulSoup(response.text, 'html.parser')

    # ! Find the all_the_site links container
    all_the_site_content = cat_soup.select("li > ul > li > a")

    # ! Clean links and titles before putting them into their list
    for cat in all_the_site_content:
        cat_string = cat.string.strip()
        cat_string = cat_string.replace(' ', '-')
        cat_list_titles.append(cat_string)
        cat_href = cat.get('href')
        cat_href = str(cat_href).replace('../', 'http://books.toscrape.com/catalogue/category/')
        book_all_the_site_links.append(cat_href)
    
    
    tf.website_create_folders(test_folder, cat_list_titles)
    
    print(f"Recherche de l'url des catégories et d'éventuelles pages supplémentaires")
    for category_link in book_all_the_site_links:
        tf.get_cat_book_link(category_link, the_cat_urls_list)
    
    # ! get all the categories pages and its books
    print(f"Vérification de l'existence de pages supplémentaires")
    for urx in the_cat_urls_list:
        tf.urx_treatments(urx, the_new_list)

    print(f"Modification de l'url des livres pour la rendre consultable")
    for url in the_new_list:
        tf.books_links(url, lien_livres)

    print('Je stocke les informations des livres')
    for link in lien_livres:
        tf.book_infos_from_cat_url(link)
        
        my_list = tf.book_infos_from_cat_url(link)

        for fold in os.listdir(test_folder):
            for item in my_list:
                if fold == item:
                    os.chdir(f'{test_folder}/{fold}')
                    tf.write_infos(my_list)
            os.chdir('../../')

print('Informations écrites avec succès, vous pouvez consulter les fichiers dans downloads/tout_le_site')