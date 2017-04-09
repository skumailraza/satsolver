
""" Created by Kumail Raza on 9-04-17 """

from parser import parse, SyntaxError
### AND FUNCTION ###
def and_(prp1, prp2):
    if isinstance(prp1, bool) and prp1:
        return prp2
    elif isinstance(prp1, bool) and not prp1:
        return False
    elif isinstance(prp2, bool) and prp2:
        return prp1
    elif isinstance(prp2, bool) and not prp2:
        return False
### OR FUNCTION ###
def or_(prp1, prp2):
    if isinstance(prp1, bool) and prp1:
        return True
    elif isinstance(prp1, bool) and not prp1:
        return prp2
    elif isinstance(prp2, bool) and prp2:
        return True
    elif isinstance(prp2, bool) and not prp2:
        return prp1
### IMPLICATION FUNCTION ###
def if_(prp1, prp2):
    if isinstance(prp1, bool) and prp1:
        return prp2
    elif isinstance(prp1, bool) and not prp1:
        return True
    elif isinstance(prp2, bool) and prp2:
        return True
### REVERSE IMPLICATON FUNCTION ###
def fi_(prp1, prp2):
    return if_(prp2, prp1)
### NOT FUNCTION ###
def not_(arg):
    if isinstance(arg, bool):
        return not arg

### BICONDITIONAL FUNCTION ###
def iff_(prp1, prp2):
#     if isinstance(prp1, bool) and isinstance(prp2, bool):
#         return prp1 == prp2
    return if_(prp1,prp2) and if_(prp2,prp1);
### EQUIVALENCE FUNCTION ####
def equiv_(prp1, prp2):
    F = [iff_, prp1, [not_, prp2]]
    if satisfiable(F):
        return False
    else:
        return True
### IDENTITY FUNCTION ###
def ident_(*args):
    return args


op_functions = {
    '!': not_,
    '->': if_,
    '<->': iff_,
    '&': and_,
    '|': or_,
    '<=>': equiv_,
    }

macros = [
    ident_,
]

def parse2ast(L):
    if isinstance(L, list) and len(L) >= 2:
        operator = op_functions[L[0]]
        if operator in macros:
            return operator(*map(parse2ast, L[1:]))
        else:
            return [operator] + map(parse2ast, L[1:])
    elif isinstance(L, list) and len(L) == 1:
        return parse2ast(L[0])
    else:
        return L

def yield_unbounds(F):
    all_unbounds = []
    if isinstance(F, list):
        for arg in F[1:]:
            for unbound in yield_unbounds(arg):
                if unbound not in all_unbounds:
                    all_unbounds.append(unbound)
                    yield unbound
    elif isinstance(F, str):
        all_unbounds.append(F)
        yield F

def next_unbound(F):
    for unbound in yield_unbounds(F):
        return unbound
    raise StopIteration

def simplify(F, bindings=dict(), infer=True):
    # Simplifies the wff to it's values for further calculation
    if isinstance(F, list):
        fn = F[0]
        args = [simplify(a, bindings, infer) for a in F[1:]]
        r = fn(*args)
        if r is not None and infer:
            return r
        else:
            return [fn] + args
    elif isinstance(F, str) and F in bindings:
        return bindings[F]
    else:
        return F

def dpll(F, bindings=dict()):
    F = simplify(F, bindings)
    
    if F is True:
        yield bindings or F
        return
    elif F is False:
        return
    
    L = next_unbound(F)
    
    bindings1 = bindings.copy()
    bindings1[L] = True
    for sat in dpll(F, bindings1):
        yield sat

    bindings2 = bindings.copy()
    bindings2[L] = False
    for sat in dpll(F, bindings2):
        yield sat

def satisfiable(F):
    for sat in dpll(F):
        return sat
    return False

def sol(exprstr):
    expression = parse2ast(parse(exprstr))
    return dpll(expression)
    
