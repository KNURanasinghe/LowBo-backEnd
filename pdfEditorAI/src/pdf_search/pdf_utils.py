# pdf_search/pdf_utils.py
import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text

def preprocess_text(text):
    # Add your preprocessing steps here
    # For example, remove special characters, extra whitespaces, etc.
    processed_text = re.sub(r'\s+', ' ', text)
    return processed_text
