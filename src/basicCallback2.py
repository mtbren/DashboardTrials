import dash
from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("./data/gapminderDataFiveYear.csv")

app = dash.Dash()

year_options = []
for year in df['year'].unique():
    year_options.append({'label': str(year), 'value': year})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',
                 options=year_options,
                 value=df['year'].min())
])


@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
    # Data only for selected year from Dropdown
    filtered_df = df[df['year'] == selected_year]
    traces = []

    for continent_name in df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size':15},
            name=continent_name,
            text=df_by_continent['country']
        ))

    figure = {'data': traces,
              'layout': go.Layout(
                title='GDP vs Life Expectancy',
                xaxis={'title':'GDP Per Capita', 'type':'log'},
                yaxis={'title':'Life Expectancy'})}
    return figure


if __name__ == "__main__":
    app.run_server()
