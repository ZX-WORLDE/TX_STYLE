#!/bin/bash
#
## Termux-Zsh
printf "033[1;37m[033[1;31m×033[1;37m] 033[1;32mPRESS 033[1;36mENTER 033[1;32mTO START"
sleep 3
logoz=$(cat << "EOF"
██ ███    ██ ███████  ██████ 
██ ████   ██ ██      ██    ██ 
██ ██ ██  ██ █████   ██    ██ 
██ ██  ██ ██ ██      ██    ██ 
██ ██   ████ ██       ██████
EOF
)
# Color Codes
red="\e[0;31m"             # Red
green="\e[0;32m"           # Green
nocol="\033[0m"            # Default
RED="\e[0;31m"
WHITE="\e[0;37m"
YELLOW="\e[0;33m"
RESET="\033[0m"
install_dependencies() {
    echo -e "${green}Installing dependencies ...${nocol}"
    apt update && apt install -y git zsh figlet toilet lf wget micro man
}

install_ohmyzsh() {
    echo -e "${green}Installing Oh-My-Zsh ...${nocol}"
    git clone https://github.com/ohmyzsh/ohmyzsh.git "${HOME}"/.oh-my-zsh
    echo -e "${green}Installing powerlevel10k theme ...${nocol}"
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/themes/powerlevel10k
    echo -e "${green}Installing custom plugins ...${nocol}"
    git clone https://github.com/zsh-users/zsh-autosuggestions.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/plugins/zsh-syntax-highlighting
    echo -e "${green}Configuring Oh-My-Zsh ...${nocol}"
    cp -f OhMyZsh/zshrc ~/.zshrc
    if [[ "$(dpkg --print-architecture)" == "arm" ]]; then
        echo -e "Armv7 device detected${red}!${nocol} Gitstatus disabled${red}!${nocol}"
        # There's no binaries of gitstatus for armv7 right now so disable it
        echo -e "\n# Disable gitstatus for now (Only for armv7 devices)\nPOWERLEVEL9K_DISABLE_GITSTATUS=true\n" >> ~/.zshrc
    fi
    chmod +rwx ~/.zshrc
    if [[ -f "OhMyZsh/zsh_history" ]]; then
        echo -e "${green}Installing zsh history file ...${nocol}"
        cp -f OhMyZsh/zsh_history ~/.zsh_history
        chmod +rw ~/.zsh_history
    fi
    if [[ -f "OhMyZsh/custom_aliases.zsh" ]]; then
        echo -e "${green}Installing custom aliases ...${nocol}"
        cp -f OhMyZsh/custom_aliases.zsh ~/.oh-my-zsh/custom/custom_aliases.zsh
    fi
    echo -e "${green}Configuring powerlevel10k theme ...${nocol}"
    cp -f OhMyZsh/p10k.zsh ~/.p10k.zsh
    echo -e "${green}Oh-My-Zsh installed!${nocol}"
}

finish_install() {
    echo -e "${green}Configuring termux ...${nocol}"
    # Remove already existing .termux folder
    rm -rf ~/.termux
    cp -r Termux ~/.termux
    chmod +x ~/.termux/fonts.sh ~/.termux/colors.sh
    echo -e "${green}Setting IrBlack as default color scheme ...${nocol}"
    ln -fs ~/.termux/colors/dark/IrBlack ~/.termux/colors.properties
    # Replacing termuxs boring welcome message with something good looking
    mv "${PREFIX}"/etc/motd "${PREFIX}"/etc/motd.bak
    mv "${PREFIX}"/etc/motd.sh "${PREFIX}"/etc/motd.sh.bak
    # Remove gitstatusd from cache if arm
    if [[ "$(dpkg --print-architecture)" == "arm" ]]; then
        rm -rf ~/.cache/gitstatus
    fi
    echo -e "${green}Setting zsh as default shell ...${nocol}"
    chsh -s zsh
    # Setup Complete
    termux-setup-storage
    termux-reload-settings
    echo -e "${green}Setup Completed!${nocol}"
    echo -e "${green}Please restart Termux!${nocol}"
}

install_dependencies
install_ohmyzsh
finish_install
clear
printf "%s\n" "$logoz"
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mD \033[1;35m= \033[1;31mEXIT\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mL \033[1;35m= \033[1;36mCLEAR\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mO \033[1;35m= \033[1;32mSUPER MENU\n'
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf 'PRESS \033[1;37m[CTRL \033[1;33m+ \033[1;32mD\033[1;37m] \033[1;35m=\033[1;36m AND PRESS AGAIN  \033[1;37m[CTRL \033[1;33m+ \033[1;32mD\033[1;37m] \033[1;35m✓\n'
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m"
printf '\033[1;37m'
read -p "[×] ENTER TO MENU"
printf ''
exit 0
