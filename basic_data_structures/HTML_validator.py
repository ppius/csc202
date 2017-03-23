from stack import Stack


def validateHTMLTags(htmlStr):
    stack = Stack()
    hsize = len(htmlStr)
    i = 0
    while i < hsize:
        tag = []
        openTag = True
        if htmlStr[i] == '<':
            tag.append('<')
            i += 1
            if htmlStr[i] == '/':
                openTag = False
                i += 1
            while (i < hsize) and htmlStr[i] == ' ':
                i += 1
            while (i < hsize) and (htmlStr[i].isalpha() or htmlStr[i].isdigit()):
                tag.append(htmlStr[i])
                i += 1
            while (i < hsize) and htmlStr[i] != '>':
                i += 1
            if (i >= hsize):
                return False
            tag.append(htmlStr[i])
            htmTag = ''.join(tag)
            if openTag:
                stack.push(htmTag)
            elif stack.is_empty():
                return False
            else:
                topTag = stack.pop()
                if topTag != htmTag:
                    return False
        i += 1
    if not stack.is_empty():
        return False
    return True
