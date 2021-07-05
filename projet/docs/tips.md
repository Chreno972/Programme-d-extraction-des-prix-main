# TUTO WEBSCRAPPING

Pour faire du webscrapping avec Python:

on importe tout d'abord requests et bs4 'beautifulSoup'

    `import requests
     from bs4 import BeautifulSoup`

Ensuite, on stock l'url choisie dans une variable:

    `url = 'http://feeds.bbci.co.uk/news/rss.xml'`

On va chercher une réponse de l'url

    `response = requests.get(url)`

Ensuite, on utilise bs pour récupérer des éléments:

    `if response.ok:
        soup = BeautifulSoup(response.text)
        tds = soup.findAll('td')
        print(len(tds))
        [print(f'{td}\n\n') for td in tds]`

Ici on cherche si le site possède des td (table div)

---

Pour récupérer un attribut avec python, par exemple:

    `a = td.find('a')
     link = a[]`

par exemple href, src etc.

---

On peut le faire aussi si il existe plusieurs balises td à rechercher sur le site

    `for td in tds:
        a = td.find(a)
        link = a['href']`

---

Avec BeautifulSoup, on peut rechercher des balises imbriquées:

    `soup = BeautifulSoup(response.text)
     country = soup.find('tr', {'id': 'places_country_row'}).find('td', {'class': 'w2p_fw})`

Ou bien:

    `categories_content = soup.select("li > ul > li > a")`

Ici, on cherche une balise td de classe... imbriquée dans une balise tr d'id...

---

Nettoyer une balise avec beautifulSoup

    `soup = BeautifulSoup(response.text)
    h = soup.find('h1').text`

    replacements = ['<h1>', '</h1>', '(', ')', '#', ':']

    `for item in replacements:
        if item in h:
            h = str(h).replace(item, '')
    print(h)`

---

Extraire tout le texte de la page

    `soup.get_text().replace('\n', '-')`

---

Extraire toutes les urls du site

    `for link in soup.findAll('a'):
        links = link.get('href')`

---

Afficher toutes les classes des balises paragraphes de la page

    `all_classes = [print(classes.get('class')) for classes in soup.findAll('p')]`

---

Utiliser les expressions régulières pour extraire les chiffres ou nombres dans une string

    `find_number = re.findall('\d+', string_to_work)`

    l'expression régulière 
        => d = prends tous les nombres entre [0-9]
        => + = sélectionne un ou plus d'item de l'expression régulière

---

Combiner les méthodes 'dict' et 'zip' pour créer un dictionnaire à partir de deux listes

    `
        cat_list_links = ['name', 'age', 'profession']
        cat_list_titles = ['thomas', 42, 'sousseuw de kyou']

        book_dict = dict(zip(cat_list_titles, cat_list_links))

        # returns => {'name':'thomas', 'age':42, 'profession':'sousseuw de kyou'}
    `

---

Préparer correctement l'ouverture d'un fichier CSV avec la bibliothèque 'os'

    `
    import os
    
    if not os.path.isfile('projet.csv'):
        print("Le fichier n'existe pas !")
    else:
        print("Le fichier existe")
        try:
            projet = open("projet.csv", 'r', encoding="utf-8")
        except:
            print("Erreur lors de l'ouverture du fichier !")
        else:
            print("Fichier ouvert : le traitement va commencer...")
            # Lire les données
            ******
            # Traiter les données
            ******
            # Fermer le fichier
            projet.close()`

---

Utiliser la bibliothèque os pour manipuler les dossiers

    `
    import os
    os.getcwd()
    if not os.path.exists('category'):
        os.mkdir('category')
    `
    Cela récupère l'adresse de l'environnement de développement, check si un document existe, s'il n'existe pas, cela crée le dossier spécifié grace à mkdir

---

Enregistrer un document dans un autre grace à 'os' et 'os.path'

    `
    import os
    import os.path

    os.getcwd()
    if not os.path.exists('category'):
        os.mkdir('category')

    os.path.join('category', 'books')
    `

---

Créer un dossier, entrer dans ce nouveau dossier et créer plusieurs dossiers à l'intérieur avec 'os' et 'os.path'

    `
    import os
    import os.path

    caracar = ['ererer', 'ezerazdqdf', 'dsfsdfoiqsudfqsdf', 'qsdfqsdfsdfhalekha']

    os.getcwd()
    if not os.path.exists('category'):
        os.mkdir('category')
        
    os.chdir('category')
    os.getcwd()

    for cac in caracar:
        if not os.path.exists(cac):
            os.mkdir(cac)
    `
---

