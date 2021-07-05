import subprocess as sb
import time
import os


# Création des dossiers de sauvegarde
if not os.path.exists('downloads/books'):
    os.makedirs('downloads/books')
if not os.path.exists('downloads/categories'):
    os.makedirs('downloads/categories')


print("Vous souhaitez télécharger un livre par son url, tapez la commande 'livre'")
print()
print("Vous souhaitez télécharger une catégorie par son url, tapez la commande 'categorie'")
print()
print("(récupération longue) - Vous souhaitez télécharger toutes les informations du site tapez la commande 'site'")
print()
print("Pour sortir du menu principal, tapez 'fin'")
print()

search = input("Tapez ici votre commande => ")

if search.lower() == "site":
    print('Veuillez patienter, cela peut prendre un certain temps')
    sb.call('py projet/my_scripts/get_the_site.py 1', shell=True)
elif search.lower() == "categorie":
    sb.call('py projet/my_scripts/get_category.py 1', shell=True)
elif search.lower() == "livre":
    sb.call('py projet/my_scripts/get_book.py 1', shell=True)
elif search.lower() == 'fin':
    print()
    print('Au revoir')
else:
    print("Veuillez s'il vous plait taper les commandes 'disponibles' ?")
    time.sleep(2)
    sb.call('py menu_principal.py 1', shell=True)
