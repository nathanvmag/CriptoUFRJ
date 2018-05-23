def rMod(n,mod):
    return n%mod;
    
def aee(a,b):
    x=[];
    y=[];
    x.append(1);
    x.append(0);
    y.append(0);
    y.append(1);
  
    while(b!=0):
        if (a%b==0):
            mdc=b;
            alpha=x[len(x)-1];
            beta=y[len(y)-1];
        temp=a%b;
        q=a//b;
        a=b;
        b=temp;
        xl=x[len(x)-2]-x[len(x)-1]*q;
        yl=y[len(y)-2]-y[len(y)-1]*q;
        x.append(xl);
        y.append(yl);        
    return [mdc,alpha];
    

n=input()
for i in range (n):
    u,Su=input();
    un=[];
    error=0;
    for i in range (u):
        if (i>0 and aee(i,u)[0]==1):
            un.append(i);
    if (1 in Su):
        for z in range (len(Su)):        
            if(Su[z] not in un):
                error+=1;
                break;          
            for x in range (len(Su)):
                if(rMod(Su[z]*Su[x],u) not in Su):
                    error+=1;
                    break;   

            if(rMod(aee(Su[z],u)[1],u) not in Su):
                error+=1;     
                break;       
    else : 
        error+=1;
        
    if(error !=0):
        print "NAO";
        print "---";        
    else :
        print"SIM";
        print"---";


    
    