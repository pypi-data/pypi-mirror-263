from . import lexical_tokens as tk
from . import jsdoc_data as jd

# Token Errors handling
class WrongTokenError(Exception):
    def __init__(self, tokenFound, *tokensExpected):
        self.tokenFound = tokenFound
        self.tokensExpected = tokensExpected

    def __str__(self):
        found_str = self.tokenFound
        expected_str = " or ".join(str(token) for token in self.tokensExpected)
        return f"Syntax Error: Token found: {found_str}, Tokens expected: {expected_str}"

# Reading tokens
def consumme_token(tokens):
    return tokens.pop(0)

def first_token(tokens):
    return tokens[0]

# Symbol parsing
def accept_symbol(tokens, target):

    token = first_token(tokens)

    if isinstance(token, target):
        return consumme_token(tokens)
    else:
        raise WrongTokenError(token, target)
    
# Text parsing
def accept_text(tokens):
    # 19: Text -> word Texte {word}
    # 20: Text -> ε {*, '}', */}

    word_token = accept_symbol(tokens, tk.TokenWord)

    text = word_token.get_word()

    token = first_token(tokens)

    if isinstance(token, tk.TokenWord): # 19
        next_text = accept_text(tokens)
        text += " " + next_text
    elif isinstance(token, tk.TokenTypeEnd): # 20
        pass
    elif isinstance(token, tk.TokenNewLine): # 20
        pass
    elif isinstance(token, tk.TokenJSDocEnd): # 20
        pass
    else:
        raise WrongTokenError(token, tk.TokenWord, tk.TokenTypeEnd, tk.TokenNewLine, tk.TokenJSDocEnd)
    
    return text

# Type parsing
def accept_type(tokens):
    # 18: Type -> { Texte } { '{' }

    accept_symbol(tokens, tk.TokenTypeBegin)
    text = accept_text(tokens)
    accept_symbol(tokens, tk.TokenTypeEnd)

    return text

# Function Tag parsing
def accept_function_tag(tokens):
    # 17: FunctionTag -> @function Texte {word}

    accept_symbol(tokens, tk.TokenTagFunction)
    description_text = accept_text(tokens)

    return jd.FunctionTag(description_text)

# Description Tag parsing
def accept_description_tag(tokens):
    # 16: DescriptionTag -> description Texte {word}
    
    accept_symbol(tokens, tk.TokenTagDescription)
    description_text = accept_text(tokens)

    return jd.DescriptionTag(description_text)

# Param Tag parsing
def accept_param_tag(tokens):
    # 15: ParamTag -> @param Type word Texte { '{' }

    accept_symbol(tokens, tk.TokenTagParameter)
    type = accept_type(tokens)
    word_token = accept_symbol(tokens, tk.TokenWord) # Name of the parameter
    param_name = word_token.get_word()
    description_text = accept_text(tokens)

    return jd.ParamTag(type, param_name, description_text)

# Return Tag parsing
def accept_return_tag(tokens):
    # 14: ReturnTag -> @return Type Texte {word}

    accept_symbol(tokens, tk.TokenTagReturn)
    type = accept_type(tokens)
    description_text = accept_text(tokens)

    return jd.ReturnTag(type, description_text)

# Tag parsing
def accept_tag(tokens):
    # 10: Tag -> FunctionTag {function}
    # 11: Tag -> DescriptionTag {description}
    # 12: Tag -> ParamTag {param}
    # 13: Tag -> ReturnTag {return}

    tag = None

    token = first_token(tokens)

    if isinstance(token, tk.TokenTagFunction): # 10
        tag = accept_function_tag(tokens)
    elif isinstance(token, tk.TokenTagDescription): # 11
        tag = accept_description_tag(tokens)
    elif isinstance(token, tk.TokenTagParameter): # 12
        tag = accept_param_tag(tokens)
    elif isinstance(token, tk.TokenTagReturn): # 13
        tag = accept_return_tag(tokens)
    else:
        raise WrongTokenError(token, tk.TokenTagFunction, tk.TokenTagDescription, tk.TokenTagParameter, tk.TokenTagReturn)
    
    return tag

