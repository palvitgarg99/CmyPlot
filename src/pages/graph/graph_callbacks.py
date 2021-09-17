# package imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context
import pandas as pd
import plotly.express as px

# local imports
from app import app
from layout.layout import store_id
from utils.functions import fetch_columns_options
from components import graph_options
from pages.graph import graph


@app.callback(
    Output(graph_options.collapse, 'is_open'),
    Input(graph_options.toggler, 'n_clicks'),
    State(graph_options.collapse, 'is_open')
)
def handle_accordian_collapse(go_clicks, go_open):
    """Handle toggling the various accordian collapses

    Parameters
    ----------
        temp_clicks: int
            How many times the temp link has been clicked
        temp_open: bool
            Whether the temp card is currenlty open or not

    Returns
    ----------
        temp_open: bool
            The reverse of what temp_open passed in
    """

    # Extract button id from triggered context
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Open specific accordian item
    if button_id == graph_options.toggler and go_clicks:
        return not go_open
    else:
        raise PreventUpdate


@app.callback(
    Output(graph_options.x_att, 'options'),
    Output(graph_options.y_att, 'options'),
    Output(graph_options.color, 'options'),
    Output(graph_options.size, 'options'),
    Input(store_id, 'data')
)
def fetch_columns_from_data(data):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        options: list of dict
            Options for each of the dropdowns in the form of
            {'label': 'Example', 'value': 'example'}
    """

    if data is None:
        raise PreventUpdate

    options = fetch_columns_options(data['df'])

    return options, options, options, options


@app.callback(
    Output(graph.graph_id, 'figure'),
    Input(store_id, 'data'),
    Input(graph_options.x_att, 'value'),
    Input(graph_options.y_att, 'value'),
    Input(graph_options.color, 'value'),
    Input(graph_options.size, 'value')
)
def create_figure(data, x_att, y_att, color, size):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        options: list of dict
            Options for each of the dropdowns in the form of
            {'label': 'Example', 'value': 'example'}
    """

    if data is None or all(i is None for i in [x_att, y_att, size, color]):
        raise PreventUpdate

    df = pd.DataFrame(data['df'])

    x = x_att if x_att else None
    y = y_att if y_att else None
    size = size if size else None
    color = color if color else None

    print('Rendering: ', [x, y, size, color])
    figure = px.scatter(
        df,
        x=x,
        y=y,
        size=size,
        color=color
    )

    return figure
