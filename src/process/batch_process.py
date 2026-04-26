import os
os.environ["OPENAI_API_KEY"] = ""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import chromadb
from pathlib import Path
import json


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# Connect to the server you just started
client = chromadb.HttpClient(host='127.0.0.1', port=8000)
# embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")
collection = client.get_or_create_collection("datatalks-qa")

# Get the path where your script is currently located
current_dir = Path(__file__).resolve().parent
# print(current_dir)

# Go up one level and into a folder named 'external_storage'
save_path = current_dir.parent.parent / "data/processed_data"

# Full path for a file
file_path = save_path / "documents.json"

# Read data
with open(file_path, 'r') as file:
    data = json.load(file)

def create_embeddings():

    for d in data:
        course_text = ''
        for doc in d['documents']:
            text = doc['question'] + ' ' + doc['text']
            course_text = course_text + text

        chunks = splitter.create_documents([course_text], metadatas= [{ 'course': d['course']}])
        response = embeddings.embed_documents([chunk.page_content for chunk in chunks])
        ids = [d['course'] + '_' + str(i) for i in range(len(chunks))]
        metadatas = [{'course' : d['course']} for i, chunk in enumerate(chunks)]

        docs = [chunk.page_content for chunk in chunks]
        collection.add(
        embeddings=response,
        documents=docs,
        metadatas=metadatas,
        ids=ids)


