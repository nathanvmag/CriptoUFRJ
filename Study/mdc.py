num1,num2 = input();
if(num1>num2):
	temp=num2
	num1=num2
	num2=num1
n1=num1
n2=num2
rest=num1%num2;
if (num1%num2==0):	
	print "MDC e",num2,"O MMC e ",num1;
else:
	while(num1%num2!=0):
		rest=num1%num2;
		num1=num2;
		num2=rest;
	print "MDC e",rest," MMC e",n1*n2/rest,




