# package imports
from dash import dash_table, html
import dash_bootstrap_components as dbc

# set constants
path = '/table'
title = 'Table'
table_id = 'id-table'

layout = dbc.Container(
    [
        html.H1('Table'),
        dash_table.DataTable(
            id=table_id
            # TODO: style table in css (make sure it doesn't go beyond 100% width)
        )
    ]
)
