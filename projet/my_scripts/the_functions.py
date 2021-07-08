
# IMPORTS
#################################################################
import re
import csv
import os
import time
import os.path
import requests
from bs4 import BeautifulSoup as bs
from pathlib import Path
#################################################################


base_dir = Path(os.getcwd())
tfold = base_dir / 'downloads/tout_le_site'


# fonction utile pour remplacer plusieurs caractères d'une string
def cls(str_to_clean, replacement_items_array, replace_by): 
    for item in replacement_items_array:
        if item in str_to_clean:
            str_to_clean = str_to_clean.replace(item, replace_by)
    return(str_to_clean)


# récupérer le lien de chaque catégorie, et trouver les catégories avec plusieurs pages
def get_cat_book_link(lien, liste):
    liste.append(lien)
    try:
        for i in range(2,9):
            uri = lien.replace('index', f'page-{i}')
            status_code = requests.get(uri)
            if status_code.ok:
                liste.append(uri)
    except:
        pass


# Sauvegarder dans une nouvelle liste uniquement les urls fonctionnelles
def urx_treatments(urz, nouvelle_liste):
    status_code = requests.get(urz)
    if status_code.ok:
        nouvelle_liste.append(urz)
    return nouvelle_liste


# Corriger le lien de chaque livre pour le rendre consultable
def books_links(page_categorie, le_lien_livres):
    res = requests.get(page_categorie)
    soupy = bs(res.text, 'html.parser')
    product_pods = soupy.find_all(class_="product_pod")
    for soup in product_pods:
        book_link = soup.find("h3").a.get('href')
        book_link = book_link.replace('../../../', 'https://books.toscrape.com/catalogue/')
        le_lien_livres.append(book_link)
    return(le_lien_livres)
        

# traiter les informations récoltées d'un livre et les regrouper dans une variable
def book_infos_from_cat_url(the_link):
    response = requests.get(the_link)
    if response.ok:
        book_info_soup = bs(response.content, 'html.parser')

        # Findings & Treatments
        tds = book_info_soup.find_all('td')
        tds_arr = []
        for td in tds:
            tds_arr.append(td.string)
        universal_product_code = tds_arr[0]

        price_excluding_tax = cls(tds_arr[2], ['Â', '£'], '')
        price_including_tax = cls(tds_arr[3], ['Â', '£'], '')

        number_available = re.findall('\d+', tds_arr[5])
        number_available = cls(str(number_available), ["[", "]", "'"], '')

        # Nettoyer les titres pour éviter les bugs et retirer toutes imperfections
        title = book_info_soup.title.string
        title = cls(str(title), [' | Books to Scrape - Sandbox',":", ")", "(", '...', '*', '"', '#', '?', ','], '')
        title = title.strip()
        title = title.replace(' ', '_')
        title = title.replace('/', '_')
        title = title.replace('Vol._', 'Vol.')

        # ne garde que le texte entre crochets ou entre parenthèses
        title = re.sub(r'\([^)]*\)', '', title)
        # enregiste uniquement les 84 premièrs caractères des titres trop longs
        title = title[:84] 

        cat_lis = book_info_soup.find('ul', class_="breadcrumb").contents[5].find('a')
        cat_name = cat_lis.string.replace(' ', '-')

        # Nettoyer l'url des images pour la rendre consultable
        img_url = book_info_soup.find("div", class_="item active").find_next('img').get('src')
        img_url = img_url.replace('../../', 'http://books.toscrape.com/')

        # Si un livre ne possède pas de description, remplacer sa valeur par 'Not Found'
        try:
            product_description = book_info_soup.find('div', id="product_description").find_next('p').next_element
        except AttributeError:
            product_description = "Not Found"
        
        # Récupérer la deuxième valeur de la classe "instock availability"
        review_rating = book_info_soup.find("p", class_="instock availability").find_next('p').get('class')[1]
        # Transformer les lettres en chiffres
        rating_numbers = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
        for key, value in rating_numbers.items():
            if review_rating in key:
                review_rating = review_rating.replace(review_rating, str(value))
        review_rating = review_rating

        category_name = cat_name
        image_url = img_url
        url_livre = the_link
        product_description = cls(str(product_description), ['—', '--', '"', '-'], ' ')
        the_books_list = url_livre,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,category_name,review_rating,image_url,product_description
        return the_books_list

# Enregistrer les informations de chaque livre dans le fichier csv ainsi que chaque image dans le dossier de sa catégorie
def write_infos(the_books_list):
    f = open(f'infos.csv', 'a', encoding="utf-8", newline="")
    with f:
        fnames = ['url_livre','universal_product_code','title','price_including_tax','price_excluding_tax','number_available','category_name','review_rating','image_url','product_description']
        my_dict = {'url_livre':the_books_list[0],'universal_product_code':the_books_list[1],'title':the_books_list[2],'price_including_tax':the_books_list[3],'price_excluding_tax': the_books_list[4],'number_available':the_books_list[5],'category_name':the_books_list[6],'review_rating':the_books_list[7],'image_url':the_books_list[8],'product_description':the_books_list[9]}
        writer = csv.DictWriter(f, fieldnames=fnames, delimiter=";")
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow(my_dict)
        print(f'{the_books_list[2]} de la catégorie {the_books_list[6]}')
    os.chdir(f'images')
    titre = the_books_list[2]
    if not os.path.exists(f"{titre}.jpg"):
        with open(f"{titre}.jpg", "wb") as f:
            im = requests.get(the_books_list[8])
            f.write(im.content)

# Créer le dossier qui regroupe toutes les informations du site books.toscrape.com
def website_create_folders(tfold, cat_list_tt):
    print('Veuillez patienter, création du dossier tout_le_site\n')
    # Create the tout_le_site folder and its tout_le_site_titles folders
    if not os.path.exists('tout_le_site'):
        os.chdir('downloads')
        os.mkdir('tout_le_site')
    else:
        print("Le dossier existe déjà")
    
    time.sleep(3)
    print("Création des dossiers de catégories\n")
    os.chdir('tout_le_site')
    for title in cat_list_tt:
        if not os.path.exists(title):
            os.mkdir(title)
        else:
            print(f'le dossier {title} existe déjà')
    
    time.sleep(3)
    print("Création des fichiers csv et des dossiers d'image\n")
    # Create the csv files into each category_title folder
    for fold in os.listdir(tfold):
        os.chdir(f'{tfold}/{fold}')
        os.getcwd()
        if not os.path.exists("images"):
            os.mkdir("images")
        else:
            print("le fichier spécifié existe déjà")
        cmd = f"echo product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;category;review_rating;image_url;product_description > infos.csv"
        os.system(cmd)
    time.sleep(3)
    print('les dossiers et fichiers ont été crées\n')
    time.sleep(2)
    print("maintenant veuillez patienter quelques minutes le temps de la récolte des données\n")
    os.chdir('../')