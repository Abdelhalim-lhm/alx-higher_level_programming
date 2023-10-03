#!/usr/bin/python3
for i in range(90):
    if i < 89:
        is_dup = False
        double_i = "{:02d}".format(i)
        for j in range(i + 1, 100):
            double_j = "{:02d}".format(j)
            if set(double_i) == set(double_j):
                is_dup = True
                break 
        if is_dup:
            print("{:02d}, ".format(i), end='')
    else:
        print("{:02d}".format(i))