Créer un fichier avec les bibliothèques "os" et "os.path"

    `
        os.chdir('category')
        os.getcwd()
        cmd = f"echo. > lacreation.csv"
        os.system(cmd)
    `

---

Utiliser 'time' et effectuer une requête vers plusieurs urls avec paramètres

    `
        for url in urls:
            page = ''
            while page == '':
                    try:
                            page = requests.get(url, verify=False)
                            break
                    except:
                            print("Connection refused by the server..")
                            print("Let me sleep for 5 seconds")
                            print("ZZzzzz...")
                            time.sleep(5)
                            print("Was a nice sleep, now let me continue...")
                            continue

            if page.ok:
                    soup = BeautifulSoup(page.text, 'html.parser')
                    print(str(soup))
    `
---

Boucler sur un dictionnaire

    `
        lettres = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
        for key, value in lettres.items():
            print (value)
    `
---

Passer un chiffre écrit en toutes lettres en int
    pratique quand l'on trouve une valeur en lettre mais que l'on souhaite avoir un chiffre à la place

    `
        lettre = 'five'
        lettres = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
        for key, value in lettres.items():
            if lettre in key:
                print (value)
    `

---

Trouver le texte contenu dans une balise
    Ce code retourne l'élément qui se trouve directement entre l'ouverture et la fermeture de sa balise parente

    `
        product_description = book_info_soup.find('div', id="product_description").find_next('p').next_element
    `

---

Créer un dossier, puis plusieurs dossiers et créer un dossier dans chaque dossier avec "os"
    Difficultés ici, le chemin doit être entièrement spécifié pour pouvoir boucler dedans, de plus, on doit changer tous les " \ " en " / "

    `
        os.mkdir('test_multi')
        os.chdir('test_multi')
        for i in range(10):
            os.mkdir(str(i))
        test_multi = 'C:/Users/Christophe/Desktop/Formations-projets/OC Learning/TRAININGS/Projet2_analyse_de_marche/test_multi'
        for element in os.listdir(test_multi):
            os.chdir(f'{test_multi}/{element}')
            os.getcwd()
            os.mkdir('close')
    `

---

Retirer tous les espaces à gauche et à droite des lettres d'une string avec strip()

    `
        s = '    abc def    \n\n'
        print(s.strip())
        l'avantage avec ça, c'est que ça retire les espaces uniquement partant des deux côtés des mots et ça retire même les sauts de ligne
        cela retourne 'abc def'
    `

---

Capitaliser la première lettre de chaque mot d'une string avec strip()

    `
        s = '    abc def    \n\n'
        print(s.strip())
        l'avantage avec ça, c'est que ça retire les espaces uniquement partant des deux côtés des mots et ça retire même les sauts de ligne
        cela retourne 'abc def'
    `

---

Créer un environement virtuel
    Dans le dossier de projet, pour windows, utiliser la ligne de commande !!!! Pas powershell, ni gitbash ou autre, sinon vous risquez de
    vous arracher les cheveux en temptant d'activer votre environement virtuel
    `py -m venv "nom_du_venv"`
    Le plus simple c'est de toujours nommer ses environement virtuels 'env' pour éviter de se perdre si l'on travaille sur plusieurs projets
Pour l'activer
    `cd env/Scripts`, puis `activate.bat`
Pour le désactiver
    `deactivate`
Pour le supprimer (de manière récursive)
    `rm -r env/` "ne marche pas sur la command line (rm n'est pas reconnu)" pour la cmd il faut faire rmdir tout simplement plus le nom
    du dossier à supprimer

---

Créer un fichier requirements.txt
    dans le dossier du projet ou de projet contenant l'environnement virtuel, taper dans le terminal
    `pip freeze > requirements.txt`
    Le fichier sera automatiquement créé
Pour au contraire, installer les dépendances inscrites dans le fichier
    dans le dossier
    `pip install -r requirements.txt`
    Et cela va installer automatiquement toutes les dépendances nécessaires au projet en cours

---

Lancer un fichier depuis un autre fichier
    `import subprocess`
    `subprocess.call('py fichier.py 1', shell=True)`

---

Utiliser "try / except" afin de continuer une boucle en cas d'erreur ou d'impossibilité de récupérer une information d'une liste d'éléments à récupérer

    `
    try:
        product_description = book_info_soup.find('div', id="product_description").find_next('p').next_element
    except AttributeError:
        product_description = "Not Found"
    `
    En gros, je devais afficher toutes les informations contenues dans la variable product_description, cependant, une de ces infos étaient manquantes dans
    le squelette HTML du site. Du coup, une erreur m'était retournée dès que la boucle arrivait au niveau de cette information manquante. Du coup,
    la meilleure manière pour éviter ce genre d'erreur est d'utiliser la méthode "try / catch". Simple, rapide et efficace

