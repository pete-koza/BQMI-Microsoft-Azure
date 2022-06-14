import dash
import app
from dash import dcc, html
from dash.dependencies import ALL, Input, Output, State

def generate_travel_tables():
    return html.Div(
        id="front-page-tables",
        className="front-page-tables",
        children=[
            html.P("Selector")
        ]
    )
