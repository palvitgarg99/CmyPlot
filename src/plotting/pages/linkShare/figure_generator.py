import pickle
import pandas as pd
import plotly.express as px
from dash import exceptions

xaxis = ""
yaxis = ""
filename = ""


def make_graph():
    global yaxis, xaxis
    if filename != "":
        try:
            a_file = open(filename, "rb")
            output = pickle.load(a_file)
            # prep data

            if output == None:
                return px.scatter()
            df = pd.DataFrame(output["df"])
            if yaxis == "":
                yaxis = None
            if xaxis == "":
                xaxis = None

            figure = px.scatter(
                df,
                x=xaxis,
                y=yaxis,
            )

            a_file.close()
            return figure
        except Exception as e:
            return px.scatter()
    else:
        return px.scatter()
