# Projet de Web Scraping : Annonces Immobilières et Véhicules en Tunisie

Ce projet permet de collecter des annonces immobilières et de véhicules d'occasion en Tunisie en utilisant des techniques de **web scraping**. L'application expose une **API REST** qui permet de récupérer les annonces collectées et de lancer une nouvelle session de scraping.

## Fonctionnalités

L'application expose les deux endpoints suivants :

- **GET /annonces** : Retourne toutes les annonces collectées dans un format JSON.
- **POST /scrape** : Lance une nouvelle session de scraping pour collecter des annonces récentes.

### Exemple de données retournées par `/annonces` :

```json
[
  {
    "Titre": "Occasion à ne pas rater",
    "Prix": "Prix : 71 000 DT",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/occasion-a-ne-pas-rater-23229",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23229/thumbs/th_occasion-a-ne-pas-rater_used_01742231587.jpeg",
    "Carburant": "Essence",
    "Transmission": "Automatique",
    "État": "Etat : Neuf"
  },]
  ...

####Installer les dépendances
pip install -r requirements.txt


Dépendances:
Flask : Framework web léger pour construire des applications web.

requests : Bibliothèque pour effectuer des requêtes HTTP.

BeautifulSoup4 : Utilisé pour parser le HTML et extraire les informations des pages.

Selenium : Permet de contrôler un navigateur pour simuler des interactions avec des pages web dynamiques.

undetected-chromedriver : Permet d'utiliser Selenium avec Chrome sans être détecté par le site.

Lancer l'application:
python app.py
-> Le serveur sera accessible sur http://127.0.0.1:5000/annonces