import streamlit as st
from PyPDF2 import PdfReader  # PDF extraction library
import requests
from bs4 import BeautifulSoup

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

# Streamlit UI
st.title("AI-Powered Learning Assistant for Students")
st.write("Upload your textbook PDF or enter a URL for study material.")

# Upload PDF
uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")
if uploaded_pdf:
    text_from_pdf = extract_pdf_text(uploaded_pdf)
    st.write("Text extracted from PDF:")
    st.text_area("Extracted Text", text_from_pdf, height=300)

# URL input
url_input = st.text_input("Enter URL for Educational Content")
if url_input:
    text_from_url = extract_url_text(url_input)
    st.write("Text extracted from URL:")
    st.text_area("Extracted Text", text_from_url, height=300)
