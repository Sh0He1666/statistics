def stan_dev(my_list): #　標準偏差
    import statistics
    ave_list = statistics.mean(my_list) # リストの平均
    dub_list = 0 #　リストの二乗
    dis_list = 0 #　リストの分散
    for num in my_list:
        dub_list += (num - ave_list)**2

    dis_list = (dub_list/len(my_list))**(1/2)
    return dis_list

list = [0,1,2,3,5,5,7,8,9,10]
print(stan_dev(list))
