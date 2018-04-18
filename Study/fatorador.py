def Fatorar():
	num = input();
	i =2;
	fatores=[];
	rest=num;
	print "comeca com " , int(rest**0.5);
	while (int(rest** (0.5))>i):
		if (rest%i==0):		
			print rest,i;
			fatores.append(i);
			rest= rest/i;				
			print "vai ate ", int(rest**0.5);
		else :
			i+=1;
		if (int(rest**0.5)<i):
			fatores.append(rest);
			break;
	print fatores;	

Fatorar();

