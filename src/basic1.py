import dash
from dash import dcc
from dash import html

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('Hello Dash!', style={'textAlign': 'center',
                                  'color': colors['text']}),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='example',
              figure={'data': [
                  {'x': [1, 2, 3], 'y': [4, 1, 2], 'name': 'SF', 'type': 'bar'},
                  {'x': [1, 2, 3], 'y': [2, 4, 5], 'name': 'NYC', 'type': 'bar'},
              ],
                  'layout': {'title': 'Bar Plot',
                             'plot_bgcolor': colors['background'],
                             'paper_bgcolor': colors['background'],
                             'font': {'color': colors['text']}}
              })
], style={'backgroundColor': colors['background']})

# If you are running the script directly, it will grab the application object and run the server
if __name__ == '__main__':
    app.run_server()
