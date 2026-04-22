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
                    create_search_input(),

                    dbc.Row(
                        dbc.Col(
                            dcc.Loading(
                                html.Div(
                                    id="answer_area",
                                    className="answer-area",
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
    style={"min-height": "83vh", "fontSize": '2rem', 'color' : '#4f6d3a'},
)




# @callback(
#     [

#         Output("answer_area", "children"),
#         Output("search-input", "value"),
#     ],
#     [
#         Input("search-input", "value")
#     ],
#     prevent_initial_call=True
# )

# def handle_interactions(user_query):
#     triggered_id = ctx.triggered_id


#     if triggered_id == "search-input":
#         return  (
#         f"Answer \n {get_answer(user_query)}", f'{user_query}'
#         )