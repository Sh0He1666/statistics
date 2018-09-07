def my_covari(list1, list2): # 共分散
    import stan_dev
    import statistics
    # Standard Deviations
    s1 = stan_dev.stan_dev(list1)
    s2 = stan_dev.stan_dev(list2)
    n = len(list1)
    s12 = 0
    # Average of each list
    ave_list1 = statistics.mean(list1)
    ave_list2 = statistics.mean(list2)
    # Decrement between ave and sample
    dec_list = 0
    for (samp1, samp2) in zip(list1, list2):
        dec_list = dec_list + (samp1 - ave_list1) *(samp2 - ave_list2)

    s12 = (dec_list/n)/(s1*s2)
    return s12
    
