import dash
from dash import html
from dash import dcc

app = dash.Dash()

print(help(dcc.Dropdown))

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label':'New York City', 'value':'NYC'},
                          {'label':'San Francisco', 'value':'SF'}],
                 value='NYC'),

    html.Label('Slider'),
    dcc.Slider(min=0, max=10, value=3, step=0.5, marks={i: i for i in range (0,11)}),

    html.P(html.Label('Radio Buttons')),
    dcc.RadioItems(options=[{'label':'New York City', 'value':'NYC'},
                            {'label':'SanFrancisco', 'value':'SFO'}],
                   value='SFO')
])

if __name__=="__main__":
    app.run_server();