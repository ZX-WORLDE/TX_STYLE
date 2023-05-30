Here's the translation of the provided Bash script to Python:

```python

import os

import subprocess

red = "\033[0;31m"

green = "\033[0;32m"

nocol = "\033[0m"

def install_dependencies():

    print(f"{green}Installing dependencies ...{nocol}")

    subprocess.run(["apt", "update"])

    subprocess.run(["apt", "install", "-y", "git", "zsh", "figlet", "toilet", "lf", "wget", "micro", "man"])

def install_ohmyzsh():

    print(f"{green}Installing Oh-My-Zsh ...{nocol}")

    subprocess.run(["git", "clone", "https://github.com/ohmyzsh/ohmyzsh.git", os.path.expanduser("~/.oh-my-zsh")])

    print(f"{green}Installing powerlevel10k theme ...{nocol}")

    subprocess.run(["git", "clone", "--depth=1", "https://github.com/romkatv/powerlevel10k.git", os.path.expanduser("~/.oh-my-zsh/custom/themes/powerlevel10k")])

    print(f"{green}Installing custom plugins ...{nocol}")

    subprocess.run(["git", "clone", "https://github.com/zsh-users/zsh-autosuggestions.git", os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")])

    subprocess.run(["git", "clone", "https://github.com/zsh-users/zsh-syntax-highlighting.git", os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")])

    print(f"{green}Configuring Oh-My-Zsh ...{nocol}")

    subprocess.run(["cp", "-f", "OhMyZsh/zshrc", os.path.expanduser("~/.zshrc")])

    if os.uname().machine.startswith("arm"):

        print(f"Armv7 device detected{red}!{nocol} Gitstatus disabled{red}!{nocol}")

        # There's no binaries of gitstatus for armv7 right now so disable it

        with open(os.path.expanduser("~/.zshrc"), "a") as f:

            f.write("\n# Disable gitstatus for now (Only for armv7 devices)\nPOWERLEVEL9K_DISABLE_GITSTATUS=true\n")

    os.chmod(os.path.expanduser("~/.zshrc"), 0o777)

    if os.path.isfile("OhMyZsh/zsh_history"):

        print(f"{green}Installing zsh history file ...{nocol}")

        subprocess.run(["cp", "-f", "OhMyZsh/zsh_history", os.path.expanduser("~/.zsh_history")])

        os.chmod(os.path.expanduser("~/.zsh_history"), 0o666)

    if os.path.isfile("OhMyZsh/custom_aliases.zsh"):

        print(f"{green}Installing custom aliases ...{nocol}")

        subprocess.run(["cp", "-f", "OhMyZsh/custom_aliases.zsh", os.path.expanduser("~/.oh-my-zsh/custom/custom_aliases.zsh")])

    print(f"{green}Configuring powerlevel10k theme ...{nocol}")

    subprocess.run(["cp", "-f", "OhMyZsh/p10k.zsh", os.path.expanduser("~/.p10k.zsh")])

    print(f"{green}Oh-My-Zsh installed!{nocol}")

def finish_install():

    print(f"{green}Configuring termux ...{nocol}")

    # Remove already existing .termux folder

    subprocess.run(["rm", "-rf", os.path

.expanduser("~/.termux")])

    subprocess.run(["cp", "-r", "Termux", os.path.expanduser("~/.termux")])

    os.chmod(os.path.expanduser("~/.termux/fonts.sh"), 0o777)

    os.chmod(os.path.expanduser("~/.termux/colors.sh"), 0o777)

    print(f"{green}Setting IrBlack as default color scheme ...{nocol}")

    os.symlink(os.path.expanduser("~/.termux/colors/dark/IrBlack"), os.path.expanduser("~/.termux/colors.properties"))

    # Replacing termux's boring welcome message with something good looking

    subprocess.run(["mv", "/data/data/com.termux/files/usr/etc/motd", "/data/data/com.termux/files/usr/etc/motd.bak"])

    subprocess.run(["mv", "/data/data/com.termux/files/usr/etc/motd.sh", "/data/data/com.termux/files/usr/etc/motd.sh.bak"])

    # Remove gitstatusd from cache if arm

    if os.uname().machine.startswith("arm"):

        subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/gitstatus")])

    print(f"{green}Setting zsh as default shell ...{nocol}")

    subprocess.run(["chsh", "-s", "zsh"])

    # Setup Complete

    subprocess.run(["termux-setup-storage"])

    subprocess.run(["termux-reload-settings"])

    print(f"{green}Setup Completed!{nocol}")

    print(f"{green}Please restart Termux!{nocol}")

# Start installation

install_dependencies()
install_ohmyzsh()
finish_install()
exit(0)


# Error msg for invalid choice

print(f"{red}Invalid choice!{nocol}")

print()

exit(1)

```

