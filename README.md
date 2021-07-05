'TELECHARGEMENT DU DOSSIER GITHUB'
# INSTALLATIONS ET LANCEMENT DU PROJET

Vous devez installer python 3 si vous ne l'avez pas encore fait
    - Vous devez vous rendre sur le site ` https://www.python.org/downloads/ ` et télécharger la dernière versionde python
    - Cocher la case 'Add Python 3.9 to PATH'. Cette version installe automatiquement pip, qui va nous être très utile pour la suite.
    - Le reste se fait tout seul.
    - Pour une installation sur mac, il suffit de faire la même chose que pour windows 10 et installer comme tout logiciel que vous
    - pourriez installer sur votre mac

Vous pouvez utiliser n'importe quel éditeur de code pour exécuter le projet.

## Lorsque vous démarrez, vous devez avoir uniquement

    - Un dossier projet, qui contient tous les scripts
    - Des fichiers (.gitignore, requirements.txt, README.MD et menu_principal.py)
    - Logiquement vous allez vous servir uniquement du fichier "menu_principal.py"
    - Mais avant cela, nous allons passer à l'installation des outils necessaires au démarrage du projet.

## Environnement virtuel et fichier requirements

Si votre IDE possède un terminal permettant d'utiliser la ligne de commande, utilisez la.
Sinon, utilisez directement la ligne de commande.

Pour y accéder:
    - Sous windows, Appuyez simultanément sur les touches Win + r
    - Une fenêtre intitulée Exécuter s'affiche : tapez cmd puis Entrée
    - Sous Mac rendez-vous dans le dossier "Applications", puis dans "Utilitaires"
    - Vous n'avez plus qu'à l'ouvrir comme n'importe quelle autre application

Une fois dans la ligne de commande:
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
Retour

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

## LANCEMENT DU PROJET

### **A cette étape, vous devez avoir**

    - Un dossier 'projet'
    - votre 'environnement virtuel'
    - le fichier 'menu_principal.py'
    - le fichier 'README.md'
    - ainsi que le fichier 'requirements.txt'

    Dans le terminal, tapez:
    `python3 menu_principal.py`
    ou
    `python menu_principal.py`
    ou
    `py menu_principal.py`

### **Ouvrir le menu principal, déclenche la création d'un dossier 'downloads'**

    - Dans ce dossier, deux dossiers:
      - Le dossier books, dans lequel sera stocké chaque image et informations de livre que vous allez télécharger
      - Le dossier catégories:
        - Dans lequel un dossier sera crée pour chaque catégorie téléchargée
          - le dossier créé portera le nom de la catégorie
          - à l'intérieur de ce dossier sera aussi créé un fichier csv contenant les informations de chaque livre
          - ainsi qu'un dossier images qui contiendra l'image de chaque livre de la catégorie
      - Le dossier site:
        - Sera seulement créé si vous téléchargez tout le contenu du site

## LES MENUS

### **LE MENU PRINCIPAL**

#### Télécharger le livre avec son url (procésus rapide)

      - renseignez l'url du livre que vous voulez télécharger
      - le dossier portant le nom du livre est créé dans "downloads/books/"
        - il contient maintenant l'image du livre et un fichier csv contenant toutes ses informations

#### Télécharger les livres d'une catégorie avec son url

      - renseignez l'url de la catégorie à télécharger
      - le dossier de la catégorie portant son nom est créé dans "downloads/categories"
        - ce dossier contient un fichier url regroupant les infos de tous les livres de la catégorie
        ainsi qu'un dossier regroupant les images de tous les livres de la catégorie

#### Télécharger toutes les informations du site

      - le téléchargement se déclenche directement dès la validation de l'option
      - un dossier est directement créé dans "download"
        - Ce dossier créera un dossier par catégorie
        - Chaque dossier de catégorie contiendra
          - un fichier csv contenant les informations de chaque livre de cette catégorie
          ainsi qu'un dossier contenant les images de chaque livre de cette catégorie

    Une fois toutes les informations téléchargés, vous êtes automatiquement redirigés vers un menu 
    pour accéder à ces informations. 
  
#### Télécharger le livre avec son titre, son upc ou son url (procésus long)

      - Pour récupérer gràce au titre, récupérer uniquement la partie du titre avant les ":", si le titre en est composé
      - Ici, vous pouvez télécharger les informations d'un livre en renseignant soit son 'titre', soit son 'upc', soit son 'url'
      - ce procéssus est plus long car notre script parcours chaque page du site jusqu' à trouver une correspondance entre
        - le renseignement fournit par l'utilisateur et les renseignements du livre recherché
      - ceci étant, le livre téléchargé ira directement dans "downloads/books".
      - Mon script

### **LE MENU D'ACCES AUX INFORMATIONS TELECHARGEES**

#### Afficher les informations d'un livre grâce à une de ses informations

    - Entrez directement une des informations du livre dont vous souhaitez afficher les informations
    - Aucun dossier n'est créé, les informations sont justes affichées

#### Afficher les informations d'un ou plusieurs livres depuis sa catégorie

    - repérez le nom de la catégorie concernée et renseignez la
    - tous les livres de la catégorie sont affichés
    - repérez ensuite le livre dont vous souhaitez afficher les informations
    - copier et coller une des infos du livre dont vous souhaitez afficher toutes les infos
    - Aucun dossier n'est crée, les informations sont justes affichées
