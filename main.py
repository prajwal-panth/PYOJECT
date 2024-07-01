import argparse
import os
import sys
from version import __version__, __author__, __description__
from Projects.decoration import Decoration
from Projects.ChatBot import main as chatbot_main
from Projects.NepalPinCode import main as nepalpin_main
from Projects.RPSgame import main as rpsgame_main
from Projects.CalcC2Py import main as calculator_main
from Projects.CDTimerJava2Py import main as gui_cd_timer_main
from Projects.HotelMS import main as hotel_ms_main
from Projects.UnitQB2Py import main as unit_converter_main

colors = Decoration.colors()

class SwitchCase:
    def switch(self, choice):
        attribute = "case_" + str(choice)
        method = getattr(self, attribute, self.default)
        method()

    def case_1(self):
        chatbot_main()

    def case_2(self):
        nepalpin_main()

    def case_3(self):
        rpsgame_main()

    def case_4(self):
        calculator_main()
    
    def case_5(self):
        gui_cd_timer_main()

    def case_6(self):
        hotel_ms_main()

    def case_7(self):
        unit_converter_main()

    def case_8(self):
        print(f"{colors['LCyan']}Exiting the program.{colors['Reset']}")
        sys.exit(0)

    def default(self):
        print(f"{colors['LCyan']}Invalid choice. Please enter a number between 1 and 8.{colors['Reset']}")

class MainProgram:
    def __init__(self):
        self.sc = SwitchCase()

    def menu(self):
        Decoration.pyoject_ascii()
        print(f"{colors['LGreen']}\nPyoject v{__version__}{colors['Reset']}")
        print(f"\n{colors['Pink']}Menu:{colors['Reset']}")
        print(f"{colors['Blue']}1. Chat Bot{colors['Reset']}")
        print(f"{colors['Blue']}2. Nepal Postal Code{colors['Reset']}")
        print(f"{colors['Blue']}3. Rock Paper Scissors{colors['Reset']}")
        print(f"{colors['Blue']}4. Calculator{colors['Reset']}")
        print(f"{colors['Blue']}5. GUI Countdown Timer{colors['Reset']}")
        print(f"{colors['Blue']}6. Hotel Management System{colors['Reset']}")
        print(f"{colors['Blue']}7. QBasic Unit Converter{colors['Reset']}")
        print(f"{colors['Red']}8. Exit{colors['Reset']}")

    def run(self):
        try:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                self.menu()
                user_choice = input(f"\n{colors['LCyan']}Enter Your Choice: {colors['Reset']}")
                self.sc.switch(user_choice)
                input(f"\n{colors['LCyan']}Press Enter to continue...{colors['Reset']}")
        except KeyboardInterrupt:
            print(f"\n{colors['Red']}Program interrupted by user{colors['Reset']}")
        except Exception as e:
            print(f"\n{colors['Red']}An unexpected error occurred: {str(e)}{colors['Reset']}")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="It is a collection of beginner-friendly programming projects across various languages.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {__version__}',
        help='Show the version of the program and exit.'
    )
    
    parser.add_argument(
        '-r', '--run',
        choices=['1', '2', '3', '4', '5', '6', '7'],
        help=("Run a specific program by selecting its corresponding number:\n"
            "  1. Chat Bot\n"
            "  2. Nepal Postal Code\n"
            "  3. Rock Paper Scissors\n"
            "  4. Calculator\n"
            "  5. GUI Countdown Timer\n"
            "  6. Hotel Management System\n"
            "  7. QBasic Unit Converter\n"
        )
    )
    
    parser.add_argument(
        '--author',
        action='version',
        version=f'Author: {__author__}',
        help='Show the author of the program and exit.'
    )
    
    parser.add_argument(
        '--description',
        action='version',
        version=f'Description: {__description__}',
        help='Show the description of the program and exit.'
    )
    
    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.run:
        SwitchCase().switch(args.run)
    else:
        program = MainProgram()
        program.run()

if __name__ == "__main__":
    print("__name__ == '__main__'")
    main()
