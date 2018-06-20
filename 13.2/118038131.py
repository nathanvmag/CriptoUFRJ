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
def Mers(n):
	return (2**n) -1

control =input();
for c in range(control):
	num =input();
	mer= Mers(num);
	print mer;
	aux=0;
	r= int(((2**num)**0.5))/(2*num);
	print r;
	for i in range(1,r+1):
		print i;
		q= 1+2*i*num;
		if(rMod(potmod(2,num,q),q)==1):
			print q;
			aux=0;
			print"---";
			break;
		else:
			aux=999;
	if (r==0 or aux !=0):
		print mer;
		print "---";
	