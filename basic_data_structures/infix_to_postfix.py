from linear_adts import Stack

def infix_to_postfix(infix_expr):
    """
      >>> infix_to_postfix("(A + B) * (C + D)")
      'A B + C D + *'
      >>> infix_to_postfix("A + B * C")
      'A B C * +'
      >>> infix_to_postfix("(A + B) * C - (D - E) * (F + G)")
      'A B + C * D E - F G + * -'
    """
    
    prec = {} 
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2 
    prec["-"] = 2 
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = list(infix_expr.split(" "))
    char_tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_tokens = "1234567890"

    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
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
