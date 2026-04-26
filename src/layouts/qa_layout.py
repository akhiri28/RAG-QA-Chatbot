import dash
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
import dash_bootstrap_components as dbc
# from src.process.realtime_process import get_answer


# Layout
def create_search_input():
    return html.Div(
        className="icon-container mx-auto",
        style={"maxWidth": "1000px", 'color' : '#a25c3d'},
        children=[

            dcc.Input(
                id="search-input",
                placeholder="Enter any question",
                debounce=True,
                style={"position":"relative"}
            )

        ],
    )


layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.Div(
        className="icon-container mx-auto",
        style={"maxWidth": "1000px", 'color' : '#a25c3d'},
        children=[

            dcc.Input(
                id="search-input",
                placeholder="Enter any question",
                debounce=True,
                style={"position":"relative"}
            )

        ],
    ),

                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                html.Div(
                                    id="answer_area",
                                    # className="answer-area",
                                    className = "p-4 border rounded bg-light shadow-sm"
                                ),
                                type="circle",
                                color='#d02b27',
                            ),
                            md=12,
                            className="mt-5",
                        ),
                        
                    ),
                ],
                md=12,
            ),
            justify="center",
            className="mt-5",
            style={'color' : '#4f6d3a'},
        ),
        html.Br(),
        
    ],
    fluid=True,
    style={"min-height": "83vh", "fontSize": '1.5rem', 'color' : '#4f6d3a'},
)


try_llm_layout = html.Div([ 
                            html.Div([
                            dcc.Button('Summerize', id='summary_button', n_clicks=0,
                                       style= {'width': '100%', "backgroundColor": "#a56448", 'color' :  "white"}),
                            html.Br(),
                            html.Br(),
                            html.Div(
                                id="summary-output",
                                className="p-4 border rounded bg-light shadow-sm",
                                style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                            ),

                    ], style={'padding': 40, 'flex': 2}),


                html.Div(children=[
                                    html.Div(
                                            className="icon-container mx-auto",
                                            style={"maxWidth": "1000px",},
                                            children=[

                                                dcc.Input(
                                                    id="llm-search-input",
                                                    placeholder="Enter any question",
                                                    debounce=True,
                                                    style={"position":"relative"}
                                                )

                                            ]
                                    ),
                                    html.Br(),
                                    html.Div(
                                        id="llm_answer_area",
                                        className="p-4 border rounded bg-light shadow-sm",
                                        # className="answer-area",
                                        style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                                    )
                ], style={'padding': 40, 'flex': 2})
        ], 
        style={'display': 'flex', 'flexDirection': 'row'})


etl_layout = html.Div([
                            html.Div([
                            dcc.Upload(
                                        id='upload-docs',
                                        children=html.Div([
                                                            'Drag and Drop or ',
                                                            html.A('Select Files')
                                                        ]),
                                                        style={
                                                            'width': '50%',
                                                            'height': '40px',
                                                            'lineHeight': '40px',
                                                            'borderWidth': '4px',
                                                            # 'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'textAlign': 'center',
                                                            'margin': '10px',
                                                            "backgroundColor": "#e0926e",
                                                            'color' :  "black"
                                                        },
                                                        # Allow multiple files to be uploaded
                                                        multiple=False),
                            html.Br(),
                            html.Div(id='output-data-upload',
                                    className="answer-area",
                                    style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                                     ),
                            html.Br(),
                            dcc.Button('Extract, Transform and Load', id='transform_button', n_clicks=0,
                                       style= {'width': '50%', "backgroundColor": "#a56448", 'color' :  "white" }),
                            html.Br(),
                            html.Br(),
                            html.Div(
                                id="transform-output",
                                className="answer-area",
                                style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                            ),
                            html.Br(),
                            html.Br(),
                            dcc.Button('Create JSONL File for Fine Tuning', id='jsonl_button', n_clicks=0,
                                       style= {'width': '50%', "backgroundColor": "#a56448", 'color' :  "white" }),
                            html.Br(),
                            html.Br(),
                            html.Div(
                                id="jsonl-output",
                                className="answer-area",
                                style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                            ),
                            html.Br(),
                            html.Br(),
                            dcc.Button('Create Vector Embedding', id='embeddings_button', n_clicks=0,
                                       style= {'width': '50%', "backgroundColor": "#a56448", 'color' :  "white" }),
                            html.Br(),
                            html.Br(),
                            html.Div(
                                id="embeddings-output",
                                className="answer-area",
                                style= { "fontSize": '1rem', 'color' : '#4f6d3a'}
                            ),

                    ], style={'padding': 10, 'flex': 2}),


        ], 
        style={'display': 'flex', 'flexDirection': 'row'})


finetune_llm_layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.Div(
        className="icon-container mx-auto",
        style={"maxWidth": "1000px", 'color' : '#a25c3d'},
        children=[

            dcc.Input(
                id="finetune-search-input",
                placeholder="Enter any question",
                debounce=True,
                style={"position":"relative"}
            )

        ],
    ),

                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                html.Div(
                                    id="finetune-answer_area",
                                    # className="answer-area",
                                    className = "p-4 border rounded bg-light shadow-sm"
                                ),
                                type="circle",
                                color='#d02b27',
                            ),
                            md=12,
                            className="mt-5",
                        ),
                        
                    ),
                ],
                md=12,
            ),
            justify="center",
            className="mt-5",
            style={'color' : '#4f6d3a'},
        ),
        html.Br(),
        
    ],
    fluid=True,
    style={"min-height": "83vh", "fontSize": '1.5rem', 'color' : '#4f6d3a'},
)