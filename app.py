import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
from src.layouts.qa_layout import layout
from src.callbacks.QA_callback import register_qa_callback


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
                dcc.Tab(label = 'Try LLM',
                style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},),
        dcc.Tab(label = 'Fine Tune LLM',
                style = {'fontWeight': "bold", "fontSize": '1.5rem', 'color': '#d16b00'},),
        dcc.Tab(label = 'Q & A Chat Bot', 
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

if __name__ == "__main__":
    app.run(debug=True)