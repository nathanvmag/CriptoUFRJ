count = input();
for i in range(count):
	num = input();
	x=int(num**(0.5));
	y=0;
	while(num!= x*x-y*y):
		print x,y,"N";
		x+=1;
		y=int((x*x-num)**0.5);
		
	print x,y,"S"
	x1= x-y;
	x2=x+y;
	print x1,x2;
	print "---";