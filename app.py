from dash import Dash, html

app = Dash()

app.layout = html.Div(
    children=[
    html.H1(children='Fahrparcours_Gruppe4',
    style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40})])













if __name__ == '__main__':
    app.run_server(host = '192.168.178.66', port=8080, debug=False)