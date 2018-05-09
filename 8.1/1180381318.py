def rMod(n,mod):
    return n%mod;
	
n=input();
for i in range(n):
    n2,n3=input();
    R=1;
    A=n3;
    E=n2-1;
    while (E!=0):
        if (E%2==1):
            print R,A,E,"S"
            R=rMod(R*A,n2);
            E=(E-1)/2;
            A=rMod(A*A,n2);
        else:
            print R,A,E,"N"
            E/=2;
            A=rMod(A*A,n2)
    print R,A,E,"N";
    if (R==1):
		print "INCONCLUSIVO";
    else:
		print "COMPOSTO";
    print "---";
	