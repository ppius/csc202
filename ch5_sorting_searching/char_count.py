from string import ascii_uppercase, digits

def char_counts(s):
    """
    Return a list containing counts of the number of occurances of each
    ASCII character in s.

      >>> result = char_counts("this is seriously silly")
      >>> result[ord('t')]
      1
      >>> result[ord('i')]
      4
      >>> result[ord('2')]
      5
      >>> result2 = char_counts("abbcccddddeeeeeffffff")
      >>> result2[96:105]
      [0, 1, 2, 3, 4, 5, 6, 0, 0]
    """
    count = 0
    for ch in s:
        if letter == ch:
            ord(ch)
            count += 1
            chr(ch)
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
