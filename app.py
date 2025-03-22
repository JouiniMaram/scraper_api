from flask import Flask, jsonify, request
import threading
import time

app = Flask(__name__)

# Liste simulée des annonces collectées
annonces = [
    {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23229/thumbs/th_occasion-a-ne-pas-rater_used_01742231587.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/occasion-a-ne-pas-rater-23229",
    "Prix": "Prix : 71 000 DT",
    "Titre": "Occasion \u00e0 ne pas rater",
    "Transmission": "Automatique",
    "\u00c9tat": "Etat : Neuf"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23228/thumbs/th_peugeot-3008-premium-blanc-nacre_used_01742210763.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/peugeot-3008-premium-blanc-nacre-23228",
    "Prix": "Prix : 40 000 DT",
    "Titre": "Peugeot 3008 Premium Blanc Nacr\u00e9",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Excellent"
  },
  {
    "Carburant": "Diesel",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23227/thumbs/th_207-peugeot_used_01741816895.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/207-peugeot-23227",
    "Prix": "Prix : 26 000 DT",
    "Titre": "207 Peugeot",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Tr\u00e8s bon"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23226/thumbs/th_suv-volvo-xc60-finition-r-design-tout-option-en-excellent-etat_used_01740710023.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/suv-volvo-xc60-finition-r-design-tout-option-en-excellent-etat-23226",
    "Prix": "Prix : 45 000 DT",
    "Titre": "SUV - Volvo XC60 finition R-Design , tout option , en excellent etat",
    "Transmission": "Automatique",
    "\u00c9tat": "Etat : Excellent"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23224/thumbs/th_belle-ford-kuga_used_01740254835.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/belle-ford-kuga-23224",
    "Prix": "Prix : 73 000 DT",
    "Titre": "Belle Ford kuga",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Excellent"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23223/thumbs/th_belle-occasion-1ere-main-avec-historique-des-visites-chez-giat_used_01739199084.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/belle-occasion-1ere-main-avec-historique-des-visites-chez-giat-23223",
    "Prix": "Prix : 28 000 DT",
    "Titre": "Belle occasion. 1\u00e8re main, avec historique des visites chez Giat",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Bon"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23222/thumbs/th_tiggo-7-pro_used_01739189974.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/tiggo-7-pro-23222",
    "Prix": "Prix : 93 000 DT",
    "Titre": "TIGGO 7 PRO",
    "Transmission": "Automatique",
    "\u00c9tat": "Etat : D\\'origine"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23221/thumbs/th_peugeot-3008_used_01738494934.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/peugeot-3008-23221",
    "Prix": "Non sp\u00e9cifi\u00e9",
    "Titre": "Peugeot 3008",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Bon"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23220/thumbs/th__used_01738159230.png",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/a-vendre-toyota-rav-4-occasion-en-tres-bon-etat-23220",
    "Prix": "Prix : 56 000 DT",
    "Titre": "\u00c0 vendre Toyota RAV 4 occasion en tr\u00e8s bon \u00e9tat",
    "Transmission": "Automatique",
    "\u00c9tat": "Etat : Excellent"
  },
  {
    "Carburant": "Essence",
    "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23219/thumbs/th_peugeot-308-en-excellent-etat-fin-2012_used_01737900551.jpeg",
    "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/peugeot-308-en-excellent-etat-fin-2012-23219",
    "Prix": "Prix : 24 000 DT",
    "Titre": "Peugeot 308 en excellent etat Fin 2012",
    "Transmission": "Manuelle",
    "\u00c9tat": "Etat : Tr\u00e8s bon"
  }
]

def start_scraping():
    """Fonction simulant le démarrage du scraping."""
    print("Début du scraping...")
    time.sleep(5)  # Simule une opération longue de scraping
    print("Scraping terminé!")

@app.route('/annonces', methods=['GET'])
def get_annonces():
    """Retourne toutes les annonces collectées."""
    return jsonify(annonces)

@app.route('/scrape', methods=['POST'])
def scrape():
    """Lance une nouvelle session de scraping."""
    # Lance le scraping dans un thread séparé pour ne pas bloquer le serveur
    threading.Thread(target=start_scraping).start()
    return jsonify({"message": "Scraping lancé. Vous serez informé lorsque le processus sera terminé."})

if __name__ == '__main__':
    app.run(debug=True)
