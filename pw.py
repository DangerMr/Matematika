import os, sys

os.system("cowsay  -f ren 'Masukin Pasword Sama Username Dulu Yah' | lolcat")
print ("\033[1;32mMasukan UserName & Password:)")
print ("\033[1;31;1mjika tidak tau hubungi Sadboys 6288703041772")
username ='Sadboys'     
password = 'Gans'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome To Tools SadBoys", 
			sys.exit()

		else:
			print "\n\033[1;36mmaaf kata sandi anda salah\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mmaaf kata sandi anda salah\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()