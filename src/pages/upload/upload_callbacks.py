# package imports
import base64
import io
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# local imports
from app import app
from pages.upload import upload
from layout.layout import store_id


@app.callback(
    Output(upload.info_id, 'children'),
    Output(store_id, 'data'),
    Input(upload.upload_id, 'contents'),
    State(upload.upload_id, 'filename')
)
def update_upload(contents, filename):
    """Handle uploading data

    Parameters
    ----------
        contents: str
            base64 string that contains contents of uploaded file
        filename: str
            Name of file being uploaded

    Returns
    ----------
        text: list or str
            list of components or str of output text
        data: dict
            Dictionary that contains data from uploaded file
    """

    if filename is None:
        raise PreventUpdate

    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8', 'replace'))
            )
        else:
            raise Exception
    except Exception as e:
        print(e)
        error_text = 'Error uploading, something is wrong with the file.'
        return error_text, None

    succ_text = 'File uploaded successfully: ' + filename
    return succ_text, {'df': df.to_dict('records')}
