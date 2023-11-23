from dash import Dash, html, dcc, Input, Output
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc



from frontend.area1 import area1
from frontend.area2 import *
from frontend.area3 import *
from frontend.area4 import area4
from frontend.area5 import area5




# Crea la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# Define el layout de la aplicación
app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(area1, md=12, style={'background-color': 'white'}),
            dbc.Col(area2, md=6, style={'background-color': 'white'}), 
            dbc.Col(area3, md=6, style={'background-color': 'white'}), 
            dbc.Col(area4, md=6, style={'background-color': 'white'}),
            dbc.Col(area5, md=6, style={'background-color': 'white'})
        ])
    ],
    fluid=True
)

@app.callback(
    [Output('asentamiento', 'figure'),
     Output('distancia-actual', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def consultar(n):
    # Utilizar la variable global data_dist
    global data_dist, result, db
    result = db.find_one(sort=[('updated_at', -1)])
    distancia = int(result['distancia'])
    data_dist.append(distancia)

    # Crear el objeto de figura de Plotly
    fig = go.Figure(data=[go.Scatter(y=data_dist, mode='lines+markers')])

    # Agregar una línea horizontal en y=5
    fig.add_shape(
        type="line",
        x0=0,
        x1=len(data_dist),
        y0=10,
        y1=10,
        line=dict(color="red", width=2),
    )

    # Formatear la distancia para mostrarla en el H1
    distancia_texto = f"El asentamiento fue: {distancia} cm"

    return fig, distancia_texto

if __name__ == '__main__':
    app.run_server(debug=True)

