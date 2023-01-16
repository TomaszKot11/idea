from dash import Dash, html, dcc, Input, Output, State
import dash_cytoscape as cyto
from main import prepare_graph

app = Dash(__name__)

data_prepared = prepare_graph()

# TODO: refactor
HOURS_AVAILABLE = [
    1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24
]

app.layout = html.Div([
    html.P("Network visuaization sample"),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='demo-dropdown'),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='demo-dropdown-two'),
    html.Button('Submit', id='submit-val', n_clicks=0),
    # html.Button('Select', id='submit-val', n_clicks=0),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            # nodes
            *data_prepared['elements']['nodes'],
            # edges
            *data_prepared['elements']['edges']
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