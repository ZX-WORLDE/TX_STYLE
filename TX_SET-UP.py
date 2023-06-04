#THIS TOOL IS SECURE. ALL SCRIPT IS OPEN...
import os
import sys
import time
import subprocess
logo = """\033[1;37m
  ______
 /_  __/__ ______ _  __ ____ __
  / / / -_) __/  ' \/ // /\ \ /
 /_/  \__/_/ /_/_/_/\_,_//_\_\" """
logos = """\033[1;31m
⠀⠀         ⠀⠀⠀⠀⠀⣀⣤⣶⣿⠷⠾⠛⠛⠛⠛⠷⠶⢶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀         ⠀⠀⣀⣴⡾⠛⠉⠁⠀⣰⡶⠶⠶⠶⠶⠶⣶⡄⠀⠉⠛⠿⣷⣄⡀⠀⠀⠀
⠀         ⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠈⠛⢿⣦⡀⠀
         ⢠⣼⠟⠁⠀⠀⠀⠀⣠⣴⣶⣿⡇⠀⠀⠀⠀⠀⣿⣷⣦⣄⠀⠀⠀⠀⠀⠙⣧⡀
         ⣿⡇⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢈⣷
         ⣿⣿⣦⡀⣠⣾⣿⣿⣿⡿⠟⢻⣿⠀⠀⠀⠀⢠⣿⠻⢿⣿⣿⣿⣿⣆⣀⣠⣾⣿
         ⠉⠻⣿⣿⣿⣿⣽⡿⠋⠀⠀⠸⣿⠀⠀⠀⠀⢸⡿⠀⠀⠉⠻⣿⣿⣿⣿⣿⠟⠁
⠀         ⠀⠈⠙⠛⣿⣿⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⣹⣿⡟⠋⠁⠀⠀
⠀         ⠀⠀⠀⠀⢿⣿⣷⣄⣀⣴⣿⣿⣤⣤⣤⣤⣼⣿⣷⣀⣀⣾⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀         ⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀
⠀⠀⠀         ⠀⠀⠀⠀⠀⠉⠉⠁⣿⡇⠀⠀⠀⠀⢸⣿⡏⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀         ⠀⠀⠀⠀⠀⠀⠀⣿⣷⣄⠀⠀⣀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def jaln(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

def TX_SL():
    os.system("rm -rf README.md")
    os.system("clear")
    print(logo)
    print("")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;91m")
    print("\033[1;91m[\033[1;97m1\033[1;91m]\033[1;96m TMX_STYLE:\033[1;92m                           SET UP")
    print("\033[1;91m[\033[1;97m2\033[1;91m]\033[1;94m TXT\033[1;97m-\033[1;93mFONTs:\033[1;97m                           CHANGE")
    print("\033[1;91m[\033[1;97m3\033[1;91m]\033[1;95m TXT\033[1;97m-\033[38;5;208mC\033[1;92mO\033[1;91mL\033[1;93mO\033[1;95mU\033[1;96mR\033[1;37m                           CHANGE")
    print("\033[1;91m[\033[1;97m4\033[1;91m]\033[1;37m -\033[1;97m[\033[1;91mREMOVE\033[1;97m]-\033[1;90m                           SET UP")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
    zx = input("\033[1;91m[\033[1;97m?\033[1;91m]\033[38;5;208m Choose:\033[1;32m ")
    if zx in ["1", "01"]:
        os.system("clear")
        jalan("       \033[1;96m  [\033[1;92mSET UP YOUR SYSTEM \033[1;91mDON'T \033[1;92mSKIP\033[1;96m]")
        print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        os.system("cd tarmux && bash setup.sh")
        os.system("clear")
    elif zx in ["2", "02"]:
        os.system("clear")
        os.system("cd tarmux && cd Termux && bash fonts.sh")
    elif zx in ["3", "03"]:
        os.system("clear")
        os.system("cd tarmux && cd Termux && bash colors.sh")
    elif zx in ["4", "04"]:
        os.system("clear")
        jalan("\033[1;32mCLEAR DATA YOUR\033[1;31m tarmux \033[1;32mAPP TO REMOVE THIS STYLE")
        time.sleep(3)
        TX_SL()
    else:
        time.sleep(1)
        os.system("cd tarmux && bash setup.sh")


def zx():
    if not os.path.exists("sarv.txt"):
        os.system("clear")
        print(logo)
        jalan("\033[1;97m[\033[1;92mPRESS \033[1;91mENTER \033[1;92mTO UPDATE TARMUX\033[1;97m]")
        os.system("clear")
        print(logo)
        input("\033[1;97m[\033[1;92mPRESS \033[1;91mENTER \033[1;92mTO UPDATE TARMUX\033[1;97m]")
        os.system("clear")
        print(logo)
        print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
        os.system("clear")
        try:
            subprocess.check_output(['ping', '-c', '1', 'www.google.com'])
            internet_connection = True
        except subprocess.CalledProcessError:
            internet_connection = False

        if internet_connection:
            jalan("       \033[1;96m  [\033[1;92mSET UP YOUR SYSTEM \033[1;91mDON'T \033[1;92mSKIP\033[1;96m]")
            print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━033[1;32m")
            os.system("cd tarmux && bash setup.sh")
            with open("sarv.txt", "w") as file:
                file.write("FILE")
            TX_SL()
        else:
            os.system("clear")
            print(logos)
            print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m")
            jalan("\033[1;91m[!] FILE DOWNLOAD FAILED!\n\033[1;91m[!] NO INTERNET CONNECTION..")
            print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;91m")
            time.sleep(2)
            os.system("clear")
            print(logos)
            print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;91m")
            print("\033[1;91m[\033[1;97m1\033[1;91m]\033[1;92m FIX\033[1;92m INTERNET \033[1;91mERROR \033[1;92mPROBLEM")
            print("\033[1;91m[\033[1;97m2\033[1;91m]\033[1;96m CONTROL MENU")
            print("\033[1;91m[\033[1;97m3\033[1;91m]\033[1;91m EXIT")
            print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m")
            zx = input("\033[1;91m[\033[1;97m?\033[1;91m]\033[38;5;208m Choose:\033[1;32m ")
            if zx in ["1", "01"]:
                os.system("clear")
                jalan("       \033[1;96m  [\033[1;92mSET UP YOUR SYSTEM \033[1;91mDON'T \033[1;92mSKIP\033[1;96m]")
                print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━033[1;32m")
                os.system("cd tarmux && bash setup.sh")
            elif zx in ["2", "02"]:
                time.sleep(1)
                TX_SL()
            elif zx in ["3", "03"]:
                os.system("clear")
                jalan("\033[1;96mON YOUR INTERNET CONNECTION")
                exit()
        TX_SL()

zx()
