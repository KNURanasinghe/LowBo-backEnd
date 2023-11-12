from flask import Flask, request, jsonify
from pdf_search.pdf_utils import extract_text_from_pdf, preprocess_text
from pdf_search.search_algorithm import search_in_pdf

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    pdf_path = 'pdf_files/sample.pdf'  # Update with your PDF file path
    user_keyword = request.args.get('keyword', '')

    try:
        pdf_text = extract_text_from_pdf(pdf_path)
        filtered_text = preprocess_text(pdf_text)

        context = search_in_pdf(filtered_text, user_keyword)

        if context:
            response = {'status': 'success', 'result': context}
        else:
            response = {'status': 'error', 'message': f'No details found for "{user_keyword}".'}
    except FileNotFoundError:
        response = {'status': 'error', 'message': f'The file "{pdf_path}" does not exist.'}

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
