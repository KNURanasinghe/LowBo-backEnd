# main.py

import os
from pdf_search.pdf_utils import extract_text_from_pdf, preprocess_text
from pdf_search.search_algorithm import search_in_pdf

def main():
    current_working_directory = os.getcwd()
    print("Current working directory:", current_working_directory)

    # Use forward slashes and specify the full path directly
    pdf_path = r'F:\Projects\react Project\LowBo-backEnd\pdfEditorAI\pdf_files\Lesson 1.pdf'
    print("Absolute path to PDF file:", pdf_path)

    user_input = input("Enter keyword or phrase: ")
    user_keyword = user_input.strip()

    try:
        pdf_text = extract_text_from_pdf(pdf_path)
        filtered_text = preprocess_text(pdf_text)

        context = search_in_pdf(filtered_text, user_keyword)  # Customize the context factor

        if context:
            print(f"Found details related to '{user_keyword}':")
            print(context)
        else:
            print(f"No details found for '{user_keyword}'.")

    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' does not exist.")

if __name__ == "__main__":
    main()
