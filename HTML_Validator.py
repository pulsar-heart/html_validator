#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    balanced = True
    index = 0
    tags = _extract_tags(html)
    s = []
    if len(tags) == 0:
            bool1 = '<' or '>' in html
            return not bool1
    while index < len(tags) and balanced:
        tag = tags[index]
        if '</' not in tag:
            s.append(tag)
        else:
            if len(s) == 0:
                balanced = False
            else:
                top = s.pop()
                top_word = top[1:-1]
                this_word = tag[2:-1]
                if not top_word == this_word:
                    balanced = False
        index += 1
    bool1 = balanced and len(s) == 0
    return bool1


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    is_tag = False
    tags = []
    this_tag = ''
    for symbol in html:
        if symbol == '<':
            is_tag = True
            this_tag += '<'
        elif is_tag:
            this_tag += symbol
            if symbol == '>':
                is_tag = False
                tags.append(this_tag)
                this_tag = ''
    return tags
