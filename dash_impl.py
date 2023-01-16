from dash import Dash, html, dcc, Input, Output, State, dash_table
import dash_cytoscape as cyto
from main import prepare_graph
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
from main import PURPLE, YELLOW, GRAY

app = Dash(__name__)

initial_data_prepared = prepare_graph()

# print(initial_data_prepared)
# for _ in range(25):
#     print("0------")

# LEGEND_ELEMENTS = [
#         Line2D([0], [0], marker='_', linewidth='2.0', color='g', label='Flow direction change',markerfacecolor='g', markersize=15), 
#         Line2D([0], [0], marker='o', color='w', label='Node is now a generator',markerfacecolor=PURPLE, markersize=15), 
#         Line2D([0], [0], marker='o', color='w', label='Node now is slave',markerfacecolor=YELLOW, markersize=15), 
# ]

HOURS_AVAILABLE = [
    1,2,3,4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ,24
]

app.layout = html.Div([
    html.P("Network visuaization sample"),
    dcc.Dropdown(HOURS_AVAILABLE, '1', id='hour-one-dropdown'),
    dcc.Dropdown(HOURS_AVAILABLE, '2', id='hour-two-dropdown'),
    html.Button('Submit', id='submit-val', n_clicks=0),
    # TODO: more colors
    dash_table.DataTable([{"Kolor": "Zielony", "Wytłumaczenie": "Zmiana kierunku przepływu"},
                          {"Kolor": "Filetowy", "Wytłumaczenie": "Zmiana stanu węzła na generator"}, 
                          {"Kolor": "Żółty", "Wytłumaczenie": "Zmiana stanu węzła na pobór"}, 
                          {
                            "Kolor": "Waga na krawędzi", "Wytłumaczenie": "Różnica całkowita w przepływie"
                          }
                          ],
                           [{"name": i, "id": i} for i in ["Kolor", "Wytłumaczenie"]]),
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
                    # TODO: maybe shapes would be better
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
                    'curveStyle': 'bezier'
                }
            },
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '1080px', 'height': '1700px'}
    )
])

@app.callback(
    Output('cytoscape', 'elements'),
    Input('submit-val', 'n_clicks'),
    [State('hour-one-dropdown', 'value'), State('hour-two-dropdown', 'value')]
)
def update_output(n_clicks, value, value_two):
    first_hour = "hour_" + str(value)
    second_hour = "hour_" + str(value_two)
    new_data = prepare_graph(first_hour, second_hour)
    return [
        # nodes
        *new_data['elements']['nodes'],
        # edges
        *new_data['elements']['edges']
    ]

if __name__ == '__main__':
    app.run_server(debug=True)