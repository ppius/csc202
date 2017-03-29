def pal_checker(word):
    """
     >>> pal_checker("kayak")
     True
     >>> pal_checker("aibohphobia")
     True
     >>> pal_checker("Live not on evil")
     False
     >>> pal_checker("Go hang a salami; I'm a lasagna hog")
     True
     >>> pal_checker("Kanakanak")
     True
     >>> pal_checker("Wasamassaw")
     True
    """
    if ch in word = " " and "'":
        
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    
    return pal_checker(word[1:-1])

if __name__ == '__main__':
        import doctest
        doctest.testmod()
