import requests
import os

try:
    from .decoration import Decoration
except ImportError:
    from decoration import Decoration

def display_info():
        colors = Decoration.colors()
        Decoration.bot_ascii()
        print(f"{colors['RWHITE']}************ Project: ChatBot - Gemini Chatter ************{colors['Reset']}")
        print(f"{colors['Pink']}This is a simple chat bot with restrictions...{colors['Reset']}")

def bot(msg):
    data = '{"contents":[{"parts":[{"text":"' + msg + '"}]}]}'
    url = 'Add Your Gemini API'
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, data=data).json()
    return response["candidates"][0]['content']['parts'][0]['text']

def main():
    os.system("cls")
    colors = Decoration.colors()
    display_info()
    try:
        while True:
            msg = input(f"{colors['LCyan']}YOU: {colors['Reset']}")
            
            try:
                bot_reply = bot(msg)
                print(f"{colors['LCyan']}BOT: {colors['Reset']}{bot_reply}")
            except Exception as e:
                print(f"{colors['Red']}Error: {str(e)}{colors['Reset']}")
            
            choice = input(f"{colors['Pink']}Do you want to play again? (y/n):{colors['Reset']}\n")
            if choice.lower() != "y":
                print(f"{colors['Red']}Program Exited{colors['Reset']}")
                break
    except KeyboardInterrupt:
        print(f"\n{colors['Red']}Program interrupted by user{colors['Reset']}")
    except Exception as e:
        print(f"\n{colors['Red']}An unexpected error occurred: {str(e)}{colors['Reset']}")

if __name__ == "__main__":
    main()
