def rMod(n, mod):
    return n % mod


def potmod(n1, n2, n3):
    R = 1
    A = n1
    E = n2
    while E != 0:
        if E % 2 == 1:
            print R, A, E, 'S'
            R = rMod(R * A, n3)
            E = (E - 1) / 2
            A = rMod(A * A, n3)
        else:
            print R, A, E, 'N'
            E /= 2
            A = rMod(A * A, n3)
    print R, A, E, 'N'
    return R


n = input()
for i in range(n):

    (n2, n3) = input()
    n2 = n2 - 1
    exp = n2
    k = 0
    q = n2
    while n2 % 2 == 0:
        n2 = n2 / 2
        k = k + 1

    q = q / 2 ** k
    print k, q
    pt = potmod(n3, q, exp + 1)
    if pt == 1 or pt == exp:
        print 'INCONCLUSIVO'
        print '---'
    else:
        i = 1
        print i * q, pt;
        while (i < k):
        	q=q* 2;
        	pt = rMod(pt ** 2, exp + 1)
        	if pt == exp:
        		print q, pt; 
        		print 'INCONCLUSIVO'
        		print '---'
        		break
        	i = i + 1
        	print q, pt;            
        if (pt != exp):
            print 'COMPOSTO'
            print '---'
