def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a_list2 = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
bubble_sort(a_list)
bubble_sort(a_list2)
print(a_list)
print(a_list2)
