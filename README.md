# P2_WEBSCRAPPING

## TELECHARGEMENT DU PROJET DEPUIS GITHUB

Vous êtes à présent sur le dossier du "programme d'extraction des prix" du site books.toscrape.com
pour le télécharger, il vous suffit de cliquer à droite sur le bouton "code".
Le plus simple est de télécharger sa version ZIP, donc cliquez sur Download ZIP

---
---

## INSTALLATIONS

**Vous n'avez pas installé python 3 ?**

- rendez-vous [sur le site](https://www.python.org/downloads/) et télécharger la dernière version de python
- Cocher la case 'Add Python 3.9 to PATH'. Cette version installe automatiquement pip, qui va nous être très utile pour la suite.
- Le reste se fait tout seul.
- Pour une installation sur mac, il suffit de faire la même chose que pour windows 10 et installer comme tout logiciel que vous
- pourriez installer sur votre mac

    > Vous pouvez utiliser "vscode", l'un des plus puissants éditeurs de code qui   simule une ligne de commande, mais je vous conseille plus d'utiliser votre ligne de commande Windows ou Mac

**Une fois le dossier téléchargé!**

- ***Récupérez*** le, faites un copier coller de votre dossier de téléchargement jusqu'à un dossier de votre choix, de préférence vierge.
- ***décompressez*** le fichier ZIP
- ***Ouvrez*** le dossier qui contient désormais:
  - Un dossier " *projet* " qui contient tous les scripts
  - Un fichier " *.gitignore* "
  - Un fichier " *menu_principal.py* " qui permet de lancer le projet
  - Le fichier " *README.md* " que vous êtes actuellement en train de lire
  - Ainsi qu'un fichier " *requirements.txt* " qui contient toutes les librairies necessaires à l'exécution du projet que vous devez installer.

**Ouvrez maitenant votre ligne de commande**
Pour y accéder:

- Sous windows, Appuyez simultanément sur les touches Win + r
- Une fenêtre intitulée Exécuter s'affiche : tapez cmd puis Entrée
- Sous Mac rendez-vous dans le dossier "Applications", puis dans "Utilitaires"
- Vous n'avez plus qu'à l'ouvrir comme n'importe quelle autre application
- Accéder au dossier du projet
  - tapez "cd nom_du_dossier"
  - la commande cd permet de passer d'un dossier à l'autre et chaque dossier est séparé par un '/'
  - Pour revenir au dossier précédent, il suffit de taper 'cd ../'

---

    Tapez dans le terminal:
    ` python3 -m venv (nom de l'environnement virtuel) `

---

    Activez votre environnement virtuel en tapant ces deux commandes:
    ` cd (nom de l'environnement virtuel)/Scripts `
    ensuite tapez:
    ` activate.bat `

---

    Revenez dans le dossier du projet:
    ` cd ../../ `

---

    Installer 'pip':
    ` pip install pip `

---

    Installer les dépendances du fichier requirements.txt:
    `pip install -r requirements.txt`

---

    Puis vérifier si toutes les dépendance sont installées:
    `pip freeze`
Exemple de retour

    `
        beautifulsoup4==4.9.3
        certifi==2021.5.30
        chardet==4.0.0
        idna==2.10
        lxml==4.6.3
        requests==2.25.1
        soupsieve==2.2.1
        urllib3==1.26.5
    `
---
---

## LANCEMENT DU PROJET

**Pour lancer le projet:**

- Dans le terminal, tapez, selon le mot clé de déclenchement des scripts python autorisé:
`python3 menu_principal.py`
ou
`python menu_principal.py`
ou
`py menu_principal.py`

**Ouvrir le menu principal, déclenche la création d'un dossier 'downloads':**

- Dans ce dossier, deux dossiers:
  - Le dossier books, dans lequel sera stocké chaque image et informations de livre que vous allez télécharger
  - Le dossier catégories:
    - Dans lequel un dossier sera crée pour chaque catégorie téléchargée
      - le dossier créé portera le nom de la catégorie
      - à l'intérieur de ce dossier sera aussi créé un fichier csv contenant les informations de chaque livre
      - ainsi qu'un dossier images qui contiendra l'image de chaque livre de la catégorie
  - Le dossier site:
    - Sera seulement créé si vous téléchargez tout le contenu du site

---
---

## **LE MENU PRINCIPAL**

**Télécharger le livre avec son url:**

- renseignez l'url du livre que vous voulez télécharger
- le dossier portant le nom du livre est créé dans "downloads/books/"
  - il contient maintenant l'image du livre et un fichier csv contenant toutes ses informations

**Télécharger les livres d'une catégorie avec son url:**

- renseignez l'url de la catégorie à télécharger
- le dossier de la catégorie portant son nom est créé dans "downloads/categories"
  - ce dossier contient un fichier url regroupant les infos de tous les livres de la catégorie
  ainsi qu'un dossier regroupant les images de tous les livres de la catégorie

**Télécharger toutes les informations du site:**

- le téléchargement se déclenche directement dès la validation de l'option
- un dossier est directement créé dans "download"
  - Ce dossier créera un dossier par catégorie
  - Chaque dossier de catégorie contiendra
    - un fichier csv contenant les informations de chaque livre de cette catégorie
    ainsi qu'un dossier contenant les images de chaque livre de cette catégorie
