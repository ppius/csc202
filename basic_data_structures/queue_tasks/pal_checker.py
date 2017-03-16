from deque import Deque

def pal_checker(a_string):
    """
      >>> pal_checker("lsdkjfskf")
      False
      >>> pal_checker("radar")
      True
      >>> pal_checker("short")
      False
      >>> pal_checker("mom")
      True
    """
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal
            
if __name__ == '__main__':
    import doctest
    doctest.testmod()
