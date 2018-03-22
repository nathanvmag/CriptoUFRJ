
def Criptografar(tx,k):
	chars = list(tx);
	cripto="";
	for i in range(len(chars)):	
		chars[i]= chr(ord(chars[i])+k);
		cripto+=chars[i];

	return cripto;	
def Start():
	print "\nBem Vindo a Cifra de Cesar \nPara Criptografar um texto digite 1\nPara Descriptografar digite 2\n"
	control = raw_input();
	if (control =="1"):
		print "Digite o texto a ser criptografado:";
		a= raw_input();
		print "Digte o K para a chave da Criptografia:";
		k=input();
		crip = Criptografar(a,k);
		print "O texto criptografado e: \n"+ crip;
	elif (control =="2"):
		print "Digite o texto a ser Descriptografado:";
		a= raw_input();
		print "Digte o K para a chave da Decriptacao:";
		k=input();
		crip = Criptografar(a,-k);
		print "O texto decriptado e: \n"+ crip;
	else :
		print "Voce digitou um numero invalido tente novamente";
		Start();
Start();