# package imports
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# local imports
from src.plotting.app import app
from src.plotting.utils.functions import fetch_columns_options
from src.plotting.pages.table import table
from src.plotting.layout.layout import store_id


@app.callback(
    Output(table.table_id, "data"),
    Output(table.table_id, "columns"),
    Input(store_id, "data"),
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

    cols = fetch_columns_options(data["df"], table=True)
    return data["df"], cols


@app.callback(
    Output(table.table_id, "page_size"),
    Input(table.dropdown_id, "value"),
    Input(table.table_id, "data"),
)
def update_graph(page_size, data):
    if page_size is None:
        page_size = table.PAGE_SIZE

    if (data is not None) and (page_size == -1):
        page_size = len(data)

    return page_size