---

Effacer une partie du texte et ne récupérer qu'une partie avec la méthode
split()
    `separateur = ':'`
    `textes = texte.split(séparateur, 1)[0]`

    Ici, je ne récupère que la première partie du texte, plus précisément, 
    ce qui est écrit avant le séparateur pas besoin de conditions

---

Enlever les parenthèses à l'intérieur d'une string avec la bib regex
    `title = re.sub(r'\([^)]*\)', '', title)`

---

Conditionner l'écriture ou l'ouverture d'un fichier csv avec 'csv.excel_tab'
    `writer = csv.DictWriter(f, fieldnames=fnames, dialect=csv.excel_tab)`
    `writer = csv.writer(f, dialect=csv.excel_tab)`
    `reader = csv.DictReader(f, fieldnames=fnames, dialect=csv.excel_tab)`
    `reader = csv.reader(f, dialect=csv.excel_tab)`

    Cela créera des lignes dont les colonnes sont séparées par des tabulations

---

Parourir les éléments d'une fonction
    On créé tout d'abord une fonction
    `def uneFonction(argument):`
        `variable0 = action0`
        `variable1 = action1`
        `variable2 = action2`
        `return [variable1,variable2]` => en gros [index0, index1, etc...]
    du coup le return met les variables à retourner dans un tableau, et on y
    accède comme cela
    `fonc(arg)[index_return]`
    `uneFonction(argument)[0]`

---

Certaines fois, dans les chaines de caractère, il se peut que certaines
lettres ne soient pas encodables, du coup, dans mes chaines de caractère,
j'avais des espèces de 'â' et points d'interrogation de couleur noire. J'ai fini
par trouver un moyen de les supprimer tout est expliqué ici
'https://docs.python.org/fr/3.7/howto/unicode.html'

il m'a suffit de faire des recherches pour trouver le code de ces caractères
puis faire un replace multiple définit dans la fonction "cls"
    `cls(chaine_de_caractère, ['â','\x80','\x99', "'''"], '')`

---

Rendre un fichier csv lisible dans excel et formaté en liste colonne
    Le fait de simplement mettre 'delimiter=";"' sépare les chaque élément par un ";"
    Dans Excel, cela représente la fin d'une colonne. Du coup, avec Excel on aura un
    jeu de données bien classé en colonnes et en ligne
    `writer = csv.DictWriter(f, fieldnames=fnames, delimiter=";")`

---

Récupérer des éléments présents sur plusieurs pages d'une catégorie
    `

    url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
    urls = []
    new_url = []
    urls.append(url)
    try:
        for i in range(2,9):
            uri = url.replace('index', f'page-{i}')
            status_code = requests.get(uri)
            if status_code.ok:
                urls.append(uri)
    except:
        pass
    for urx in urls:
        status_code = requests.get(urx)
        if status_code.ok:
            new_url.append(urx)
    `
---

Modifier une chaine de caractère (phrase) pour ne récupérer qu'une partie de celle_ci
    `txt = "welcome to the jungle`
    `x = txt.split(" ")`=> ['welcome', 'to', 'the', 'jungle']
    `splitted = x[:3]`=> ['welcome', 'to', 'the']
    `y = " ".join(splitted)`=> welcome to the
    `z = y + '...'`=> welcome to the...

    Cette méthode est efficace quand l'on connait exactement le nombre maximal de lettres de chaque chaine de caractères

---

Quand mettre un return à la fin d'une fonction ?

Il est obligatoire de mettre un return à la fin d'une fonction, quand la variable que nous voulons utiliser par la suite
n'a pa s été déclarée au préalable avant la fonction. Par exemple, si on a déclaré une liste au début de notre code et
qu'à la moitié du code on appelle une fonction qui va utiliser cette liste pour stocker des calculs, nous n'avons pas à
mettre un return de cette liste car son résultat sera automatiquement mis à jour si l'on l'appelle après cette fonction.
Elle nous retournera le résultat quoi qu'il en soit.

En revanche, si la liste est créée dans la fonction, nous devons retourner cette dernière à la fin de la fonction pour
que l'on puisse la récupérer par la suite. En python, on peut récupérer un return comme l'élément d'une liste.
> **par exemple pour récupérer l'une des valeurs d'un return multiple**
    return [one,two,three]
    => `one = lafonction(argument)[0]`
    => `two = lafonction(argument)[1]`
