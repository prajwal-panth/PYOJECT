import random
import os
try:
    from .decoration import Decoration, RPS_ascii
except ImportError:
    from decoration import Decoration, RPS_ascii

class Game:
    color = Decoration.colors()
    def __init__(self):
        self.possibilities = ["Rock", "Paper", "Scissors"]

    def print_rules(self):
        print(f"{Game.color['Cyan']}Rules for winning the Rock Paper Scissors game are as follows:{Game.color['Reset']}")
        print(f"{Game.color['Pink']}Rock vs Paper => Paper wins{Game.color['Reset']}")
        print(f"{Game.color['Pink']}Rock vs Scissors => Rock wins{Game.color['Reset']}")
        print(f"{Game.color['Pink']}Paper vs Scissors => Scissors wins{Game.color['Reset']}")

    def play(self):
        os.system("cls" if os.name == "nt" else "clear")
        
        print(f"{Game.color['RWHITE']}************ Project: Rock Paper Scissors (RPS) ************{Game.color['Reset']}")
        RPS_ascii.Game()
        self.print_rules()
        try:
            while True:

                user_choice = input("\nEnter Your Choice (Rock, Paper, Scissors): ").capitalize()
                if user_choice not in self.possibilities:
                    print(f"{Game.color['Red']}Invalid choice.{Game.color['Reset']} Please enter Rock, Paper, or Scissors.")
                    continue
                
                computer_choice = random.choice(self.possibilities)
                print(f"\n{Game.color['Blue']}You chose: {Game.color['Reset']}")
                if user_choice == "Rock":
                    RPS_ascii.Rock_LtoR()
                elif user_choice == "Paper":
                    RPS_ascii.Paper_LtoR()
                else:
                    RPS_ascii.Scissors_LtoR()

                print(f"\n{Game.color['Blue']}Computer chose: {Game.color['Reset']}")
                if computer_choice == "Rock":
                    RPS_ascii.Rock_RtoL()
                elif computer_choice == "Paper":
                    RPS_ascii.Paper_RtoL()
                else:
                    RPS_ascii.Scissors_RtoL()

                if user_choice == computer_choice:
                    print(f"Both players selected {user_choice}. {Game.color['LCyan']}It's a Tie.{Game.color['Reset']}\n")
                elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                     (user_choice == "Paper" and computer_choice == "Rock") or \
                     (user_choice == "Scissors" and computer_choice == "Paper"):
                    print(f"{user_choice} beats {computer_choice}. {Game.color['Green']}You Won!{Game.color['Reset']}\n")
                else:
                    print(f"{computer_choice} beats {user_choice}. {Game.color['Red']}You Lose.{Game.color['Reset']}\n")

                play_again = input(f"{Game.color['Pink']}Do you want to play again? (y/n):{Game.color['Reset']}")
                if play_again.lower() != "y":
                    print(f"{Game.color['Red']}Program Exited{Game.color['Reset']}")
                    break
        except KeyboardInterrupt:
            print(f"\n{Game.color['Red']}Program interrupted by user{Game.color['Reset']}")
        except Exception as e:
            print(f"\n{Game.color['Red']}An unexpected error occurred: {str(e)}{Game.color['Reset']}")

def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
