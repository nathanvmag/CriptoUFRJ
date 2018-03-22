def divid (n1,n2):
	Q=0
	R=n1
	if (n1<=n2 or n1<0 or n2<0 ):
		return "sem resposta"
	while (n2<=R):
		Q+=1
		R-=n2
	return "o quociente e "+str(Q)+" o Resto e "+str(R)
a,b = input()
c = divid(a,b)

print c

