''' Import Errors: Fix-1
Since NepalZipCode.py is inside the Essentials folder, importing the Decoration 
class using from Essentials import Decoration will not work because it's trying 
to import a package that is at the same level.
To fix this, you can use a relative import instead. i.e.
Instead of: from Essentials import Decoration  # Import the Decoration class
Use: from .decoration import Decoration  # Use relative import

Fix-2:
The error is due to running NepalZipCode.py as a standalone script. Relative imports 
only work when the script is run as part of a package. To handle this, you can modify 
the script to allow it to be run directly or as part of a package.
Modifications needed:
Relative and Absolute Imports: The try block attempts a relative import (from .decoration 
import Decoration), which works if the script is part of a package. If it fails, the except block 
handles an absolute import (from decoration import Decoration), allowing the script to run standalone.'''
import json
import os

try:
    from .decoration import Decoration
except ImportError:
    from decoration import Decoration 

class PostalCodeManager:
    def __init__(self, filePath):
        self.postalData = self.loadPostalData(filePath)
        self.cityDistrictMap = self.createCityDistrictMapping(self.postalData)
        self.colors = Decoration.colors()  # Get the color codes

    def loadPostalData(self, filePath):
        with open(filePath, 'r') as jsonFile:
            postalData = json.load(jsonFile)
        return postalData

    def createCityDistrictMapping(self, postalData):
        cityDistrictMap = {}
        for district, cities in postalData.items():
            for city, postalCode in cities.items():
                cityDistrictMap[city.lower()] = (district, postalCode)
        return cityDistrictMap

    def getPostalCode(self, city):
        city = city.lower()
        if city in self.cityDistrictMap:
            district, postalCode = self.cityDistrictMap[city]
            return district, postalCode
        else:
            return None, None

    def displayCities(self, district):
        if district in self.postalData:
            return self.postalData[district]
        else:
            return None

    def displayInfo(self):
        Decoration.nepalPIN_ascii()
        print(f"{self.colors['Blue']}Postal Code is also known as Post Code, PIN or ZIP Code. It is a series of letters, digits, spaces or even punctuation.{self.colors['Reset']}")
        print(f"{self.colors['Blue']}Postal Code represents the geographic areas of addresses and help the concerned postal services deliver mail to them.{self.colors['Reset']}")
        print(f"{self.colors['Pink']}Postal Code in Nepal are five digit numbers. Nepal has Post Office in all the 77 districts.{self.colors['Reset']}")

    def handleGetPostalCode(self):
        city = input(f"{self.colors['LCyan']}Enter the city name: {self.colors['Reset']}").strip().title()
        district, postalCode = self.getPostalCode(city)
        if postalCode:
            print(f"{self.colors['Green']}The postal code of {city} in {district} is {postalCode}.{self.colors['Reset']}")
        else:
            print(f"{self.colors['Red']}No postal code found for {city}.{self.colors['Reset']}")

    def handleFindCities(self):
        partialDistrict = input(f"{self.colors['LCyan']}Enter the partial district name (e.g., 'R' for districts starting with R): {self.colors['Reset']}").strip().title()
        matchingDistricts = [dist for dist in self.postalData if dist.startswith(partialDistrict)]
        if not matchingDistricts:
            print(f"{self.colors['Red']}No districts found starting with '{partialDistrict}'.{self.colors['Reset']}")
        else:
            self.displayMatchingDistricts(matchingDistricts)

    def displayMatchingDistricts(self, matchingDistricts):
        print(f"{self.colors['Green']}Matching districts:{self.colors['Reset']}")
        for index, dist in enumerate(matchingDistricts, start=1):
            print(f"{self.colors['Pink']}{index}. {dist}{self.colors['Reset']}")
        self.chooseDistrict(matchingDistricts)

    def chooseDistrict(self, matchingDistricts):
        choiceDistrict = input(f"{self.colors['LCyan']}Enter the number corresponding to the district: {self.colors['Reset']}")
        try:
            choiceIndex = int(choiceDistrict) - 1
            if 0 <= choiceIndex < len(matchingDistricts):
                selectedDistrict = matchingDistricts[choiceIndex]
                self.displayCitiesInDistrict(selectedDistrict)
            else:
                print(f"{self.colors['Red']}Invalid choice.{self.colors['Reset']}")
        except ValueError:
            print(f"{self.colors['Red']}Invalid input. Please enter a number.{self.colors['Reset']}")

    def displayCitiesInDistrict(self, selectedDistrict):
        cities = self.displayCities(selectedDistrict)
        if cities:
            print(f"{self.colors['Green']}The cities in {selectedDistrict} are:{self.colors['Reset']}")
            for city, postalCode in cities.items():
                print(f"{self.colors['Pink']}{city}: {postalCode}{self.colors['Reset']}")
        else:
            print(f"{self.colors['Red']}No cities found for district {selectedDistrict}.{self.colors['Reset']}")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    '''don't use this: postalCodeManager = PostalCodeManager('district_codes.json')'''
    postalCodeManager = PostalCodeManager(os.path.join(os.path.dirname(__file__), 'district_codes.json'))
    colors = Decoration.colors() 

    print(f"{colors['RWHITE']}************ Project: POSTAL CODE OF NEPAL ************{colors['Reset']}")
    try:
        while True:
            print(f"\n{colors['LCyan']}Options:{colors['Reset']}")
            print(f"{colors['Blue']}1. Get Info about Postal Code{colors['Reset']}")
            print(f"{colors['Blue']}2. Get Postal Code of a City{colors['Reset']}")
            print(f"{colors['Blue']}3. Having trouble finding the postal code?{colors['Reset']}")
            print(f"{colors['Red']}4. Exit{colors['Reset']}")
            
            choice = input(f"{colors['LCyan']}Enter your choice: {colors['Reset']}")
            if choice == "1":
                postalCodeManager.displayInfo()
            elif choice == "2":
                postalCodeManager.handleGetPostalCode()
            elif choice == "3":
                postalCodeManager.handleFindCities()
            elif choice == "4":
                print(f"{colors['Red']}Program Exited{colors['Reset']}")
                break
            else:
                print(f"{colors['Red']}Invalid choice. Please try again.{colors['Reset']}")
    except KeyboardInterrupt:
        print(f"\n{colors['Red']}Program interrupted by user{colors['Reset']}")
    except Exception as e:
        print(f"\n{colors['Red']}An unexpected error occurred: {str(e)}{colors['Reset']}")

if __name__ == "__main__":
    main()
