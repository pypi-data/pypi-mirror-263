import json

class Document:
    def __init__(self):
        self.jsdoc = []

    def add_jsdoc(self, jsdoc):
        self.jsdoc.append(jsdoc)

    def __repr__(self):
        str = ""
        for jsdoc in self.jsdoc:
            str += f"\t{repr(jsdoc)}"
        return str
    
    def to_dict(self):
        return {
            "jsdoc": [jsdoc.to_dict() for jsdoc in self.jsdoc]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)
    
    def is_empty(self):
        return len(self.jsdoc) == 0

class JSDoc:
    def __init__(self):
        self.function_tag = None
        self.description_tag = None
        self.param_tags = []
        self.return_tag = None

    def set_function_tag(self, function_tag):
        self.function_tag = function_tag

    def set_description_tag(self, description_tag):
        self.description_tag = description_tag
    
    def add_param_tag(self, param_tag):
        self.param_tags.insert(0, param_tag)

    def set_return_tag(self, return_tag):
        self.return_tag = return_tag

    def __repr__(self):
        str = "JSDoc\n"
        if self.function_tag:
            str += f"\t\t{repr(self.function_tag)}\n"
        if self.description_tag:
            str += f"\t\t{repr(self.description_tag)}\n"
        for param_tag in self.param_tags:
            str += f"\t\t{repr(param_tag)}\n"
        if self.return_tag:
            str += f"\t\t{repr(self.return_tag)}\n"
        return str
    
    def to_dict(self):
        return {
            "function_tag": self.function_tag.to_dict() if self.function_tag else None,
            "description_tag": self.description_tag.to_dict() if self.description_tag else None,
            "param_tags": [param.to_dict() for param in self.param_tags],
            "return_tag": self.return_tag.to_dict() if self.return_tag else None
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

class Tag:
    def add_text(self, text):
        self.description += text

    def to_dict(self):
        return {
            "description": self.description
        }

class FunctionTag(Tag):
    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"FunctionTag({self.description})"
    
    def to_dict(self):
        return {
            "description": self.description
        }
    
class DescriptionTag(Tag):
    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return f"DescriptionTag({self.description})"

class ParamTag(Tag):
    def __init__(self, type, name, description):
        self.type = type
        self.name = name
        self.description = description

    def __repr__(self):
        return f"ParamTag({self.type}, {self.name}, {self.description})"
    
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description
        }

class ReturnTag(Tag):
    def __init__(self, type, description):
        self.type = type
        self.description = description

    def __repr__(self):
        return f"ReturnTag({self.type}, {self.description})"
    
    def to_dict(self):
        return {
            "type": self.type,
            "description": self.description
        }
    