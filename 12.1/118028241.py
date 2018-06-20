def rMod(n,mod):
    return n%mod;

control =input();
for c in range(control):
	num =input();
	snum= num;
	num= num-1;
	i=2;
	error=0;
	fatores=[];
	limit=int(num**(0.5));
	eleva=0;
	feleva=[];
	while(limit>=i):
		if(num%i==0):		
			eleva+=1;
			num=num/i;
			limit=int(num**(0.5));		
			if(i>limit and eleva==1 and i!=num):
				fatores.append(i);
				feleva.append(i**eleva);
				print i,eleva;
				eleva=0;
		elif(eleva>0):
			fatores.append(i);
			print i,eleva;
			feleva.append(i**eleva);
			eleva=0;
			i+=1;
		else:
			i+=1;
			eleva=0;	
	eleva+=1;	
	print num,eleva;
	fatores.append(num);	
	feleva.append(num**eleva);
	g=1;
	for z in range(len (fatores)):
		a=2;
		while(rMod(a**((snum-1)/fatores[z]),snum)==1):
			a=a+1;
		h= rMod(a**((snum-1)/feleva[z]),snum);
		g=rMod(g*h,snum);
		print fatores[z],a,h;
	print g;
	print"---";

	
