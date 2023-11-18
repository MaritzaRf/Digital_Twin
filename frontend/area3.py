import pandas as pd
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Datos de ejemplo
d = [["1", 1, 3], ["2", 2, 5], ["3", 3, 6]]
df = pd.DataFrame(d, columns=["| ID |", "T(s) |", "Ase(cm)|"])

# Crear figura con Plotly Express
fig = px.line(df, x='T(s) |', y='Ase(cm)|', title='Asentamiento por Segundo')

# Ajustar dimensiones del gráfico
fig.update_layout(height=300, width=450) 

# Configurar el primer área con el gráfico
area31 = dbc.Stack(
    children=[
        html.H4("GRÁFICA ", className="font-weight-bold"),
        # Agregar el gráfico usando dcc.Graph y la figura creada
        dcc.Graph(figure=fig),
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 mb-4 text-black",
)

# Configurar el segundo área con la tabla
area32 = dbc.Stack(
    children=[
        html.H4("TABLA DE DATOS", className="font-weight-bold"),
        html.H5(".", className="font-weight-bold text-white"),
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
)

# Definir el layout de la aplicación con las dos áreas
area3 = dbc.Container(
    [
    dbc.Row([
        dbc.Col(area31, md =6, style = {'background-color':'white'}), 
        dbc.Col(area32, md = 6, style = {'background-color':'white'})
        ])  
    ],
    fluid=True,
    style={"background-color": "white", "border": "2px solid #f1e7da"}
)
