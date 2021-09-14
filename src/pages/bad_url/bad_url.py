# package imports
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        html.H1('404 Error'),
        html.P(
            [
                'Page not found, return to ',
                html.A('Home', href='/')
            ]
        )
    ]
)
