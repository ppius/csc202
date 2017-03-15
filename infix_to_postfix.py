from string import ascii_uppercase, digits
from linear_adts import Stack
from par_checker import par_checker
#from [filename] import *

def infix_to_postfix(expr):
    """
    Convert infix arithmetic expression to postfix
      >>> infix_to_postfix('5 * 7')
      '5 7 *'
      >>> infix_to_postfix('A * B + C * D')
      'A B * C D * +'
      >>> infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )')
      'A B + C * D E - F G + * -'
      >>> infix_to_postfix('5 ( 7')
      'Invalid Expression'
      >>> infix_to_postfix(') 5 ( 7')
      'Invalid Expression'
      >>> infix_to_postfix('55 * 2')
      '55 2 *'
    """

    boo = par_checker(expr)
    if boo is not True:
        return 'Invalid Expression' 

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = expr.split()
    
    
    for token in token_list:
        if token in ascii_uppercase or token[:1] in digits:
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
              (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)


def eval_postfix(expr):
    """
    Evaluate a numerical postfix expression.
      >>> eval_postfix('3 2 +')
      '5'
      >>> eval_postfix('3 2 + 11 *')
      '55'
    """
    op_stack = Stack()
    token_list = expr.split()

    for token in token_list:
        if token[0] in digits:
            op_stack.push(token)
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            op_stack.push(str(eval(op1 + token + op2)))
    return op_stack.pop()



def eval_infix(expr):
    """
    Evaluate a numerical infix expression using infix_to_postfix and
    eval_postfix.
      >>> eval_infix('3 + 2')
      '5'
      >>> eval_infix('311 * 3')
      '933'
    """

    postfix = infix_to_postfix(expr)
    result = eval_postfix(postfix)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
