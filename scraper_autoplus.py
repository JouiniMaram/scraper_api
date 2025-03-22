import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuration de Selenium
chrome_options = Options()
# Désactiver le mode headless pour observer le navigateur
chrome_options.add_argument("--start-maximized")  # Ouvre le navigateur en mode plein écran
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

# Initialisation du WebDriver
driver = uc.Chrome(options=chrome_options)

BASE_URL = "https://www.auto-plus.tn"
LISTING_URL = f"{BASE_URL}/voitures-d-occasion.html"  # Modification de l'URL

def get_autoplus_data():
    driver.get(LISTING_URL)
    
    # Attendre quelques secondes pour voir la page se charger
    time.sleep(5)
    
    # Afficher les 1000 premiers caractères de la page source pour vérifier
    print(driver.page_source[:1000])  # Cela nous montre si la page charge correctement
    
    wait = WebDriverWait(driver, 20)  # Attente prolongée pour le chargement

    annonces = []

    try:
        # Attendre que les annonces apparaissent
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-data")))
    except:
        print("❌ Les annonces ne se chargent pas correctement.")
        return []

    # Récupérer toutes les annonces
    annonce_elements = driver.find_elements(By.CLASS_NAME, "search-results-data")
    print(f"✅ {len(annonce_elements)} annonces trouvées !")

    for annonce in annonce_elements:
        try:
            titre = annonce.find_element(By.CLASS_NAME, "hide-mobile").text.strip()
        except:
            titre = "Non spécifié"

        try:
            prix = annonce.find_element(By.CLASS_NAME, "crTypePrice").text.strip()
        except:
            prix = "Non spécifié"

        try:
            lien_annonce = annonce.find_element(By.XPATH, ".//preceding::a[1]").get_attribute("href")
        except:
            lien_annonce = "Non spécifié"

        try:
            image_url = annonce.find_element(By.XPATH, ".//preceding::a[1]/img").get_attribute("src")
        except:
            image_url = "Non disponible"

        try:
            carburant = annonce.find_element(By.CLASS_NAME, "opt1").text.strip()
        except:
            carburant = "Non spécifié"

        try:
            transmission = annonce.find_element(By.CLASS_NAME, "opt2").text.strip()
        except:
            transmission = "Non spécifié"

        try:
            etat = annonce.find_element(By.CLASS_NAME, "opt6").text.strip()
        except:
            etat = "Non spécifié"

        annonces.append({
            "Titre": titre,
            "Prix": prix,
            "Lien": lien_annonce,
            "Image": image_url,
            "Carburant": carburant,
            "Transmission": transmission,
            "État": etat
        })

    return annonces

if __name__ == "__main__":
    try:
        data = get_autoplus_data()
        if data:
            df = pd.DataFrame(data)
            df.to_csv("data/autoplus_data.csv", index=False, encoding="utf-8")
            print("✅ Données AutoPlus.tn enregistrées avec succès !")
        else:
            print("❌ Aucune annonce trouvée.")
    finally:
        driver.quit()  # Force la fermeture du driver
