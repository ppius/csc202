from string import ascii_uppercase, digits

def char_counts(s):
    """
    Return a list containing counts of the number of occurances of each
    ASCII character in s.

      >>> result1 = char_counts("abbcccddddeeeeeffffff")
      >>> len(result1)
      256
      >>> result1[96:105]
      [0, 1, 2, 3, 4, 5, 6, 0, 0]
      >>> result2 = char_counts("AACEEEGIIJLLL")
      >>> result2[64:78]
      [0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 1, 0, 3, 0]
      >>> result3 = char_counts("this is seriously silly")
      >>> result3[ord('t')]
      1
      >>> result3[ord('i')]
      4
      >>> result3[ord('2')]
      5
    """
    counts = [0] * 256

    for ch in s:
        counts[ord(ch)] += 1
    return counts

if __name__ == '__main__':
    import doctest
    doctest.testmod()
