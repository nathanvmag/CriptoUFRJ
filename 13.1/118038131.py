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
				feleva.append(i*eleva);
				print i,eleva;
				eleva=0;
		elif(eleva>0):
			fatores.append(i);
			print i,eleva;
			feleva.append(i*eleva);
			eleva=0;
			i+=1;
		else:
			i+=1;
			eleva=0;	
	eleva+=1;	
	print num,eleva;
	fatores.append(num);	
	feleva.append(i*eleva);
	testes=[]+fatores;
	base =2;
	for i in range (snum-2):
		if (len(testes)>0):
			print base;
			exp = snum-1;
			print exp;
			if (rMod(potmod(base,exp,snum),snum)==1):
				for z in range (len(fatores)):
					if (fatores[z]in testes):
						nexp= (snum-1)/fatores[z];
						print nexp;
						if (rMod(potmod(base,nexp,snum),snum)!=1):
							if (fatores[z] in testes):
								testes.remove(fatores[z]);
							if (len (testes)==0):
								print "PRIMO"
								print"---";
								break;		
			else :
				print "COMPOSTO";
				print "---";
				break;
			base+=1;
