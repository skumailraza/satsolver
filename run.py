
""" Created by Kumail Raza on 9-04-17 """

import sys, readline, parser
from logic import sol as solutions

def display(variables):
    if variables is True or variables is False:
        return variables
    else:
        return ", ".join( (v and " %s" or "!%s") % k 
                          for k,v in variables.iteritems() )

""" MAIN FUNCTION """

if __name__ == '__main__':
    print "******** Example Usage ************"
    print "> (p -> q) <=> (!p | q)"
    print "> p & !p"
    print "> (p -> q) & (q -> p) <=> p <-> q"
    print "Answers are for which the logical"
    print "formula is satisfied or otherwise"
    print "***********************************\n"

    while True:
        try:
            F = raw_input('> ').strip()
            if not F:
                continue
            
            while True:
                try:
                    sols = solutions(F)
                    break

                except EOFError:
                    F += " " + raw_input('... ').strip()
                    continue

                except SyntaxError, se:
                    # syntax error handling
                    print "! " + F 
                    sys.stdout.write('-' * (se.charnum + 2) + '^\n')
                    sys.stdout.write(se.mesg + '\n')
                    raise
            
            satisfied = False
            for solution in sols:
                print "= ", display(solution)
                satisfied = True
            if not satisfied:
                print "CONTRADICTION!"
            print 
        except SyntaxError, s:
            continue
        except (KeyboardInterrupt,EOFError):
            print
            break
    
