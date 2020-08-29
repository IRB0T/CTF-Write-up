with open('b.txt','r') as f:
    for i in f:
        for j in i:
            for k in j:
                if k.isupper():
                    print(k,end='')
