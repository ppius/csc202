from string import ascii_uppercase, digits
from linear_adts import Stack


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
    """

    balanced = True
    index = 0

    while index < len(expr) and balanced:
        s = Stack()
        char = expr[index]
        if char == '(':
            s.push(char)
        else:
            if char != '(' and char != ')':
                None
            elif s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    return balanced and s.is_empty()

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
        if token in ascii_uppercase or token in digits:
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
