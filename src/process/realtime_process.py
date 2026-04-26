import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
import chromadb
os.environ["OPENAI_API_KEY"] = ""

# Connect to the server you just started
client = chromadb.HttpClient(host='127.0.0.1', port=8000)
collection = client.get_or_create_collection("datatalks-qa")
# Get embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
# 4. Search Chroma
llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0.2)
ft_llm = ChatOpenAI(model="ft:gpt-3.5-turbo-0125:personal::DYunoBkh", temperature=0.2)
# Prompt Template

prompt = PromptTemplate(
    template="""
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION. Please limit your to 100 words. Dont give information about the year of course.

QUESTION: {question}

CONTEXT: 
{context}
    """,
    input_variables = ['context', 'question']
)


def get_answer(user_question):
    query_vector = embeddings.embed_query(user_question)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=5,  # Number of matching chunks to return
        include=["documents", "metadatas", "distances"]
    )

    context_text = "\n\n".join(doc for doc in results['documents'][0])

    final_prompt = prompt.invoke({"context": context_text, "question": user_question})

    answer = llm.invoke(final_prompt)

    return answer.content

def get_ft_answer(user_question):
    query_vector = embeddings.embed_query(user_question)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=5,  # Number of matching chunks to return
        include=["documents", "metadatas", "distances"]
    )

    context_text = "\n\n".join(doc for doc in results['documents'][0])

    final_prompt = prompt.invoke({"context": context_text, "question": user_question})

    answer = ft_llm.invoke(final_prompt)

    return answer.content


# Prompt
# SYSTEM_PROMPT = """You are a highly knowledgeable and specialized tutor in GitHub.
# Your goal is to help users effectively understand and use GitHub for practical applications and exam certification.

# SCOPE:
# - You must answer ONLY questions about GitHub and its official documentation.
# - You must use ONLY the provided Documents context. If the context is empty or not clearly relevant to the user's question, you MUST refuse with the template below.
# - Do NOT invent, guess, or use outside knowledge.

# REFUSAL TEMPLATE (use exactly this when out of scope or low relevance):
# ###### This assistant only answers questions about GitHub's official documentation. 

# MANDATORY FORMATTING RULES:
# - NEVER use additional information or further reading with links.
# - You MUST treat ###### as plain section labels, not visual titles.
# - NEVER emphasize headers visually.
# - If you need emphasis, use **bold text**, never headers.

# Guidelines:
# 1. Provide a working example with commands.
# 2. Give a clear, beginner-friendly explanation.
# 3. Structure your response with clear sections and subsections.
# 4. Use bullet points for lists and numbered lists when appropriate.
# 5. If you don't know the answer, do not fabricate one.

# Documents:
# {context}
# """

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", SYSTEM_PROMPT),
#         ("human", "{input}"),
#     ]
# )

# from langchain_core.runnables import RunnableLambda


# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)


# def normalize_markdown_headers(text: str) -> str:
#     """
#     Converte qualquer header Markdown (#, ##, ###, ####, #####)
#     para ######, garantindo tamanho pequeno.
#     """
#     # substitui linhas que começam com 1 a 5 #
#     text = re.sub(r"(?m)^(#{1,5})\s+", "###### ", text)
#     return text


# # RAG Chain
# rag_chain = (
#     {
#         "context": retriever | RunnableLambda(format_docs),
#         "input": RunnablePassthrough(),
#     }
#     | prompt
#     | llm
#     | StrOutputParser()
#     | RunnableLambda(normalize_markdown_headers)
# )
