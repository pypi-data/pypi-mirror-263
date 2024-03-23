import re

COMMENT         = re.compile(r'/\*\*.*?\*/', re.DOTALL)

JSDOC_BEGIN     = re.compile(r'\/\*\*')
JSDOC_END       = re.compile(r'\*\/')
TAG_FUNCTION    = re.compile(r'@(function|func)')
TAG_DESCRIPTION = re.compile(r'@(description|desc)')
TAG_PARAM       = re.compile(r'@(parameter|param|argument|arg)')
TAG_RETURN      = re.compile(r'@(returns|return)')
TYPE_BEGIN      = re.compile(r'{')
TYPE_END        = re.compile(r'}')
NEW_LINE        = re.compile(r'\*')
WORD            = re.compile(r"[\w']+|\.")

JSDOC = re.compile(
    JSDOC_BEGIN.pattern     + '|' +
    JSDOC_END.pattern       + '|' +
    TAG_FUNCTION.pattern    + '|' +
    TAG_DESCRIPTION.pattern + '|' +
    TAG_PARAM.pattern       + '|' +
    TAG_RETURN.pattern      + '|' +
    TYPE_BEGIN.pattern      + '|' +
    TYPE_END.pattern        + '|' +
    NEW_LINE.pattern        + '|' +
    WORD.pattern
)
