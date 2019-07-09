for i in range(1,10):
    for j in range(2,9):
        line = "{0} * {1:>2} = {2}".format(j,i,j*i)
        print(line,end="\t")
    print()
