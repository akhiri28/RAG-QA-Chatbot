import dash
from dash import callback, html, dcc, Input, Output, State, ctx, ALL
import dash_bootstrap_components as dbc
from src.process import parse_data, batch_process
import json
import base64

from pathlib import Path

# Get the path where your script is currently located
current_dir = Path(__file__).resolve().parent
# print(current_dir)




def register_etl_callback(app):
    @app.callback(
            Output("transform-output", "children"),
            Input("transform_button", "n_clicks"),
        prevent_initial_call=True
    )

    def handle_interactions(n_clicks):

        # Go up one level and into a folder named 'external_storage'
        save_path = current_dir.parent.parent / "data/processed_data"

        # Create the folder if it doesn't exist
        save_path.mkdir(parents=True, exist_ok=True)

        # Full path for a file
        file_to_save = save_path / "documents.json"
        triggered_id = ctx.triggered_id


        if triggered_id == "transform_button":

            documents = parse_data.parse_data()

            with open(file_to_save, 'wt') as f_out:
                json.dump(documents, f_out, indent=2)
            return  (
            f"Extracted 3 .docx files from cloud. Tranformed the files to dictionary. Saved it as JSON Files in local Processed Folder"
            )
    
    @app.callback(
            Output("embeddings-output", "children"),
            Input("embeddings_button", "n_clicks"),
        prevent_initial_call=True
    )    
    def handle_interactions(n_clicks):
        triggered_id = ctx.triggered_id
        if triggered_id == "embeddings_button":
            batch_process.create_embeddings()
            return  (
            f"Created Vector embeddings from .json file using Open AI text-embedding-3-small model. The vector embeddings are stored in sqlite DB."
            )

    @app.callback(
        Output('output-data-upload', 'children'),
        Input('upload-docs', 'contents'),
        State('upload-docs', 'filename')
    )
    def save_pdf_locally(contents, filename):

        # Full path for a file
        SAVE_DIR = current_dir.parent.parent / "data/raw_data"
        SAVE_DIR.mkdir(parents=True, exist_ok=True)

        # if contents is None:
        #     return "Waiting for upload..."

        # 2. Extract the base64 data
        # Format: data:application/pdf;base64,JVBERi0xLjQK...
        if contents is not None:
            header, content_string = contents.split(',')
            decoded_data = base64.b64decode(content_string)

            # 3. Define the destination
            target_path = SAVE_DIR / filename

            try:
                # 4. Save the file "as is"
                with open(target_path, "wb") as f:
                    f.write(decoded_data)
                
                return (f"Successfully saved the file : {str(filename)}")
            except Exception as e:
                return (f"Error: {str(e)}")
            
    @app.callback(
            Output("jsonl-output", "children"),
            Input("jsonl_button", "n_clicks"),
        prevent_initial_call=True
    )

    def handle_interactions(n_clicks):

        # Go up one level and into a folder named 'external_storage'
        # save_path = current_dir.parent.parent / "data/processed_data"

        # Create the folder if it doesn't exist
        # save_path.mkdir(parents=True, exist_ok=True)

        # Full path for a file
        # file_to_save = save_path / "documents.json"
        triggered_id = ctx.triggered_id


        if triggered_id == "jsonl_button":

            parse_data.convert_json_to_jsonl()

            # with open(file_to_save, 'wt') as f_out:
            #     json.dump(documents, f_out, indent=2)
            return  (
            f"Converted JSON file to JSONL file format. Saved the JSONL File in local Processed Folder"
            )