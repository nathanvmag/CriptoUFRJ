control =input();
for c in range(control):
	num =input();
	i=2;
	fatores=[];
	limit=int(num**(0.5));
	eleva=0;
	while(limit>=i):
		if(num%i==0):		
			eleva+=1;
			num=num/i;
			limit=int(num**(0.5));		
			if(i>limit and eleva==1 and i!=num):
				print i,eleva;
				eleva=0;
		elif(eleva>0):
			print i,eleva;
			eleva=0;
			i+=1;
		else:
			i+=1;
			eleva=0;	
	eleva+=1;	
	print num, eleva;
	print "---";

