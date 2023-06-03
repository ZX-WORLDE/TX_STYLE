#!/bin/bash
#!/bin/bash
import os
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

# Loading Animation Frames
frames=(
    "\e[0;37m[      \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m     \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m    \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m   \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m  \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m \e[0;37m]"
    "\e[0;37m[\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;32m=\e[0;31m\e[0;37m]"
)

# Function to display loading animation
function show_loading_animation() {
    local animation_frames=("$@")
    local num_frames=${#animation_frames[@]}
    local delay=0.1

    for ((i = 0; i < num_frames; i++)); do
        printf "\r${animation_frames[i]}"
        sleep $delay
    done
}

install_dependencies() {
    echo -e "${green}Installing dependencies ...${nocol}"

    # Start the loading animation
    show_loading_animation "${frames[@]}" &

    # Install dependencies
    apt update && apt install -y git zsh figlet toilet lf wget micro man

    # Stop the loading animation
    kill $!
    wait $! 2>/dev/null

    echo -e "${green}Dependencies installed!${nocol}"
}

install_ohmyzsh() {
    echo -e "${green}Installing Oh-My-Zsh ...${nocol}"

    # Start the loading animation
    show_loading_animation "${frames[@]}" &

    # Install Oh-My-Zsh and plugins
    git clone https://github.com/ohmyzsh/ohmyzsh.git "${HOME}"/.oh-my-zsh
    show_loading_animation "${frames[@]}" &
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/themes/powerlevel10k
    kill $!
    wait $! 2>/dev/null
    show_loading_animation "${frames[@]}" &
    git clone https://github.com/zsh-users/zsh-autosuggestions.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/plugins/zsh-autosuggestions
    kill $!
    wait $! 2>/dev/null
    show_loading_animation "${frames[@]}" &
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "${ZSH_CUSTOM:-${HOME}/.oh-my-zsh/custom}"/plugins/zsh-syntax-highlighting
    # Stop the loading animation
    kill $!
    wait $! 2>/dev/null

    echo -e "${green}Oh-My-Zsh installed!${nocol}"
}

finish_install() {
    echo -e "${green}Configuring termux ...${nocol}"

    # Start the loading animation
    show_loading_animation "${frames[@]}" &

    # Perform configuration tasks
    # ...

    # Stop the loading animation
    

    echo -e "${green}Setup Completed!${nocol}"
    echo -e "${green}Please restart Termux!${nocol}"
    kill $!
    wait $! 2>/dev/null
}
show_loading_animation "${frames[@]}" &
install_dependencies
show_loading_animation "${frames[@]}" &
install_ohmyzsh
show_loading_animation "${frames[@]}" &
finish_install
clear
printf "%s\n" "$logoz"
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf "\033[1;97m[\033[1;92mTARMUX TERMINAL SHORTCUT\033[1;97m]\n"
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mD \033[1;35m= \033[1;31mEXIT\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mL \033[1;35m= \033[1;36mCLEAR\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mO \033[1;35m= \033[1;32mSUPER MENU\n'
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;37m\n"
show_loading_animation "${frames[@]}" &
sleep 1.3
clear
printf "%s\n" "$logoz"
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf "\033[1;97m[\033[1;92mTARMUX TERMINAL SHORTCUT\033[1;97m]\033[1;31m=\033[1;37m[\033[1;32mSET UP COMPLETE\033[1;37m]\n"
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mD \033[1;35m= \033[1;31mEXIT\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mL \033[1;35m= \033[1;36mCLEAR\n'
printf '\033[1;37mCTRL \033[1;33m+ \033[1;32mO \033[1;35m= \033[1;32mSUPER MENU\n'
printf "\033[1;30m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;36m\n"
printf 'PRESS \033[1;37m[CTRL \033[1;33m+ \033[1;32mD\033[1;37m] \033[1;35m=\033[1;36m AND PRESS AGAIN  \033[1;37m[CTRL \033[1;33m+ \033[1;32mD\033[1;37m] \033[1;35m✓\n'
printf ''
printf ''
exit 0
