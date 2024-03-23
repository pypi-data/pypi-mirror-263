class Token:
    def __repr__(self):
        return self.__class__.__name__[5:]

class TokenJSDocBegin(Token):
    pass

class TokenJSDocEnd(Token):
    pass

class TokenTag(Token):
    pass

class TokenTagFunction(TokenTag):
    pass

class TokenTagDescription(TokenTag):
    pass

class TokenTagParameter(TokenTag):
    pass

class TokenTagReturn(TokenTag):
    pass

class TokenTypeBegin(Token):
    pass

class TokenTypeEnd(Token):
    pass

class TokenTypeSymbol(Token):
    pass

class TokenNewLine(Token):
    pass

class TokenWord(Token):
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f"{self.__class__.__name__[5:]}({self.word})"
    
    def get_word(self):
        return self.word

