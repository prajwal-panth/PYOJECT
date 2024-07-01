# Essentials/decoration.py
class Decoration:
    @staticmethod
    def colors():
        return {
            'RWHITE' : '\x1b[1;37;41m',
            'Grey' : '\033[30m',
            'Red' : '\033[31m',
            'Green' : '\033[32m',
            'Yellow' : '\033[33m',
            'Blue' : '\033[34m',
            'Pink' : '\033[35m',
            'Cyan' : '\033[36m',
            'White' : '\033[37m',
            'LGrey' : '\033[90m',
            'LRed' : '\033[91m',
            'LGreen' : '\033[92m',
            'LYellow' : '\033[93m',
            'LBlue' : '\033[94m',
            'LPink' : '\033[95m',
            'LCyan' : '\033[96m',
            'LWhite' : '\033[97m',
            'Reset' : '\033[00m'
        }

    @staticmethod    
    def nepalPIN_ascii():
        colors = Decoration.colors()
        print(f"{colors['Green']}+----------------------------------------------------------------------------------------------+{colors['Reset']}")
        print(f"{colors['Green']}|#     #                            ###            ######                                      |{colors['Reset']}")
        print(f"{colors['Green']}|##    # ###### #####    ##   #     ###   ####     #     # # #    #  ####   ####  #####  ######|{colors['Reset']}")
        print(f"{colors['Green']}|# #   # #      #    #  #  #  #      #   #         #     # # ##   # #    # #    # #    # #     |{colors['Reset']}")
        print(f"{colors['Green']}|#  #  # #####  #    # #    # #     #     ####     ######  # # #  # #      #    # #    # ##### |{colors['Reset']}")
        print(f"{colors['Green']}|#   # # #      #####  ###### #               #    #       # #  # # #      #    # #    # #     |{colors['Reset']}")
        print(f"{colors['Green']}|#    ## #      #      #    # #          #    #    #       # #   ## #    # #    # #    # #     |{colors['Reset']}")
        print(f"{colors['Green']}|#     # ###### #      #    # ######      ####     #       # #    #  ####   ####  #####  ######|{colors['Reset']}")
        print(f"{colors['Green']}+----------------------------------------------------------------------------------------------+{colors['Reset']}")
    
    @staticmethod  
    def bot_ascii():
        colors = Decoration.colors()
        print(f"{colors['Green']}+-----------------------------------------------------------------------------------+{colors['Reset']}")
        print(f"{colors['Green']}|     ______              _       _          _____ _           _   _                |{colors['Reset']}")
        print(f"{colors['Green']}|    / _____)            (_)     (_)        / ____| |         | | | |               |{colors['Reset']}")
        print(f"{colors['Green']}|   | /  ___  ____ ____   _ ____  _        | |    | |__  _____| |_| |_ ___ _ __     |{colors['Reset']}")
        print(f"{colors['Green']}|   | | (___)/ _  )    \\ | |  _ \\| |       | |    |  _ \\(____ |  _)  _) _ \\ '__|    |{colors['Reset']}")
        print(f"{colors['Green']}|   | \\____/( (/ /| | | || | | | | |       | |____| | ||/ ___ | |_| || |__/ |       |{colors['Reset']}")
        print(f"{colors['Green']}|    \\_____/ \\____)_|_|_||_|_| |_|_|        \\_____| | |||_____|\\__)___)____)_|      |{colors['Reset']}")
        print(f"{colors['Green']}|                                                                                   |{colors['Reset']}")
        print(f"{colors['Green']}+-----------------------------------------------------------------------------------+{colors['Reset']}")

    @staticmethod
    def pyoject_ascii():
        colors = Decoration.colors()
        print(f"{colors['Green']}  _______     ______       _ ______ _____ _______  {colors['Reset']}")
        print(f"{colors['Green']} |  __ \\ \\   / / __ \\     | |  ____/ ____|__   __| {colors['Reset']}")
        print(f"{colors['Green']} | |__) \\ \\_/ / |  | |    | | |__ | |       | |    {colors['Reset']}")
        print(f"{colors['Green']} |  ___/ \\   /| |  | |_   | |  __|| |       | |    {colors['Reset']}")
        print(f"{colors['Green']} | |      | | | |__| | |__| | |___| |____   | |    {colors['Reset']}")
        print(f"{colors['Green']} |_|      |_|  \\____/ \\____/|______\\_____|  |_|    {colors['Reset']}") 


class RPS_ascii:
    colors = Decoration.colors()
    def Game():
        print("    _______          ______             ________        ")
        print("---'   ____)     ---'    __)____    ---'    ____)_____    ")
        print("      (_____)             ______)_              ______)  ")
        print("      (_____)             ________)          __________) ")
        print("      (____)             _______)          (____)       ") 
        print("---.__(___)      ---._________)      ---.__(___)        ")
        print(f"{RPS_ascii.colors['Green']}    Rock               Paper             Scissors       {RPS_ascii.colors['Reset']}")
        print("")
        
    def Paper_LtoR():
        print("    _______         ")
        print("---'   ____)____    ")
        print("          ______)   ")
        print("          _______)  ")
        print("         _______)   ")
        print("---.__________)     ")
        print(f"{RPS_ascii.colors['Pink']}    Paper           {RPS_ascii.colors['Reset']}")
        print("")

    def Scissors_LtoR():
        print("    _______         ")
        print("---'   ____)____    ")
        print("          ______)   ")
        print("       __________)  ")
        print("      (____)        ")
        print("---.__(___)         ")
        print(f"{RPS_ascii.colors['Pink']}    Scissors        {RPS_ascii.colors['Reset']}")
        print("")
    def Rock_RtoL():
        print("  _______          ")
        print(" (____   '---      ")
        print("(_____)            ")
        print("(_____)            ")
        print(" (____)            ")
        print("  (___)__.---      ")
        print(f"{RPS_ascii.colors['Pink']}    Rock           {RPS_ascii.colors['Reset']}")
        print("")
        
    def Paper_RtoL():
        print("      _______      ")
        print("  ___(____   '---  ")
        print(" (______           ")
        print("(_______           ")
        print(" (_______          ")
        print("  (__________.---  ")
        print(f"{RPS_ascii.colors['Pink']}    Paper          {RPS_ascii.colors['Reset']}")
        print("")

    def Scissors_RtoL():
        print("      _______      ")
        print("  ___(____   '---  ")
        print(" (______           ")
        print("(__________        ")
        print("      (____)       ")
        print("      (___)__.---  ")
        print(f"{RPS_ascii.colors['Pink']}    Scissors       {RPS_ascii.colors['Reset']}")
        print("")

    def Rock_LtoR():
        print("    _______         ")
        print("---'   ____)        ")
        print("      (_____)       ")
        print("      (_____)       ")
        print("      (____)        ")
        print("---.__(___)         ")
        print(f"{RPS_ascii.colors['Pink']}    Rock            {RPS_ascii.colors['Reset']}")
        print("")

