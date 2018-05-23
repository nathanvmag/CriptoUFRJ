def fat(num):
    fatores=[];
    elevas=[];
    i=2;
    limit=int(num**(0.5));
    eleva=0;
    while(limit>=i):
        if(num%i==0):        
            eleva+=1;
            
            num=num/i;
            limit=int(num**(0.5));        
            if(i>limit and eleva==1 and i!=num):
                print i,eleva;
                fatores.append(i);
                elevas.append(eleva);
                eleva=0;
        elif(eleva>0):
            print i,eleva;
            fatores.append(i);
            elevas.append(eleva);
            eleva=0;
            i+=1;
        else:
            i+=1;
            eleva=0;    
    eleva+=1;    
    print num, eleva;
    fatores.append(num)
    elevas.append(eleva);
    return fatores,elevas;
    
n=input()
for i in range (n):
    u=input();
    ft=fat(u);
    resu=1;
    for z in range (len(ft[0])):
        resu*=(ft[0][z]**(ft[1][z]-1))*(ft[0][z]-1);
        
    print resu            
    print "---";
