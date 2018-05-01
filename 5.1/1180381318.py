def printcriv(criv):
    temp=[]
    for z in range(len(criv)):
        if(criv[z]!=0):
            temp.append(criv[z])
    print temp

n =input()
crivo=[]
crivo2=[]
i=3
while (i<n+1):
    crivo.append(i);
    crivo2.append(i);
    i+=2
limit= int(n**0.5)
print crivo 
print limit
j=0
while(crivo[j]<=limit):
    if(crivo[j] in crivo2):
        print crivo[j],crivo[j]**2,crivo.index(crivo[j]**2)
        cortes=[]
        x=0
        while (crivo[j]**2+crivo[j]*x<n):
            if (crivo[j]**2+crivo[j]*x in crivo):
                cortes.append(crivo[j]**2+crivo[j]*x)
                if(crivo[j]**2+crivo[j]*x in crivo2):
                    crivo2[crivo2.index(crivo[j]**2+crivo[j]*x)]=0
            
            x+=1;
        print cortes
        printcriv(crivo2)
    j+=1
crivo2 =[2]+crivo2;
printcriv(crivo2)