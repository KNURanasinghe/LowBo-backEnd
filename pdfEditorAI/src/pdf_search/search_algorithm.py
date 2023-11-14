# pdf_search/search_algorithm.py

import re

def search_in_pdf(pdf_text, keyword, special_character='***'):
    keyword_lower = keyword.lower()
    keyword_regex = r'\b' + re.escape(keyword_lower) + r'\b'

    special_character_index = pdf_text.lower().find(special_character)

    if special_character_index != -1:
        # Special character found, let's find the keyword
        exact_match = re.search(keyword_regex, pdf_text.lower())

        if exact_match:
            # Keyword found, determine the appropriate context
            keyword_index = exact_match.start()

            # Determine the end of the context based on the "***" tag
            end_tag_index = pdf_text.lower().find(special_character, keyword_index)
            if end_tag_index != -1:
                context = pdf_text[keyword_index:end_tag_index + len(special_character)]
                return context

    return None
