# package imports
from dash import html
import dash_bootstrap_components as dbc

# set contansts
path = '/home'
title = 'Home'
layout = dbc.Container(
    [
        html.H1('Home')
    ]
)
