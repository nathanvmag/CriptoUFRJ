def rMod(n,mod):
    return n%mod;
	
n=input();
for i in range(n):
    n1,n2,n3=input();
    R=1;
    A=n1;
    E=n2;
    while (E!=0):
        if (E%2==1):
            print R,A,E,"S"
            R=rMod(R*A,n3);
            E=(E-1)/2;
            A=rMod(A*A,n3);
        else:
            print R,A,E,"N"
            E/=2;
            A=rMod(A*A,n3)
    print R,A,E,"N";
    print "---";
	