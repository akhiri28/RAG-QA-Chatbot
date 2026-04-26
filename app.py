import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
from src.layouts.qa_layout import layout , try_llm_layout, finetune_llm_layout, etl_layout
from src.callbacks.qa_callback import register_qa_callback , register_retllm_callback, register_ftqa_callback
from src.callbacks.etl_callback import register_etl_callback


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
)


# main
# content = html.Div(
#     className="page-content",
# )


# # layout
# app.layout = dbc.Container(

#     children = [
#         html.H2("API Based Cloud Native Solutions - Assignment 2", className = "text-center my-3 fw-bold", 
#     style = {'fontWeight': "bold", "fontSize": '2rem', 'color': '#1f3735'}),
#         dcc.Tab(label = 'Q & A Chat Bot'),
#         html.Div( 

#             children = [
#                 content,
#                 html.Div(layout, className="page-content",
#                          style = {'fontWeight': "bold", "fontSize": '2rem'}),
#             ]
#         ),

# ], fluid = True)


# layout
app.layout = dbc.Container([


    html.H2("API Based Cloud Native Solutions - Assignment 2", className = "text-center my-3 fw-bold", 
    style = {'fontWeight': "bold", "fontSize": '2rem', 'color': '#a25c3d'}),

    dcc.Tabs(id = 'tabs', children = [
                dcc.Tab(
                        label = 'ETL',
                        style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},
                        children = [
                            # content,
                            html.Div(etl_layout),
                            ]
                        ),
                dcc.Tab(
                        label = 'LLM with Fixed Context',
                        style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},
                        children = [
                            # content,
                            html.Div(try_llm_layout),
                            ]
                        ),
                dcc.Tab(label = 'Fine Tuned LLM',
                        style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},
                        children = [
                            html.Div(finetune_llm_layout),
                        ]),

                dcc.Tab(label = 'RAG Based Q & A Chat Bot', 
                        style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},
                        children = [
                        # content,
                        html.Div(layout, #className="page-content",
                                #  style = {"fontSize": '2rem', 'color' : '#4f6d3a'}
                                ),
                ]
                ),

    
    ]),
  

], fluid = True)

register_qa_callback(app)
register_retllm_callback(app)
register_etl_callback(app)
register_ftqa_callback(app)

if __name__ == "__main__":
    app.run(debug=True)