def fat (n):
	if (n==1 ):
		return 1;
	elif(n==0):
		return 0;
	else :
		return n*fat(n-1);
num=input();
print fat(num);
