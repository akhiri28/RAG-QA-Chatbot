import dash
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
import dash_bootstrap_components as dbc
from src.process.realtime_process import get_answer, get_ft_answer
from src.process.try_llm import ask_question_with_openai, get_summary


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
            # return  (
            # f"{get_answer(user_query)}", f'{user_query}'
            # )
        
            return (html.Div([
        html.H3(f"Open AI Says :"),
        dcc.Markdown(
        get_answer(user_query), 
        className="summary-text-style"
    )
    ]), user_query)
        

def register_retllm_callback(app):
    @app.callback(
             Output("summary-output", "children"),
            Input("summary_button", "n_clicks"),
        prevent_initial_call=True
    )

    def handle_interactions(n_clicks):
        triggered_id = ctx.triggered_id

        
        if triggered_id == "summary_button":
            return  html.Div([
        html.H3(f"Summary of Docuemnts:"),
        dcc.Markdown(
        get_summary(), 
        className="summary-text-style"
    )
    ])
        
    @app.callback(
        [

            Output("llm_answer_area", "children"),
            # Output("llm-search-input", "value"),
        ],
        [
            Input("llm-search-input", "value")
        ],
        prevent_initial_call=True
    )

    def handle_interactions(user_query):
        triggered_id = ctx.triggered_id


        if triggered_id == "llm-search-input":
            return (html.Div([
        html.H3(f"Open AI Says :"),
        dcc.Markdown(
        ask_question_with_openai(user_query), 
        className="summary-text-style"
    )
    ]),)
            # print(ask_question_with_openai(user_query))
            # return  (
            # ask_question_with_openai(user_query),
            # )
        
def register_ftqa_callback(app):
    @app.callback(
        [

            Output("finetune-answer_area", "children"),
            Output("finetune-search-input", "value"),
        ],
        [
            Input("finetune-search-input", "value")
        ],
        prevent_initial_call=True
    )

    def handle_interactions(user_query):
        triggered_id = ctx.triggered_id


        if triggered_id == "finetune-search-input":
            # return  (
            # f"{get_answer(user_query)}", f'{user_query}'
            # )
        
            return (html.Div([
        html.H3(f"Open AI model gpt-3.5-turbo fine tuned with FAQ dataset - says :"),
        dcc.Markdown(
        get_ft_answer(user_query), 
        className="summary-text-style"
    )
    ]), user_query)