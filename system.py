import os
import datetime

x = input("Choose the Language (Türkçe/English) ")

if(x == "Türkçe"):
	print("------------Sisteme Hoşgeldiniz------------")
	print(datetime.date.today())

	a = input("İsim giriniz: ")

	if(a == "furkan"):
		print("Sisteme giriş başarılı..")
	else:	
		print("Bu isimde bir kayıt yok")	

	if(a == "furkan"):
		c = input("Rutin uygulamalar başlatılsın mı? ")
		if(c == "evet"):
			os.system("google-chrome-stable")
			os.system("spotify")
			os.system("/home/furkan/Masaüstü/Telegram/Telegram")

		else:
			print("Sistem kapatılıyor...")

	else:
		print("Yanlış giriş, sistemi yeniden başlatın lütfen..")	

elif(x == "English"):
	print("------------Welcome to the System------------")
	print(datetime.date.today())

	a = input("Input name: ")

	if(a == "furkan"):
		print("Succesful to login system..")
	else:	
		print("No members by this name..")	

	if(a == "furkan"):
		c = input("Do routin applications start? ")
		if(c == "yes"):
			os.system("google-chrome-stable")
			os.system("spotify")
			os.system("/home/furkan/Masaüstü/Telegram/Telegram")

		else:
			print("The system is shutting down..")

	else:
		print("Wrong log, reboot the System please..")
