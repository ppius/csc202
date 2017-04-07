def reverse_list(nlist):
    """
     >>> reverse_list([5, 4, 3, 2, 1])
     [1, 2, 3, 4, 5]
     >>> reverse_list([5])
     [5]
    """

    if len(nlist) == 1:
        return nlist
    rev_list = reverse_list(nlist[1:])
    rev_list.append(nlist[0])
    return rev_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()

