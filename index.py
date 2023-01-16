from dash import Dash, html, dcc, Input, Output, State, dash_table, callback_context
import dash_cytoscape as cyto
import dash_daq as daq
from utils import prepare_graph, cluster_graph
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from constants import PURPLE, YELLOW, GRAY, SELECT_HOURS_AVAILABLE
import numpy as np

app = Dash(__name__)

initial_data_prepared = prepare_graph()

# LEGEND_ELEMENTS = [
#         Line2D([0], [0], marker='_', linewidth='2.0', color='g', label='Flow direction change',markerfacecolor='g', markersize=15), 
#         Line2D([0], [0], marker='o', color='w', label='Node is now a generator',markerfacecolor=PURPLE, markersize=15), 
#         Line2D([0], [0], marker='o', color='w', label='Node now is slave',markerfacecolor=YELLOW, markersize=15), 
# ]

app.layout = html.Div([
    html.P("Network visuaization sample"),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='hour-one-dropdown'), # TODO: add some label
    dcc.Dropdown(HOURS_AVAILABLE, '2', id='hour-two-dropdown'), # TODO: add some label
    html.Button('Show difference', id='submit-val', n_clicks=0),
    html.Br(),
    daq.NumericInput(id='no-clusters', value=2),
    html.Br(),
    html.Button('Show clusters', id='submit-cluster-val', n_clicks=0),
    # TODO: more colors and better legend + hide when cluster
    dash_table.DataTable([{"Symbol/Kolor": "Zielony", "Wytłumaczenie": "Zmiana kierunku przepływu [DIFF]"},
                          {"Symbol/Kolor": "Filetowy", "Wytłumaczenie": "Zmiana stanu węzła na generator [DIFF]"}, 
                          {"Symbol/Kolor": "Żółty", "Wytłumaczenie": "Zmiana stanu węzła na pobór [DIFF]"}, 
                          {
                            "Symbol/Kolor": "Waga na krawędzi", "Wytłumaczenie": "Różnica całkowita w przepływie/Przepływm [MW]"
                          }
                          ],
                           [{"name": i, "id": i} for i in ["Symbol/Kolor", "Wytłumaczenie"]]),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            # nodes
            *initial_data_prepared['elements']['nodes'],
            # edges
            *initial_data_prepared['elements']['edges']
        ],
        stylesheet=[
              {
                'selector': 'node',
                'style': {
                    # TODO: maybe shapes would be better than colors
                    'content': 'data(id)',
                    'background-color': 'data(color)',
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
                    'curveStyle': 'bezier',
                    'font-size': 10
                    # TODO: make label more visible
                }
            },
        ],
        layout={'name': 'cose' }, #TODO: chose layout?
        style={'width': '1080px', 'height': '1500px'}
    )
])

@app.callback(
    Output('cytoscape', 'elements'),
    [Input('submit-val', 'n_clicks'), Input('submit-cluster-val', 'n_clicks')],
    [
        State('hour-one-dropdown', 'value'),
        State('hour-two-dropdown', 'value'),
        State('no-clusters', 'value')
    ]
)
def produce_cyto_data(n_clicks, n_clicks_two, value, value_two, no_clusters):
    first_hour = "hour_" + str(value)
    second_hour = "hour_" + str(value_two)
    trigger_id = callback_context.triggered[0]["prop_id"].split(".")[0]

    new_data = prepare_graph(first_hour, second_hour) if trigger_id == 'submit-val' else cluster_graph(int(no_clusters), second_hour)
    return [
        # nodes
        *new_data['elements']['nodes'],
        # edges
        *new_data['elements']['edges']
    ]

if __name__ == '__main__':
    app.run_server(debug=True)