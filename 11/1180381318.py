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
        
    return mdc;
    

n=input()
for i in range (n):
    u=input();
    un=[];
    for i in range (u):
        if (i>0 and aee(i,u)==1):
            un.append(i);
    print un;
    for x in range(len(un)) :
        sub=[];
        if(un[x]==1):
            sub.append(1);
            print sub;
        else :
            sub.append(1);
            num=1;
            tmp=un[x];
            while(tmp!=1):
                sub.append(tmp);
                num+=1;
                tmp=rMod(un[x]**num,u);
            sub.sort(key=int);
            print sub;
    print "---";


