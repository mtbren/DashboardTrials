import dash
from dash import html

app = dash.Dash()

app.layout = html.Div(['This is the outermost Div!!!',
                       html.Div('This is an inner Div!!!',
                                style={'color': 'red',
                                       'border': '2px red solid'}),
                       html.Div(['This is another Div!!!'],
                                style={'color': 'blue', 'border': '3px blue solid'})],
                      style={'color': 'green',
                             'border': '2px green solid'})

if __name__ == "__main__":
    app.run_server()
