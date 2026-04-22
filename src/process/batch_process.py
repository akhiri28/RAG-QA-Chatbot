import os

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


video_id = "Gfr50f6ZBvo" # only the ID, not full URL
api = YouTubeTranscriptApi()
try:
    # If you don’t care which language, this returns the “best” one

    transcript_list = api.fetch(video_id, languages=["en"])
    # Flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")


splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript], metadatas= [{ 'video_id': video_id}])

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

response = embeddings.embed_documents([chunk.page_content for chunk in chunks])
# 2. Create unique IDs and metadata for each chunk
ids = [str(i) for i in range(len(chunks))]
metadatas = [chunk.metadata | {"chunk_index": i} for i, chunk in enumerate(chunks)]

docs = [chunk.page_content for chunk in chunks]

import chromadb

# Connect to the server you just started
client = chromadb.HttpClient(host='127.0.0.1', port=8000)

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

collection = client.get_or_create_collection("youtube_transcripts")

collection.add(
embeddings=response,
documents=docs,
metadatas=metadatas,
ids=ids)
