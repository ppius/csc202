def print_pascal_triangle(nrow):
    print_row([1], nrow)
    pascal_triangle(nrow-1, [1])


def pascal_triangle(nrow, rlist):
    if nrow == 0:
        return
    tmp_row = []
    tmp_row.append(rlist[0])
    for i in range(0, len(rlist)-1):
        # print (rlist)
        tmp_row.append(rlist[i] + rlist[i+1])
    tmp_row.append(rlist[-1])
    print_row(tmp_row, nrow)
    pascal_triangle(nrow-1, tmp_row)

