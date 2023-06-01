#THIS TOOL IS SECURE. ALL SCRIPT IS OPEN...
import os

try:
	os.system("rm -rf README.md")
	
logo = ("""
  \033[1;91m   _____ __  _____    ____  __  _______   __
  \033[1;91m  / ___// / / /   |  / __ \/ / / /  _/ | / /
  \033[38;5;208m  \__ \/ /_/ / /| | / / / / /_/ // //  |/ / 
  \033[38;5;208m ___/ / __  / ___ |/ /_/ / __  // // /|  /  
  \033[1;95m/____/_/ /_/_/  |_/_____/_/ /_/___/_/ |_/ 
\033[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def TX-SL():
	os.system("clear")
	print(logo)
	print("\033[1;32m [1] \033[1;32m[SYSTEM]-[UPDATE TARMUX]")
	print("\033[1;32m [2] \033[1;32m[TEXT-FONT]-[UPDATE TARMUX]")
	print("\033[1;32m [3] \033[1;32m[BACKGROUND-COLOUR]-[UPDATE TARMUX]")
	print("\033[1;32m [4] \033[1;32m[REMOVE]-[UPDATE TARMUX]")
	print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	zx =input(" [?] Choose :\033[1;32m \033[1;37m")
	if zx in ["1", "01"]:
		os.system("cd tarmux && bash setup.sh")
	if zx in ["2","02"]:
		os.system("cd tarmux && cd Termux && bash fonts.sh")
	if zx in ["3","03"]:
		os.system("cd tarmux && cd Termux && bash colors.sh")
	if zx in ["4","04"]:
		jalan("\033[1;32mclear data your tarmux app")
		time.sleep(5)
	else:
		time.sleep(1)
		os.system("cd tarmux && bash setup.sh")

def zx():
	if not os.path.exists("sar.txt"):
		jalan("\033[1;32myou sure internet connection is on")
		os.system("clear")
		print(logo)
		input("[PRESS ENTER TO UPDATE TARMUX]")
		os.system("clear")
		jalan("       \033[1;96m  [SET UP YOUR SYSTEM DON'T SKIP]")
		print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		os.system("cd tarmux && bash setup.sh")
		with open("sar.txt", "w") as file:
			file.write("FILE")
			TX-SL()
	TX-SL()
zx()