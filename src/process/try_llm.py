import docx2txt
from openai import OpenAI
import os
from pathlib import Path

# Initialize OpenAI client
client = OpenAI(api_key="")

def extract_text_from_docx(docx_path):
    """
    Extracts text from a Word document.
    """
    return docx2txt.process(docx_path)

# Get the path where your script is currently located
current_dir = Path(__file__).resolve().parent

# Go up one level and into a folder named 'external_storage'
save_path = current_dir.parent.parent / "data/raw_data"

# Full path for a file
# docx_path = save_path / "Data Engineering Zoomcamp FAQ.docx"

context = extract_text_from_docx(save_path / "Data Engineering Zoomcamp FAQ.docx") + \
extract_text_from_docx(save_path / "Machine Learning Zoomcamp FAQ.docx") + \
extract_text_from_docx(save_path / "MLOps Zoomcamp FAQ.docx")

def ask_question_with_openai(question):
    """
    Ask question using OpenAI model with document context.
    """
    try:
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based only on the provided document. Please limit your to 100 words or less"
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]

        response = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=messages,
            temperature=0.2,
            max_completion_tokens=1024,
            top_p=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
    

def get_summary():

        messages = [
            {
                "role": "system",
                "content": f"""You are an Academic Student Assistant for a higher-education platform. Your goal is to summerize a messy FAQ documents into a structured, easy-to-read guide for prospective students. You are professional, encouraging, and highly organized. 
                I have already extracted the document for you. The content of the document is {context}.
                """
            },
            {
                "role": "user",
                "content": """
I am providing you with a Word document containing a list of Frequently Asked Questions (FAQs) regarding our courses in Data Engineering (DE), Machine Learning (ML), and MLOps.
Please summarize this document according to the following requirements:
Categorized Summary: Group the information into four distinct sections:
1. General Admissions & Logistics (Fees, dates, eligibility).
2. Data Engineering Curriculum (Key tools, databases, pipelines).
3. ML & MLOps Curriculum (Models, deployment, monitoring, lifecycle).
4. Career & Projects (Capstone info, placement support).
5. Key Takeaways : At the very top, provide a "Top 3 Things Every Student Must Know" section.
Format: Use bullet points for readability. Use bold text for important deadlines or specific software tools mentioned (e.g., AWS, Docker, Spark).
Tone: Maintain a helpful "Student Assistant" voice—clear, concise, and welcoming.
Handling Missing Info: If a specific category above has no information in the text, simply omit that section.  
Do not give any date nformation.
Summary should be maximum of 100 words.
"""
            }
        ] 
        response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=messages,
        temperature=0.2,
        max_completion_tokens=1024,
        top_p=0.7)
        

        return response.choices[0].message.content  



