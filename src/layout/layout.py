# package imports
from dash import html, dcc

# local imports
from layout.navbar import navbar

# constants
layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content')
        # TODO: add footer
    ]
)
