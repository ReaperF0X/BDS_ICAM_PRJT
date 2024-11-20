BDS ICAM - Gestion des Événements
  Ce projet est une application web développée pour le Bureau des Sports (BDS) de l'ICAM Strasbourg-Europe. Elle permet aux étudiants de consulter, créer, gérer et s'inscrire à divers événements proposés par l'école.


Fonctionnalités principales
  Gestion des comptes utilisateurs :
    Inscription avec vérification des e-mails ICAM.
    Connexion sécurisée avec mot de passe.
    Modification du profil, ajout de photo de profil.
  
  Gestion des événements :
    Consultation des événements disponibles avec options de recherche et filtres par discipline.
    Création et gestion d'événements par les utilisateurs.
    Visualisation des participants inscrits à un événement.
  
  Esthétique moderne et ergonomique :
    Respect de la charte graphique (couleurs bleu et jaune).
    Design responsive pour une utilisation agréable sur tous les appareils.

Technologies utilisées
  Backend :
    Django 5.0.6
    Python 3.12.2
  Base de données :
    MySQL (via WAMP Server)
  Frontend :
    HTML, CSS
  Autres :
    WAMP Server pour l'environnement local.
    Django ORM pour les interactions avec la base de données.

Installation et exécution
  Prérequis
    Python installé (3.8 ou version ultérieure).
    WAMP Server (ou un serveur compatible avec MySQL).
    Git pour la gestion de version.

Étapes
  
  Clonez le projet :
    git clone https://github.com/<votre-utilisateur>/BDS_ICAM.git
    cd BDS_ICAM
  
  Créez un environnement virtuel et activez-le :
    py -m venv env
    env\Scripts\activate
  
  Installez les dépendances :
    pip install -r requirements.txt
  
  Configurez la base de données :
    Importez le fichier SQL (bds_icam_db.sql) dans votre MySQL via phpMyAdmin.

  Appliquez les migrations :
    python manage.py makemigrations
    python manage.py migrate

  Lancez le serveur de développement :
    python manage.py runserver

  Accédez à l'application :
    Ouvrez un navigateur et rendez-vous sur : http://127.0.0.1:8000


Structure du projet

BDS_ICAM_PRJT/
│
├── BDS_ICAM/                # Application principale
│   ├── settings.py          # Configuration du projet Django
│   ├── urls.py              # Routes principales
│   ├── ...
│
├── events/                  # Application pour la gestion des événements
│   ├── models.py            # Définition des modèles (Event, User, etc.)
│   ├── views.py             # Logique des vues
│   ├── urls.py              # Routes spécifiques à l'application
│   ├── templates/           # Templates HTML
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── ...
│   └── static/              # Fichiers statiques (CSS, images)
│
├── media/                   # Stockage des fichiers uploadés (photos, illustrations)
│
├── manage.py                # Point d'entrée pour les commandes Django
└── README.md                # Fichier d'information (vous lisez ceci)


Sécurité
  Les mots de passe sont hachés et sécurisés.
  Utilisation des jetons CSRF pour prévenir les attaques Cross-Site Request Forgery.
  Accès administrateur limité aux super-utilisateurs via /admin.

Créer un super utilisateur :
  python manage.py createsuperuser

Appliquer les migrations pour la base de données :
  python manage.py makemigrations
  python manage.py migrate









  
