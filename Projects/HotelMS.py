import os
try:
    from .decoration import Decoration
except ImportError:
    from decoration import Decoration
    
class HotelManagement:
    ROOM_TYPES = {
        1: {"name": "Type A", "price": 5000},
        2: {"name": "Type B", "price": 4000},
        3: {"name": "Type C", "price": 3000},
        4: {"name": "Type D", "price": 2000}
    }

    RESTAURANT_MENU = {
        1: {"item": "Water", "price": 10},
        2: {"item": "Tea", "price": 20},
        3: {"item": "Breakfast Combo", "price": 90},
        4: {"item": "Lunch", "price": 110},
        5: {"item": "Dinner", "price": 150}
    }

    LAUNDRY_MENU = {
        1: {"item": "Shirt", "price": 3},
        2: {"item": "Jeans", "price": 4},
        3: {"item": "Daura Suruwal", "price":  7},
        4: {"item": "Sari", "price": 7},
        5: {"item": "Gunyou Cholo", "price": 8}
    }

    GAME_MENU = {
        1: {"item": "Table Tennis", "price": 60},
        2: {"item": "Badminton", "price": 80},
        3: {"item": "Snooker", "price": 70},
        4: {"item": "Video Games", "price": 90},
        5: {"item": "Pool", "price": 50}
    }

    def __init__(self):
        self.customerName = ""
        self.customerAddress = ""
        self.checkInDate = ""
        self.checkOutDate = ""
        self.roomNumber = 0
        self.roomRent = 0
        self.restaurantBill = 0
        self.laundryBill = 0
        self.gameBill = 0
        self.totalBill = 0
        self.serviceCharge = 1800

    def inputCustomerData(self):
        print("\n--- Enter Customer Data ---")
        self.customerName = input("Enter your name: ")
        self.customerAddress = input("Enter your address: ")
        self.checkInDate = input("Enter your check-in date: ")
        self.checkOutDate = input("Enter your check-out date: ")
        
        while True:
            try:
                self.roomNumber = int(input("Enter your room number: "))
                if 100 < self.roomNumber < 1000:
                    break
                else:
                    print("Invalid room number. Please enter a number between 101 and 999.")
            except ValueError:
                print("Please enter a valid room number.")
        
        print(f"Your room number: {self.roomNumber}")

    def calculateRoomRent(self):
        print("\n--- Room Rent Calculation ---")
        print("We have the following rooms for you:")
        for key, room in self.ROOM_TYPES.items():
            print(f"{key}. {room['name']} ---> Rs {room['price']} per night")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice in self.ROOM_TYPES:
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                nights = int(input("For how many nights did you stay: "))
                if nights > 0:
                    break
                else:
                    print("Please enter a positive number of nights.")
            except ValueError:
                print("Please enter a valid number.")
        
        room = self.ROOM_TYPES[choice]
        self.roomRent = room["price"] * nights
        print(f"You have opted for {room['name']}")
        print(f"Your room rent is = Rs {self.roomRent}")

    def calculateMenuBill(self, menu, billName):
        print(f"\n--- {billName} Calculation ---")
        print(f"*****{billName.upper()} MENU*****")
        for key, item in menu.items():
            print(f"{key}. {item['item']} ---> Rs {item['price']}")
        print("0. Exit this menu")

        bill = 0
        itemizedBill = []
        while True:
            try:
                choice = int(input(f"\nEnter your choice (0 to finish {billName.lower()} selection): "))
                if choice == 0:
                    break
                if choice in menu:
                    while True:
                        try:
                            quantity = int(input("Enter the quantity (max 100): "))
                            if 0 < quantity <= 100:
                                break
                            elif quantity > 100:
                                print("Quantity too high. Please enter a number between 1 and 100.")
                            else:
                                print("Please enter a positive quantity.")
                        except ValueError:
                            print("Please enter a valid number.")

                    item_total = menu[choice]["price"] * quantity
                    bill += item_total
                    itemizedBill.append(f"{menu[choice]['item']} x{quantity}: Rs {item_total}")
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        print(f"\nItemized {billName} Bill:")
        for item in itemizedBill:
            print(item)
        print(f"Total {billName} cost = Rs {bill}")
        return bill

    def displayTotalCost(self):
        if not self.customerName:
            print("Please enter customer data first.")
            return

        print("\n******HOTEL BILL******")
        print("Customer details:")
        print(f"Name: {self.customerName}")
        print(f"Address: {self.customerAddress}")
        print(f"Check-in date: {self.checkInDate}")
        print(f"Check-out date: {self.checkOutDate}")
        print(f"Room number: {self.roomNumber}")
        print(f"Room rent: Rs {self.roomRent}")
        print(f"Restaurant bill: Rs {self.restaurantBill}")
        print(f"Laundry bill: Rs {self.laundryBill}")
        print(f"Game bill: Rs {self.gameBill}")

        self.totalBill = self.roomRent + self.restaurantBill + self.laundryBill + self.gameBill
        print(f"\nSub total bill: Rs {self.totalBill}")
        print(f"Additional service charge: Rs {self.serviceCharge}")
        print(f"Grand total bill: Rs {self.totalBill + self.serviceCharge}")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    colors = Decoration.colors() 
    hotel = HotelManagement()
    try:
        while True:
            print(f"\n{colors['LCyan']}*****WELCOME TO OUR HOTEL*****{colors['Reset']}")
            print(f"{colors['Blue']}1. Enter Customer Data{colors['Reset']}")
            print(f"{colors['Blue']}2. Calculate Room Rent{colors['Reset']}")
            print(f"{colors['Blue']}3. Calculate Restaurant Bill{colors['Reset']}")
            print(f"{colors['Blue']}4. Calculate Laundry Bill{colors['Reset']}")
            print(f"{colors['Blue']}5. Calculate Game Bill{colors['Reset']}")
            print(f"{colors['Blue']}6. Display Total Cost{colors['Reset']}")
            print(f"{colors['Red']}7. Exit{colors['Reset']}")

            try:
                choice = int(input(f"\n{colors['LCyan']}Enter your choice: {colors['Reset']}"))

                if choice == 1:
                    hotel.inputCustomerData()
                elif choice == 2:
                    hotel.calculateRoomRent()
                elif choice == 3:
                    hotel.restaurantBill = hotel.calculateMenuBill(hotel.RESTAURANT_MENU, "Restaurant")
                elif choice == 4:
                    hotel.laundryBill = hotel.calculateMenuBill(hotel.LAUNDRY_MENU, "Laundry")
                elif choice == 5:
                    hotel.gameBill = hotel.calculateMenuBill(hotel.GAME_MENU, "Game")
                elif choice == 6:
                    hotel.displayTotalCost()
                elif choice == 7:
                    print(f"{colors['LCyan']}Thank you for using our hotel management system. Goodbye!{colors['Reset']}")
                    break
                else:
                    print(f"{colors['Red']}Invalid choice. Please try again.{colors['Reset']}")
            except ValueError:
                print(f"{colors['Red']}Please enter a valid number.{colors['Reset']}")
    except KeyboardInterrupt:
        print(f"\n{colors['Red']}Program interrupted by user{colors['Reset']}")
    except Exception as e:
        print(f"\n{colors['Red']}An unexpected error occurred: {str(e)}{colors['Reset']}")
if __name__ == "__main__":
    main()