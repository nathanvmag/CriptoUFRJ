def Fatorar(n):
	print "Digite um numero para fatorar :";
	num = input();
	i =2;
	rest=num;
	while (num>i):
		if (rest%i==0):		
			print rest,i;
			rest= rest/i;		
		else :
			i+=1;
		if (rest<i):
			break;
def Fatorar2(n,nlist):
	
	print "Fatorando :",n,"...";
	rest=n;
	i=0;
	while (n>i):
		if (rest%nlist[i]==0):		
			print rest,nlist[i];
			rest= rest/nlist[i];		
		else : 
			i+=1;	
		if (rest<nlist[i]):
			
			break;

print "Digite um numero para fatorar :"
num = input();
l = [];
primos=[];
for i in range (2,num+1):
	l.append(i);
	primos.append(i);


for i in range (len(l)):
	for x in range (len(l)):
		if (x!=1):
			if(l[i]*x in primos):			
				value = l[i]*x;
				primos.remove(value);
print primos;
#Fatorar2(num,primos);

