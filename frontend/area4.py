import dash
from dash import html
import dash_bootstrap_components as dbc


# Agrega estilos personalizados para justificación de texto
custom_styles = {'textAlign': 'justify' }

area4 = dbc.Stack(
    children=[
        html.H4("INTRODUCCIÓN ", className="font-weight-bold"),
        html.H5("Explicación del trabajo y objetivos", className="font-weight-bold"),
        html.Ul('''
            En el marco del curso de Ingeniería Civil, se propone un emocionante.
            Se presenta proyecto práctico: la construcción de una máquina perforadora de túneles
            a pequeña escala utilizando materiales accesibles y herramientas básicas.
            Este proyecto no solo fomenta la comprensión práctica de los principios de la ingeniería de túneles,
            sino que también desarrolla habilidades de trabajo en equipo y creatividad entre los estudiantes,
            una guía detallada para la construcción de esta máquina, junto con una estrategia de gestión
            para implementarla de manera efectiva.
        ''', style=custom_styles),
    ],
    direction="column",
    className="align-items-center flex-wrap py-4 px-4 mb-4 ml-4 text-black",
    style={"background-color": "white", "border": "2px solid #f1e7da"},
)
