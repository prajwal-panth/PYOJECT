import os
os.system("cls" if os.name == "nt" else "clear")

class OldColors:
    BMAGENTA = '\x1b[1;37;46m'
    RWHITE = '\x1b[1;37;41m'
    BBLUE = '\x1b[1;36;40m'
    BGREEN = '\x1b[1;32;40m'
    BPINK = '\x1b[1;35;40m'
    BRED = '\x1b[1;31;40m'
    BYELLOW = '\x1b[1;33;40m'
    END = '\x1b[0m'

print(f"{OldColors.BMAGENTA}Hello{OldColors.END}")
print(f"{OldColors.RWHITE}Hello{OldColors.END}")
print(f"{OldColors.BGREEN}Hello{OldColors.END}")
print(f"{OldColors.BPINK}Hello{OldColors.END}")
print(f"{OldColors.BRED}Hello{OldColors.END}")
print(f"{OldColors.BYELLOW}Hello{OldColors.END}")


class Colors:
    RWHITE = '\x1b[1;37;41m'
    Grey = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Pink = '\033[35m'
    Cyan = '\033[36m'
    White = '\033[37m'
    BrightGrey = '\033[90m'
    BrightRed = '\033[91m'
    BrightGreen = '\033[92m'
    BrightYellow = '\033[93m'
    BrightBlue = '\033[94m'
    BrightPink = '\033[95m'
    BrightCyan = '\033[96m'
    BrightWhite = '\033[97m'
    Reset = '\033[00m'

print(f"{Colors.Grey}30m:Grey{Colors.Reset}")
print(f"{Colors.Red}31m:Red{Colors.Reset}")
print(f"{Colors.Green}32m:Green{Colors.Reset}")
print(f"{Colors.Yellow}33m:Yellow{Colors.Reset}")
print(f"{Colors.Blue}34m:Blue{Colors.Reset}")
print(f"{Colors.Pink}35m:Pink{Colors.Reset}")
print(f"{Colors.Cyan}36m:Cyan{Colors.Reset}")
print(f"{Colors.White}37m:White{Colors.Reset}")
print(f"{Colors.BrightGrey}90m:BrightGrey{Colors.Reset}")
print(f"{Colors.BrightRed}91m:BrightRed{Colors.Reset}")
print(f"{Colors.BrightGreen}92m:BrightGreen{Colors.Reset}")
print(f"{Colors.BrightYellow}93m:BrightYellow{Colors.Reset}")
print(f"{Colors.BrightBlue}94m:BrightBlue{Colors.Reset}")
print(f"{Colors.BrightPink}95m:BrightPink{Colors.Reset}")
print(f"{Colors.BrightCyan}96m:BrightCyan{Colors.Reset}")
print(f"{Colors.BrightWhite}97m:BrightWhite{Colors.Reset}")
print(f"{Colors.Reset}0m:Reset{Colors.Reset}")

def color_box():
    D_GRAY = "\033[48;5;232m"
    D_RED = "\033[48;5;52m"
    D_GREEN = "\033[48;5;22m"
    D_ORANGE = "\033[48;5;130m"
    D_BLUE = "\033[48;5;19m"
    D_MAGENTA = "\033[48;5;53m"
    D_CYAN = "\033[48;5;25m"
    D_WHITE = "\033[48;5;255m"
    GRAY = "\033[48;5;240m"
    RED = "\033[48;5;196m"
    GREEN = "\033[48;5;46m"
    ORANGE = "\033[48;5;214m"
    BLUE = "\033[48;5;21m"
    MAGENTA = "\033[48;5;201m"
    CYAN = "\033[48;5;51m"
    WHITE = "\033[48;5;231m"
    RESET = "\033[0;0;0m"  # \033[0m and \033[0;0;0m are the same

    print(f"{D_GRAY}    {D_RED}    {D_GREEN}    {D_ORANGE}    {D_BLUE}    {D_MAGENTA}    {D_CYAN}    {D_WHITE}    {RESET}")
    print(f"{GRAY}    {RED}    {GREEN}    {ORANGE}    {BLUE}    {MAGENTA}    {CYAN}    {WHITE}    {RESET}")
color_box()
