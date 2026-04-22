import dash
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
import dash_bootstrap_components as dbc
from src.process.realtime_process import get_answer


def register_qa_callback(app):
    @app.callback(
        [

            Output("answer_area", "children"),
            Output("search-input", "value"),
        ],
        [
            Input("search-input", "value")
        ],
        prevent_initial_call=True
    )

    def handle_interactions(user_query):
        triggered_id = ctx.triggered_id


        if triggered_id == "search-input":
            return  (
            f"{get_answer(user_query)}", f'{user_query}'
            )