# Expression parsing
def accept_expression(tokens):
    # 6: Expression -> * Tag {@}
    # 7: Expression -> * Texte {word}
    # 8: Expression -> * {*}
    # 9: Expression -> ε {*/}

    tag = None
    text = ""

    accept_symbol(tokens, tk.TokenNewLine)
    
    token = first_token(tokens)
    
    if isinstance(token, tk.TokenTag): # 6
        tag = accept_tag(tokens)
    elif isinstance(token, tk.TokenWord): # 7
        text = " " + accept_text(tokens)
    elif isinstance(token, tk.TokenNewLine): # 8
        pass
    elif isinstance(token, tk.TokenJSDocEnd): # 9
        pass
    else:
        raise WrongTokenError(token, tk.TokenTag, tk.TokenWord, tk.TokenNewLine, tk.TokenJSDocEnd)
    
    return tag, text

# Line parsing
def accept_line(tokens):
    # 4: Line -> Expression Line {*, */}
    # 5: Line -> ε {*/}

    token = first_token(tokens)

    if isinstance(token, tk.TokenNewLine): # 4
        tag, text = accept_expression(tokens)
 
        tags, texts = accept_line(tokens)

        if tag != None: # Get a tag
            tag.add_text(texts) # Add the previous texts to the tag
            texts = "" # flush the texts
            tags.append(tag)

        elif text != "": # Get a text
            texts += text # Concatenate the texts

    elif isinstance(token, tk.TokenJSDocEnd): # 5
        tags = []
        texts = ""
    else:
        raise WrongTokenError(token, tk.TokenNewLine, tk.TokenJSDocEnd)
    
    return tags, texts # List of tags of the current line and below

# JSDoc parsing
def accept_jsdoc(tokens):
    # 3: JSDoc -> '/**' Line '*/' {*}

    jsdoc = jd.JSDoc()

    accept_symbol(tokens, tk.TokenJSDocBegin)
    tags, _ = accept_line(tokens)
    accept_symbol(tokens, tk.TokenJSDocEnd)

    for tag in tags:
        if isinstance(tag, jd.FunctionTag):
            jsdoc.set_function_tag(tag)
        elif isinstance(tag, jd.DescriptionTag):
            jsdoc.set_description_tag(tag)
        elif isinstance(tag, jd.ParamTag):
            jsdoc.add_param_tag(tag)
        elif isinstance(tag, jd.ReturnTag):
            jsdoc.set_return_tag(tag)

    return jsdoc

# Document parsing
def analysis(document):
    # 1: Document -> JSDoc Document
    # 2: Document -> ε

    document_data = jd.Document()

    for jsdoc in document:
        jsdoc = accept_jsdoc(jsdoc)
        document_data.add_jsdoc(jsdoc)

    return document_data

# Abstract Syntax Tree

# 1:    Document        -> JSDoc Document
# 2:    Document        -> ε
# 3:    JSDoc           -> '/**' Line '*/'          {*}
# 4:    Line            -> Expression Line          {*, */}
# 5:    Line            -> ε                        {*/}
# 6:    Expression      -> * Tag                    {@}
# 7:    Expression      -> * Texte                  {word}
# 8:    Expression      -> *                        {*}
# 9:    Expression      -> ε                        {*/}
# 10:   Tag             -> FunctionTag              {function}
# 11:   Tag             -> DescriptionTag           {description}
# 12:   Tag             -> ParamTag                 {param}
# 13:   Tag             -> ReturnTag                {return}
# 14:   FunctionTag     -> @return Type Texte       {word}
# 15:   ParamTag        -> @param Type word Texte   { '{' }
# 16:   DescriptionTag  -> description Texte        {word}
# 17:   ReturnTag       -> @return Type Texte       {word}
# 18:   Type            -> { Texte }                { '{' }
# 19:   Texte           -> word Texte               {word}
# 20:   Texte           -> ε                        {*, '}', */}
