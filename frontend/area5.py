import pandas as pd
import dash
from dash import html
import dash_bootstrap_components as dbc

d = [["1", 1, 3], ["2", 5, 7], ["3", 8, 10]]
df = pd.DataFrame(d, columns=["| Alerta |", "Tiempo (s) |", "Asentamiento (cm)|"])

area5 = dbc.Stack(
    children=[
        html.H4("REGISTRO DE ALERTAS E INYECCION DE LECHADA", className="font-weight-bold"),
        html.H5("ALERTAS", className="font-weight-bold"),
        # Agregar una tabla para mostrar el DataFrame
        html.Table(
            # Encabezados de la tabla
            [html.Tr([html.Th(col) for col in df.columns])] +
            # Contenido de la tabla
            [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))]
        ),
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-black",
    style={"background-color": "white", "border": "2px solid #f1e7da"}
)
