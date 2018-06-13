def rMod(n,mod):
    return n%mod;
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



c = input()
for i in range(c):
	num= input();
	fk=2**(2**num)+1;
	print fk;
	if (rMod(potmod(5,(fk-1)/2,fk),fk)==fk-1 or fk==5 ):
		print "PRIMO";
		print "---";
	else :
		print "COMPOSTO";
		print "---";
