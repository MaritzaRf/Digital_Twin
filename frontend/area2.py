import dash
from dash import html
import dash_bootstrap_components as dbc

area21 = dbc.Stack(
    children=[
        html.H4("DISEÑO ", className="font-weight-bold"),
        html.H5("", className= "font-weight-bold"),         
        html.Div(
            html.Div(
                children=[
                    html.Img(
                        src='https://mediacdn.acciona.com/media/3dahx0j1/mularroya-tbm.jpg',
                        style={'width': '100%'},  # Tamaño de la imagen
                        className=''
                    ), 
                ],
                className="d-flex flex-center gap-2 mb-4"
            )
        ) 
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-black"    
)


area22 = dbc.Stack(
    children=[
        html.H4("MATERIALES ", className="font-weight-bold"),
        html.H5("", className= "font-weight-bold"),
        html.Ul([
            html.Li("Cartón corrugado resistente."),
            html.Li("Palitos de paleta o madera para las cuchillas"),
            html.Li("Tapas para las ruedas."),
            html.Li("Motores para el mecanismo de desplazamiento."),
            html.Li("Banda de cartón u otro material para las ruedas tipo excavadora."),
            html.Li("Circuitos eléctricos para hacer girar las cuchillas."),
            html.Li("Silicona en barra."),
            html.Li("Pegamento.")
        ]),
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-black",   
)

# Define el layout de la aplicación
area2 = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area21, md =7, style = {'background-color':'white'}), 
        dbc.Col(area22, md = 5, style = {'background-color':'white'})
        ])  
    ],
    fluid=True,
    style={"background-color": "white", "border": "2px solid #f1e7da"}
)


