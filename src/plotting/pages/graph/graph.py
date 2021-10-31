# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from src.plotting.pages.graph.components import graph_options
from src.plotting.utils.constants import graph_config
from src.plotting.pages.table import table

# set constants
path = "/graph"
title = "Graph"
graph_id = "id-graph"
buttons_id = "id-share-button"

layout = dbc.Container(
    [
        html.H1("Graph"),
        dbc.Row(
            [
                dbc.Col(
                    # The next update of dash_bootstrap_components includes
                    # an accordian component. The collapse items should be
                    # changed to an accordian.
                    [
                        graph_options.card,
                    ],
                    className="col-lg-3",
                ),
                dbc.Col(
                    dcc.Graph(id=graph_id, config=graph_config), className="col-lg-9"
                ),
                dbc.Col(
                    dbc.Button(
                        html.Big("Share"),
                        color="success",
                        # disabled=True,
                        className="mr-2",
                        id=buttons_id,
                        n_clicks=0
                        # href=table.path
                    )
                ),
                dbc.Col(
                    html.Div(
                        id="container-button-basic",
                        children="Enter a value and press submit",
                    )
                ),
            ]
        ),
    ]
)
