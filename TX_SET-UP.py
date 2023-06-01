#THIS TOOL IS SECURE. ALL SCRIPT IS OPEN...
import os
import sys
import time

logo = """
  \033[1;91m   _____ __  _____    ____  __  _______   __
  \033[1;91m  / ___// / / /   |  / __ \/ / / /  _/ | / /
  \033[38;5;208m  \__ \/ /_/ / /| | / / / / /_/ // //  |/ / 
  \033[38;5;208m ___/ / __  / ___ |/ /_/ / __  // // /|  /  
  \033[1;95m/____/_/ /_/_/  |_/_____/_/ /_/___/_/ |_/ 
\033[1;96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\rProcessing " + animation[i % len(animation)])
        sys.stdout.flush()

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
    elif zx in ["2", "02"]:
        os.system("cd tarmux && cd Termux && bash fonts.sh")
    elif zx in ["3", "03"]:
        os.system("cd tarmux && cd Termux && bash colors.sh")
    elif zx in ["4", "04"]:
        os.system("clear")
        jalan("\033[1;32mCLEAR DATA YOUR\033[1;31m tarmux \033[1;32mAPP")
        time.sleep(3)
        TX_SL()
    else:
        time.sleep(1)
        os.system("cd tarmux && bash setup.sh")

def zx():
    if not os.path.exists("sar.txt"):
        jalan("\033[1;32myou make sure your internet connection is on")
        time.sleep(2)
        os.system("clear")
        print(logo)
        jalan("\033[1;97m[\033[1;92mPRESS \033[1;91mENTER \033[1;92mTO UPDATE TARMUX\033[1;97m]")
        os.system("clear")
        print(logo)
        input("\033[1;97m[\033[1;92mPRESS \033[1;91mENTER \033[1;92mTO UPDATE TARMUX\033[1;97m]")
        os.system("clear")
        jalan("       \033[1;96m  [\033[1;92mSET UP YOUR SYSTEM \033[1;91mDON'T \033[1;92mSKIP\033[1;96m]")
        print("\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        os.system("cd tarmux && bash setup.sh")
        with open("sar.txt", "w") as file:
            file.write("FILE")
        
        loading_animation()  # Display loading animation
        
        TX_SL()

    TX_SL()

zx()
