n=input();
for i in range(n):
    a,b=input()    
    x=[];
    y=[];
    x.append(1);
    x.append(0);
    y.append(0);
    y.append(1);
    print a,"-",1,0;
    print b,"-",0,1;
    while(b!=0):
        temp=a%b;
        q=a//b;
        a=b
        b=temp;
        xl=x[len(x)-2]-x[len(x)-1]*q;
        yl=y[len(y)-2]-y[len(y)-1]*q;
        x.append(xl);
        y.append(yl);
        if(b==0):
            print temp,q,"-","-";
        else:
            print temp,q,x[len(x)-1],y[len(y)-1];
    print "---";



        

