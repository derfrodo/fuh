
N = [1,2,3,4,5,6,7]
sigma = [0,4,7,6,1,2,3,5]

for a in N:
    print
    b=a
    print b,
    while sigma[b] != a:
        b=sigma[b]
        print b,
        N.remove(b)
