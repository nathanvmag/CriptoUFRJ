control =input();
for c in range(control):
	num =input();
	snum= num;
	i=2;
	error=0;
	fatores=[];
	limit=int(num**(0.5));
	eleva=0;
	while(limit>=i):
		if(num%i==0):		
			eleva+=1;
			num=num/i;
			limit=int(num**(0.5));		
			if(i>limit and eleva==1 and i!=num):
				fatores.append(i);
				print i,eleva;
				eleva=0;
		elif(eleva>0):
			fatores.append(i);
			print i,eleva;
			eleva=0;
			i+=1;
		else:
			i+=1;
			eleva=0;	
	eleva+=1;	
	print num,eleva;
	fatores.append(num);	
	if (len(fatores)==1):
		print "NAO";
	else :
		for n in range (len(fatores)):
			if (snum% (fatores[n]**2) ==0):
				error=error+1;		
				break;
			if( (snum-1)%((fatores[n]-1)  )!=0):
				error=error+1;
				break;
		if (error>0):
			print "NAO";
		else :
			print "SIM";
	print "---";
