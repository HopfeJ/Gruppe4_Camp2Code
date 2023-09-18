from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from flask import Flask, Response

import plotly.express as px
from basisklassen_cam import Camera
import cv2
import numpy as np

external_stylesheets = [dbc.themes.BOOTSTRAP]

server = Flask(__name__)

app = Dash(__name__, external_stylesheets=external_stylesheets, server=server)


def generate_camera_image(camera_class):
    while True:
        frame = camera_class.get_frame()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 100, 200)
        stacked = np.hstack([gray, canny])
        _, x = cv2.imencode(".jpeg", stacked)
        x_bytes = x.tobytes()

        x_string = (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + x_bytes + b'\r\n\r\n')
        
        yield x_string
        


@server.route("/video_feed")
def video_feed():
   return Response(generate_camera_image(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')



# Layout: Reine Optik

app.layout = html.Div(children=[
    dbc.Row([html.H1("Überschrift", style={"textAlign": "center"})]), 
    dbc.Row([
        dbc.Col([dcc.Graph(id="graph1", figure={})], width=6),
        dbc.Col([
            dbc.Row(dcc.Slider(min=0, max=5, value=2, id="slider1")),
            html.Br(), 
            html.Br(), 
            dbc.Row(dcc.Slider(min=0, max=1, value=0.5, id="slider2"))
        ],
        align="center")
    ]),
    dbc.Row([
        html.Div([
            html.Img(src="/video_feed")
        ])
    ])
])


# Callbacks: Funktionalität

@app.callback(
    Output(component_id="graph1", component_property="figure"),
    [Input(component_id="slider1", component_property="value"),
     Input(component_id="slider2", component_property="value")]
)
def update_graph1(input1, input2):
    list_x = list(range(100))
    list_y = [x**input1**input2 for x in list_x]
    fig = px.scatter(x=list_x, y=list_y)
    return fig


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True, port=8050)