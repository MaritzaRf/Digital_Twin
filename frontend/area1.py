import dash
from dash import html
import dash_bootstrap_components as dbc


area1 = dbc.Stack(
    children=[
        html.H1("ASENTAMIENTOS ", className="font-weight-bold"),
        html.H4("CON DIGITAL TWIN", className= "font-weight-bold")
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-white",
    style={"background-color": "#95a5a6"}
    
)
