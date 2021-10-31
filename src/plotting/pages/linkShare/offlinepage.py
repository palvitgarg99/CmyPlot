# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from src.plotting.pages.graph.components import graph_options
from src.plotting.pages.linkShare.figure_generator import make_graph
from src.plotting.utils.constants import graph_config

# set constants
path = "/share"
title = "Shared Graph"
graph_id = "id-graph-share"
buttons_id = "id-share-button"


def offlinepagelayout():
    layout = dbc.Container(
        [
            html.H1("Shared Graph"),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(id=graph_id, config=graph_config, figure=make_graph())
                    )
                ]
            ),
        ]
    )
    return layout
