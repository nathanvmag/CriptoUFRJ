n=input()
nuns=[]
aa=[]
maxdiv=0
for i in range(1,1+n):
    nuns.append(i)

for i in range(len(nuns)):
    div=0
    q=nuns[i]
    while(q>0):
        if(nuns[i]%q==0):
            div+=1
        q-=1
    if(div>maxdiv):
        maxdiv=div;
        aa.append(nuns[i])
        
print aa