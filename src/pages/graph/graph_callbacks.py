# package imports
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context

# local imports
from app import app
from components import graph_options


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
