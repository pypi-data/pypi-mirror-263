import re
from . import lexical_regex as rx
from . import lexical_tokens as tk

# JSON DOCUMENT EXTRACTION
def extract_comments(texte):
    matches = re.findall(rx.COMMENT, texte)
    comments = [comment.strip() for comment in matches]
    return comments

# PARSE TOKEN
def parse_token(token):
    if rx.JSDOC_BEGIN.match(token):
        return tk.TokenJSDocBegin()
    elif rx.JSDOC_END.match(token):
        return tk.TokenJSDocEnd()
    elif rx.TAG_FUNCTION.match(token):
        return tk.TokenTagFunction()
    elif rx.TAG_DESCRIPTION.match(token):
        return tk.TokenTagDescription()
    elif rx.TAG_PARAM.match(token):
        return tk.TokenTagParameter()
    elif rx.TAG_RETURN.match(token):
        return tk.TokenTagReturn()
    elif rx.TYPE_BEGIN.match(token):
        return tk.TokenTypeBegin()
    elif rx.TYPE_END.match(token):
        return tk.TokenTypeEnd()
    elif rx.NEW_LINE.match(token):
        return tk.TokenNewLine()
    elif rx.WORD.match(token):
        return tk.TokenWord(token)
    
    return tk.Token()

# LEXICAL ANALYSIS
def analysis(texte):
    document = []

    # Extract comments from the file
    for comment in extract_comments(texte):
        tokens = []

        # Get all words and symbols in the comment
        for match in re.finditer(rx.JSDOC, comment):
            token = match.group(0)
            tokens.append(parse_token(token)) # Append the corresponding token

        document.append(tokens)

    return document
