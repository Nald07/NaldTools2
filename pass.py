import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32matau silahkan Hubungi 082277001533 ")


print ("\033[1;32mScript Ini sekarang tidak gratis ")

username = 'Medan'      

password = 'Keras'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print" \033[1;32mAlhmdllh sudah masuk juga... Silakan Login Kembali"

			sys.exit()



		else:

			print "\033[1;31mSALAH KIMAKKK-_-... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;31mSALAH KIMAKKK-_-... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
