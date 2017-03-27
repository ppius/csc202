#normal for loop function
def list_sum(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum

print(list_sum([1, 3, 5, 7, 9]))
print(list_sum([0]))
print(list_sum([13, 1, 9, 17, 5]))

#recursive function for list_sum
def ls_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + ls_sum(num_list[1:])

print(ls_sum([1, 3, 5, 7, 9]))
print(ls_sum([0]))
print(ls_sum([13, 1, 9, 17, 5]))
