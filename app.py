import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from frontend.area1 import area1
from frontend.area2 import area2
from frontend.area3 import area3
from frontend.area4 import area4
from frontend.area5 import area5



# Crea la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Define el layout de la aplicación
app.layout = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area1, md = 12, style = {'background-color':'white'}), # md es el ancho de la casilla 
        dbc.Col(area2, md = 6, style = {'background-color':'white'}),
        dbc.Col(area3, md = 6, style = {'background-color':'white'}),
        dbc.Col(area4, md = 6, style = {'background-color':'white'}),
        dbc.Col(area5, md = 6, style = {'background-color':'white'})
        ])  
    ],
    fluid=True
)


if __name__ == '__main__':
    app.run_server(debug=True)
