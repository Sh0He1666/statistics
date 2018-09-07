def by_ave(my_list):# 平均差
    i = 0
    total = 0
    list_len = len(my_list)
    while i < list_len:
        for j in my_list:
            ave_dic = ((my_list[i] - j) ** 2) ** 0.5 / list_len ** 2
            total += ave_dic
        i += 1
    print(total)


