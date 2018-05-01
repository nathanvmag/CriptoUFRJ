def rMod(n,mod):
    return n%mod;
	
n=input();
for i in range(n):
    n1,n2,n3=input();
    print rMod(n1,n3),rMod(n2,n3),rMod(n1+n2,n3),rMod(n1-n2,n3),rMod(n1*n2,n3);
    print "---";