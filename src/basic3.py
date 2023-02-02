import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('../data/OldFaithful.csv')

app.layout = html.Div([
    dcc.Graph(id="ScatterPlot",
              figure={
                  'data': [go.Scatter(x=df['X'], y=df['Y'], mode='markers')],
                  'layout': go.Layout(title='Old Faithful Eruptions',
                                      xaxis={'title':'Time to Eruptions'},
                                      yaxis={'title':'Length of Eruptions'})
              }
    )
])

if __name__ == "__main__":
    app.run_server()
