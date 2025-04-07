from flask import Flask, jsonify, request
import threading
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser les requêtes CORS pour Dash

# Liste simulée des annonces collectées
annonces = [
    {
        "Carburant": "Essence",
        "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23229/thumbs/th_occasion-a-ne-pas-rater_used_01742231587.jpeg",
        "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/occasion-a-ne-pas-rater-23229",
        "Prix": "Prix : 71 000 DT",
        "Titre": "Occasion à ne pas rater",
        "Transmission": "Automatique",
        "État": "Etat : Neuf"
    },
    {
        "Carburant": "Essence",
        "Image": "https://www.auto-plus.tn/assets/modules/usedcars/23228/thumbs/th_peugeot-3008-premium-blanc-nacre_used_01742210763.jpeg",
        "Lien": "https://www.auto-plus.tn/voitures-d-occasion/a_vendre/peugeot-3008-premium-blanc-nacre-23228",
        "Prix": "Prix : 40 000 DT",
        "Titre": "Peugeot 3008 Premium Blanc Nacré",
        "Transmission": "Manuelle",
        "État": "Etat : Excellent"
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

@app.route('/annonces_json', methods=['GET'])
def get_annonces_json():
    """Retourne les annonces au format JSON pour Dash."""
    return jsonify({"annonces": annonces})

@app.route('/scrape', methods=['POST'])
def scrape():
    """Lance une nouvelle session de scraping."""
    threading.Thread(target=start_scraping).start()
    return jsonify({"message": "Scraping lancé. Vous serez informé lorsque le processus sera terminé."})

if __name__ == '__main__':
    app.run(debug=True)
