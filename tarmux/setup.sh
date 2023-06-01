#!/bin/bash

# Color Codes
red="\e[0;31m"             # Red
green="\e[0;32m"           # Green
nocol="\033[0m"            # Default

# Loading Animation Frames
frames=(
    "\x1b[1;97m[      \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m     \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m    \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m   \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m  \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m \x1b[1;97m]"
    "\x1b[1;97m[\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;92m=\x1b[1;91m\x1b[1;97m]"
)

# Function to display loading animation
function show_loading_animation() {
    local animation_frames=("$@")
    local num_frames=${#animation_frames[@]}
    local delay=0.1

    while true; do
        for ((i = 0; i < num_frames; i++)); do
            printf "\r${animation_frames[i]}"
            sleep $delay
        done
    done
}

install_dependencies() {
    echo -e "${green}Installing dependencies ...${nocol}"
    show_loading_animation "${frames[@]}" &
    local loading_animation_pid=$!

    apt update && apt install -y git zsh figlet toilet lf wget micro man

    # Stop the loading animation
    kill $loading_animation_pid
    printf "\r${green}Dependencies installed!${nocol}\n"
}

install_ohmyzsh() {
    echo -e "${green}Installing Oh-My-Zsh ...${nocol}"
    show_loading_animation "${frames[@]}" &
    local loading_animation_pid=$!

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

    # Stop the loading animation
    kill $loading_animation_pid
    printf "\r${green}Oh-My-Zsh installed!${nocol}\n"
}

finish_install() {
    echo -e "${green}Configuring termux ...${nocol}"
    show_loading_animation "${frames[@]}" &
    local loading_animation_pid=$!

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

    # Stop the loading animation
    kill $loading_animation_pid
    printf "\r${green}Setup Completed!${nocol}\n"
}

install_dependencies
install_ohmyzsh
finish_install
exit 0
