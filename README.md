# MY_API

**Description** 

Ce projet consiste à créer une API sécurisée RESTful .

**Prérequis**

Il est nécessaire d'avoir Python 3.7 et Git installé sur le PC.

**Installation**

1. Dans la console Git, choissisez l'emplacement où vous voulez cloner le projet
2. Exécuter  ``` git clone https://github.com/jaikko/MY_API.git ```
3. Ensuite, se rendre dans le projet avec ``` cd MY_API ```
4. Installer l'environnement virtuel en éxécutant ``` python -m venv env ```
5. Activer le avec la commande   ``` source env/Scripts/activate ```
6. Installer les modules avec  ```pip install -r requirements.txt ```
7. Créer la base de données en exécutant ``` python manage.py makemigrations ``` puis ``` python manage.py migrate ```
8. Lancez le serveur avec la commande ```python manage.py runserver```

**Utilisation**

L'API est accessible via cette url: http://127.0.0.1:8000. Par exemple, pour se s'inscrire, utuiliser http://127.0.0.1:8000/signup
