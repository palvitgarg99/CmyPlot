# package imports
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# local imports
from app import app
from pages.table import table
from layout.layout import store_id


@app.callback(
    Output(table.table_id, 'data'),
    Output(table.table_id, 'columns'),
    Input(store_id, 'data')
)
def initialize_table_data(data):
    """Handle setting table data

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        data: dict
            Data from stored dcc.Store component
    """
    if data is None:
        raise PreventUpdate

    cols = [{'name': i, 'id': i} for i in data[0]]
    return data, cols
