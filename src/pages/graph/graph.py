# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from components import graph_options
from utils.constants import graph_config

# set constants
path = '/graph'
title = 'Graph'
graph_id = 'id-graph'

layout = dbc.Container(
    [
        html.H1('Graph'),
        dbc.Row(
            [
                dbc.Col(
                    # The next update of dash_bootstrap_components includes
                    # an accordian component. The collapse items should be
                    # changed to an accordian.
                    [
                        graph_options.card,
                    ],
                    className='col-lg-4'
                ),
                dbc.Col(
                    dcc.Graph(
                        id=graph_id,
                        config=graph_config,
                        animate=True,
                        responsive=True
                    ),
                    className='col-lg-8'
                )
            ]
        )
    ]
)
