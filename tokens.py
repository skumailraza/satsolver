
import ply.lex as lex

#### TOKENS HERE ####
tokens = (
    'FALSE',
    'TRUE',
    'EXISTS',
    'ATOM',
    'AND',
    'OR',
    'NOT',
    'LPAR',
    'RPAR',
    'IF',
    'FI',
    'IFF',
    'EQL',
    'COMMA',
    'ORD2',
)

### TOKENS MEANING ###
t_COMMA = r','
t_EXISTS = r'3'
t_AND = r'&'
t_OR  = r'\|'
t_NOT = r'!'
t_EQL  = r'<=>' 
t_IFF  = r'<->'
t_IF   = r'->'
t_FI   = r'<-'
t_ORD2 = r'<(?![=-])|<=(?!>)|>=?'
t_LPAR = r'\('
t_RPAR = r'\)'
t_ATOM = r'[a-z][a-z0-9_]*'

def t_FALSE(t):
    r'0'
    t.value = False
    return t

def t_TRUE(t):
    r'1'
    t.value = True
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

t_ignore = ' \t\n'

lexer = lex.lex()