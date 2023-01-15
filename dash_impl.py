from dash import Dash, html, dcc, Input, Output, State
import dash_cytoscape as cyto

app = Dash(__name__)

# TODO: refactor
HOURS_AVAILABLE = [
    1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24
]

# app.layout = html.Div([
#     html.P("Dash Cytoscape:"),
#     cyto.Cytoscape(
#         id='cytoscape',
#         elements=[
#             {'data': {'id': 'ca', 'label': 'Canada'}}, 
#             {'data': {'id': 'on', 'label': 'Ontario'}}, 
#             {'data': {'id': 'qc', 'label': 'Quebec'}},
#             {'data': {'source': 'ca', 'target': 'on'}}, 
#             {'data': {'source': 'ca', 'target': 'qc'}}
#         ],
#         layout={'name': 'breadthfirst'},
#         style={'width': '400px', 'height': '500px'}
#     )
# ])

app.layout = html.Div([
    html.P("Network visuaization sample"),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='demo-dropdown'),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='demo-dropdown'),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic', children='Enter a value and press submit'),
    # html.Button('Select', id='submit-val', n_clicks=0),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': '1.0', 'value': 1.0, 'name': '1.0'}}, 
            {'data': {'id': '2.0', 'value': 2.0, 'name': '2.0'}},
            {'data': {'id': '3.0', 'value': 3.0, 'name': '3.0'}}, 
            {'data': {'id': '4.0', 'value': 4.0, 'name': '4.0'}}, 
            {'data': {'id': '5.0', 'value': 5.0, 'name': '5.0'}}, 
            {'data': {'id': '6.0', 'value': 6.0, 'name': '6.0'}}, 
            {'data': {'id': '7.0', 'value': 7.0, 'name': '7.0'}}, 
            {'data': {'id': '8.0', 'value': 8.0, 'name': '8.0'}}, 
            {'data': {'id': '9.0', 'value': 9.0, 'name': '9.0'}}, 
            {'data': {'id': '10.0', 'value': 10.0, 'name': '10.0'}}, 
            {'data': {'id': '11.0', 'value': 11.0, 'name': '11.0'}}, 
            {'data': {'id': '12.0', 'value': 12.0, 'name': '12.0'}}, 
            {'data': {'id': '13.0', 'value': 13.0, 'name': '13.0'}}, 
            {'data': {'id': '14.0', 'value': 14.0, 'name': '14.0'}}, 
            {'data': {'id': '15.0', 'value': 15.0, 'name': '15.0'}},
            {'data': {'id': '16.0', 'value': 16.0, 'name': '16.0'}}, 
            {'data': {'id': '17.0', 'value': 17.0, 'name': '17.0'}}, 
            {'data': {'id': '18.0', 'value': 18.0, 'name': '18.0'}}, 
            {'data': {'id': '19.0', 'value': 19.0, 'name': '19.0'}}, 
            {'data': {'id': '20.0', 'value': 20.0, 'name': '20.0'}}, 
            {'data': {'id': '21.0', 'value': 21.0, 'name': '21.0'}}, 
            {'data': {'id': '22.0', 'value': 22.0, 'name': '22.0'}}, 
            {'data': {'id': '23.0', 'value': 23.0, 'name': '23.0'}}, 
            {'data': {'id': '24.0', 'value': 24.0, 'name': '24.0'}}, 
            {'data': {'id': '25.0', 'value': 25.0, 'name': '25.0'}}, 
            {'data': {'id': '26.0', 'value': 26.0, 'name': '26.0'}}, 
            {'data': {'id': '27.0', 'value': 27.0, 'name': '27.0'}}, 
            {'data': {'id': '28.0', 'value': 28.0, 'name': '28.0'}},
            {'data': {'id': '29.0', 'value': 29.0, 'name': '29.0'}}, 
            {'data': {'id': '30.0', 'value': 30.0, 'name': '30.0'}}, 
            {'data': {'id': '31.0', 'value': 31.0, 'name': '31.0'}}, 
            {'data': {'id': '32.0', 'value': 32.0, 'name': '32.0'}},
            {'data': {'id': '33.0', 'value': 33.0, 'name': '33.0'}}, 
            {'data': {'id': '34.0', 'value': 34.0, 'name': '34.0'}}, 
            {'data': {'id': '35.0', 'value': 35.0, 'name': '35.0'}}, 
            {'data': {'id': '36.0', 'value': 36.0, 'name': '36.0'}},
            {'data': {'id': '37.0', 'value': 37.0, 'name': '37.0'}}, 
            {'data': {'id': '38.0', 'value': 38.0, 'name': '38.0'}}, 
            {'data': {'id': '39.0', 'value': 39.0, 'name': '39.0'}},
            ## Edges
            {'data': {'color': 'black', 'weight': 4.0, 'source': '1.0', 'target': '2.0'}},
            {'data': {'color': 'black', 'weight': 4.0, 'source': '1.0', 'target': '39.0'}},
             {'data': {'color': 'green', 'weight': 4.0, 'source': '3.0', 'target': '2.0'}},
             {'data': {'color': 'green', 'weight': 2.0, 'source': '4.0', 'target': '3.0'}},
             {'data': {'color': 'black', 'weight': 1.0, 'source': '4.0', 'target': '14.0'}},
             {'data': {'color': 'green', 'weight': 6.0, 'source': '5.0', 'target': '4.0'}},
             {'data': {'color': 'black', 'weight': 4.0, 'source': '5.0', 'target': '8.0'}},
             {'data': {'color': 'green', 'weight': 2.0, 'source': '6.0', 'target': '5.0'}},
            {'data': {'color': 'black', 'weight': 3.0, 'source': '6.0', 'target': '7.0'}},
            {'data': {'color': 'green', 'source': '6.0', 'target': '31.0'}},
            {'data': {'color': 'black', 'weight': 3.0, 'source': '7.0', 'target': '8.0'}},
            {'data': {'color': 'green', 'weight': 4.0, 'source': '9.0', 'target': '8.0'}},
            {'data': {'color': 'black', 'weight': 2.0, 'source': '10.0', 'target': '11.0'}},
            {'data': {'color': 'green', 'source': '11.0', 'target': '6.0'}},
            {'data': {'color': 'green', 'weight': '2.0', 'source': '11.0', 'target': '12.0'}},
            {'data': {'color': 'black', 'weight': 2.0, 'source': '12.0', 'target': '13.0'}},
            {'data': {'color': 'green', 'weight': 2.0, 'source': '13.0', 'target': '10.0'}},
            {'data': {'color': 'green', 'weight': 4.0, 'source': '14.0', 'target': '13.0'}},
            {'data': {'color': 'green', 'weight': 3.0, 'source': '15.0', 'target': '14.0'}},
            {'data': {'color': 'black', 'weight': 7.0, 'source': '15.0', 'target': '16.0'}},
            {'data': {'color': 'black', 'weight': 7.0, 'source': '16.0', 'target': '17.0'}},
            {'data': {'color': 'black', 'weight': 7.0, 'source': '17.0', 'target': '18.0'}},
            {'data': {'color': 'green', 'weight': 9.0, 'source': '18.0', 'target': '3.0'}},
            {'data': {'color': 'green', 'weight': 1.0, 'source': '19.0', 'target': '16.0'}},
            {'data': {'color': 'green', 'weight': 1.0, 'source': '20.0', 'target': '19.0'}},
            {'data': {'color': 'green', 'weight': 4.0, 'source': '21.0', 'target': '16.0'}},
            {'data': {'color': 'green', 'weight': 1.0, 'source': '22.0', 'target': '21.0'}},
            {'data': {'color': 'green', 'weight': 1.0, 'source': '23.0', 'target': '22.0'}},
            {'data': {'color': 'green', 'weight': 1.0, 'source': '24.0', 'target': '16.0'}}, 
            {'data': {'color': 'green', 'weight': 1.0, 'source': '24.0', 'target': '23.0'}}, 
            {'data': {'color': 'green', 'source': '25.0', 'target': '2.0'}}, 
            {'data': {'color': 'green', 'source': '26.0', 'target': '25.0'}},
            {'data': {'color': 'green', 'source': '27.0', 'target': '17.0'}}, 
            {'data': {'color': 'green', 'source': '27.0', 'target': '26.0'}}, 
            {'data': {'color': 'green', 'source': '28.0', 'target': '26.0'}}, 
           
            {'data': {'color': 'green', 'source': '29.0', 'target': '26.0'}},
            {'data': {'color': 'green', 'source': '29.0', 'target': '28.0'}},
            {'data': {'color': 'green', 'source': '30.0', 'target': '2.0'}}, 
            {'data': {'color': 'green', 'source': '32.0', 'target': '10.0'}},
            {'data': {'color': 'green', 'source': '33.0', 'target': '19.0'}},
            {'data': {'color': 'green', 'source': '34.0', 'target': '20.0'}},
            {'data': {'color': 'green', 'source': '35.0', 'target': '22.0'}},
            {'data': {'color': 'green', 'source': '36.0', 'target': '23.0'}},
            {'data': {'color': 'green', 'source': '37.0', 'target': '25.0'}},
            {'data': {'color': 'green', 'source': '38.0', 'target': '29.0'}},
            {'data': {'color': 'green', 'weight': '4.0', 'source': '39.0', 'target': '9.0'}}
        ],
        stylesheet=[
              {
                'selector': 'node',
                'style': {
                    'label': 'data(id)'
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'label': 'data(weight)',
                    'line-color': 'data(color)',
                    'target-arrow-color': 'data(color)',
                    'target-arrow-shape': 'triangle',
                    'targetArrowShape': 'triangle',
                    'curveStyle': 'bezier'
                }
            },
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '1080px', 'height': '1700px'}
    )
])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    for _ in range(5):
        print("elo elo")
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

if __name__ == '__main__':
    app.run_server(debug=True)