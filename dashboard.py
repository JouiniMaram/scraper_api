import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd

# Crée l'application Dash
app = dash.Dash(__name__)

# Charger les données depuis le fichier CSV
df = pd.read_csv("data/autoplus_data.csv")




# Nettoyage des prix
df['Prix'] = df['Prix'].str.replace("Prix : ", "").str.replace("DT", "").str.replace(" ", "").astype(float, errors='ignore')

# Graphiques
df_transmission = df["Transmission"].value_counts().reset_index()
df_transmission.columns = ["Type de Transmission", "Nombre"]

fig_transmission = px.bar(
    df_transmission,
    x="Type de Transmission",
    y="Nombre",
    color="Type de Transmission",
    title="Répartition des types de transmission",
    labels={"Type de Transmission": "Transmission", "Nombre": "Nombre d'annonces"}
)

# Table des données
table = dash_table.DataTable(
    id='table-annonces',
    columns=[
        {"name": "Titre", "id": "Titre"},
        {"name": "Prix", "id": "Prix"},
        {"name": "Carburant", "id": "Carburant"},
        {"name": "Transmission", "id": "Transmission"},
        {"name": "État", "id": "État"},
        {"name": "Lien", "id": "Lien", "presentation": "markdown"},
        {"name": "Image", "id": "Image", "presentation": "markdown"}
    ],
    data=df.to_dict('records'),
    style_table={'height': '400px', 'overflowY': 'auto'},
    style_cell={'textAlign': 'center', 'padding': '5px'},
    style_header={'backgroundColor': 'lightgray', 'fontWeight': 'bold'},
)

# Layout de l'application
app.layout = html.Div([
    html.H1("Tableau de Bord des Annonces Auto", style={'textAlign': 'center'}),
    
    dcc.Graph(figure=fig_transmission),
    
    html.Div([
        html.H2("Tableau des Annonces", style={'textAlign': 'center'}),
        table
    ], style={'padding': '20px'}),
    
    html.Div([
        html.P("Graphique montrant la répartition des types de transmission et un tableau des annonces avec des informations sur le prix, l'état, et plus.", 
               style={'fontSize': '18px', 'textAlign': 'center'}),
    ], style={'padding': '20px'}),
])

# Lancer le serveur
if __name__ == '__main__':
    app.run(debug=True)

