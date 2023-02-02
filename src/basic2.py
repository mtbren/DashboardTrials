import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objects as go

app = dash.Dash()

# Create data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    dcc.Graph(id="scatterPlot1",
              figure={
                  'data': [
                      go.Scatter(
                          x=random_x,
                          y=random_y,
                          mode='markers',
                          marker={
                              'size': 12,
                              'color': 'rgb(51,204,153)',
                              'symbol': 'pentagon',
                              'line': {
                                  'width': 2
                              }
                          }
                      )
                  ],
                  'layout': go.Layout(
                      title='ScatterPlot1 using Dash',
                      xaxis={
                          'title': 'Sample X Axis title'
                      }
                  )
              }),
    dcc.Graph(id="scatterPlot2",
              figure={
                  'data': [
                      go.Scatter(
                          x=random_x,
                          y=random_y,
                          mode='markers',
                          marker={
                              'size': 12,
                              'color': 'rgb(200,204,50)',
                              'symbol': 'pentagon',
                              'line': {
                                  'width': 2
                              }
                          }
                      )
                  ],
                  'layout': go.Layout(
                      title='ScatterPlot2 using Dash',
                      xaxis={
                          'title': 'Sample X Axis title'
                      }
                  )
              })
])

if __name__ == '__main__':
    app.run_server()