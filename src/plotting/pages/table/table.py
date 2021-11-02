# package imports
from dash import dash_table, html
import dash_bootstrap_components as dbc
from dash import dcc

# local imports
from src.plotting.utils import color

# set constants
path = "/table"
title = "Table"
table_id = "id-table"
dropdown_id = "select_page_size"
PAGE_SIZE = 20

layout = dbc.Container(
    [
        html.H1("Table"),
        dcc.Dropdown(
            id=dropdown_id,
            options=[
                {"label": "20", "value": 20},
                {"label": "50", "value": 50},
                {"label": "100", "value": 100},
                {"label": "All", "value": -1},
            ],
            value=None,
            placeholder="Page Size",
        ),
        dash_table.DataTable(
            id=table_id,
            page_size=PAGE_SIZE,
            sort_action="native",
            filter_action="native",
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": color.light_grey}
            ],
            style_header={"backgroundColor": color.dark_grey},
            style_table={"overflowX": "auto", "overflowY": "auto"},
            style_cell={
                "maxWidth": "180px",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
            },
            editable=True,
        ),
    ]
)
