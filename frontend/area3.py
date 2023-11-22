import pandas as pd
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px

#Base de datos
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://cagomezj:1234@cluster0.lg8bsx8.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.sensores.sensor_1
result = 0

# Declarar data_dist fuera de la función para evitar el UnboundLocalError
data_dist = []

# Configurar el primer área con el gráfico
area31 = dbc.Stack(
    children=[
        html.H4("ASENTAMIENTO TUNELADORA", style={'text-align': 'center'}),
        html.Hr(),
        html.H5(id='distancia-actual', style={'text-align': 'center'}),
        dcc.Graph(id='asentamiento', style={'height': '309px'}),  # Ajusta la altura del gráfico según tus necesidades
        dcc.Interval(
            id='interval-component',
            interval=1 * 500,  # en milisegundos, actualiza cada 1 segundo
            n_intervals=0
        ),
        html.Div(id='alerta-texto', style={'text-align': 'center', 'margin-top': '10px'})
    ],
)


# Definir el layout de la aplicación con las dos áreas
area3 = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area31, md = 12, style = {'background-color':'white'})
        ])  
    ],
    fluid=True,
    style={"background-color": "white", "border": "2px solid #f1e7da"}
)
