import streamlit as st
from PyPDF2 import PdfReader
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Function to read the PDF file
def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to scrape content from a URL
def extract_url_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.get_text()

# Load pre-trained model for Question Answering
qa_pipeline = pipeline("question-answering")

# Function to answer a question based on the extracted text
def get_answer(context, question):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Streamlit UI
st.title("AI-Powered Learning Assistant for Students")
st.write("Upload your textbook PDF or enter a URL for study material.")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
text_from_pdf = ""
if uploaded_pdf:
    text_from_pdf = extract_pdf_text(uploaded_pdf)
    st.write("Text extracted from PDF:")
    st.text_area("Extracted Text", text_from_pdf, height=300)

# URL input
url_input = st.text_input("Enter URL for Educational Content")
text_from_url = ""
if url_input:
    text_from_url = extract_url_text(url_input)
    st.write("Text extracted from URL:")
    st.text_area("Extracted Text", text_from_url, height=300)

# Question input
question_input = st.text_input("Ask a Question")
if question_input:
    # Use the text extracted from PDF or URL
    context = text_from_pdf if uploaded_pdf else text_from_url
    if context:
        answer = get_answer(context, question_input)
        st.write(f"Answer: {answer}")
    else:
        st.write("Please upload a PDF or enter a URL first.")
