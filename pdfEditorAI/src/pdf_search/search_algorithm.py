# pdf_search/search_algorithm.py

import re

def search_in_pdf(pdf_text, keyword, fixed_context_size=200):
    keyword_lower = keyword.lower()
    keyword_regex = r'\b' + re.escape(keyword_lower) + r'\b'

    exact_match = re.search(keyword_regex, pdf_text.lower())

    if exact_match:
        # Exact word match
        keyword_index = exact_match.start()
        keyword_length = len(keyword_lower)

        # Calculate the context window dynamically based on the length of the keyword or phrase
        context_window = int(keyword_length / 2)

        start_index = max(0, keyword_index - context_window)
        end_index = min(len(pdf_text), keyword_index + keyword_length + context_window)

        # Ensure the context size is fixed
        context_size = fixed_context_size
        start_index = max(0, keyword_index - context_size // 2)
        end_index = min(len(pdf_text), start_index + context_size)

        context = ' '.join(pdf_text[start_index:end_index])
        return context
    else:
        # Substring match
        if keyword_lower in pdf_text.lower():
            return pdf_text.lower()
        else:
            return None
