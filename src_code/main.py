import json
import os
from colorama import Fore, Style
from datetime import datetime


class WildlifeConservation:
    def __init__(self):
        self.entries = {}
        self.filename = 'entries.json'  # File name to store animal info

    def add_entry(self, name, species, age, zone, date_rescued):
        if name not in self.entries:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.entries[name] = {
                'species': species,
                'age': age,
                'zone': zone,
                'date_rescued': date_rescued,
                'added_at': current_date
            }
            print(f'{Fore.GREEN}{name} has been added to the conservation.{Style.RESET_ALL}')
            self.save_entries()
        else:
            print(f'{Fore.RED}{name} is already in the conservation. Use update_entry() to update information.{Style.RESET_ALL}')

    def update_entry(self, name, species=None, age=None, zone=None, date_rescued=None):
        if name in self.entries:
            entry = self.entries[name]

            if species is not None:
                entry['species'] = species
            if age is not None:
                entry['age'] = age
            if zone is not None:
                entry['zone'] = zone
            if date_rescued is not None:
                entry['date_rescued'] = date_rescued

            print(f'{Fore.GREEN}Information for {name} has been updated.{Style.RESET_ALL}')
            self.save_entries()
        else:
            print(f'{Fore.RED}{name} is not in the conservation. Use Option 1 to add them, or check for possible spelling errors.{Style.RESET_ALL}')

    def delete_entry(self, name):
        if name in self.entries:
            del self.entries[name]
            print(f'{name} has been released from the conservation.')
            self.save_entries()
        else:
            print(f'{name} is not in the conservation.')

    def display_entries(self):
        if self.entries:
            print('List of Wildlife Conservation Entries:')
            for name, info in self.entries.items():
                print(f'Name: {name}, Species: {info["species"]}, Age: {info["age"]}, Zone: {info["zone"]}, '
                      f'Date Rescued: {info["date_rescued"]}')
        else:
            print('The wildlife conservation is currently empty.')

    def search_by_zone(self, zone):
        matching_entries = [(name, info) for name, info in self.entries.items() if str(info['zone']) == str(zone)]
        if matching_entries:
            print(f'Entries in Zone {zone}:')
            for name, info in matching_entries:
                print(f'Name: {name}, Species: {info["species"]}, Age: {info["age"]}, '
                      f'Date Rescued: {info["date_rescued"]}')
        else:
            print(f'No entries found in Zone {zone}.')

    def save_entries(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file, indent=2)

    def load_entries(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    file_content = file.read()
                    if file_content:
                        self.entries = json.loads(file_content)
                    else:
                        # Handle the case where the file is empty
                        self.entries = {}
            except json.JSONDecodeError as e:
                # To handle the case where the file contains invalid JSON
                print(f"Error loading entries: {e}")
                self.entries = {}
        else:
            self.entries = {}



def display_menu():
    print('\nWildlife Conservation Menu:')
    print('1. Add Entry')
    print('2. Update Entry')
    print('3. Delete Entry')
    print('4. Display All Entries')
    print('5. Search by Zone')
    print('6. Exit')

if __name__ == "__main__":
    conservation = WildlifeConservation()
    conservation.load_entries()  # Load entries from file at the beginning

while True:
    display_menu()
    choice = input('Enter your choice (1-6): ')

    if choice == '1':
        name = input('Enter the name of the animal: ')
        species = input('Enter the species: ')

        while True:
            age_input = input('Enter the age: ')
            try:
                age = int(age_input)
                break
            except ValueError:
                print('Invalid input for age. Please enter a valid number.')

        while True:
            zone_input = input('Enter the zone (1-6): ')
            if zone_input.isdigit() and 1 <= int(zone_input) <= 6:
                zone = int(zone_input)
                break
            else:
                print('Invalid input for zone. Please enter a number between 1 and 6.')

        while True:
            date_rescued_input = input('Enter the date rescued (DD-MM-YYYY): ')
            try:
                date_rescued = datetime.strptime(date_rescued_input, '%d-%m-%Y').strftime('%d-%m-%Y')
                break
            except ValueError:
                print('Invalid date format. Please enter the date in DD-MM-YYYY format.')

        conservation.add_entry(name, species, age, zone, date_rescued)

    elif choice == '2':
        name = input('Enter the name of the animal to update: ')
        entry = conservation.entries.get(name)

        if entry is not None:
            print(f"Updating information for {name}:")

            current_species = entry.get('species')
            current_age = entry.get('age')
            current_zone = entry.get('zone')
            current_date_rescued = entry.get('date_rescued')

            species = input(f'Enter the new species ({current_species}) (press Enter to skip): ')
            if species.strip() == '':
                species = current_species

            age = None
            zone = None
            date_rescued = None

            valid_age = False
            while not valid_age:
                age_input = input(f'Enter the new age ({current_age}) (press Enter to skip): ')
                if age_input.strip() == '':
                    break  
                try:
                    age = int(age_input)
                    if age < 0:
                        print('Invalid input for age. Please enter a non-negative number.')
                    else:
                        valid_age = True
                except ValueError:
                    print('Invalid input for age. Please enter a valid number.')

            zone_input = input(f'Enter the new zone ({current_zone}) (press Enter to skip): ')
            if zone_input.strip():
                if zone_input.isdigit() and 1 <= int(zone_input) <= 6:
                    zone = int(zone_input)
                else:
                    print('Invalid input for zone. Please enter a number between 1 and 6.')

            date_rescued_input = input(f'Enter the new date rescued ({current_date_rescued}) (DD-MM-YYYY, press Enter to skip): ')
            if date_rescued_input.strip():
                try:
                    date_rescued = datetime.strptime(date_rescued_input, '%d-%m-%Y').strftime('%d-%m-%Y')
                except ValueError:
                    print('Invalid date format. Please enter the date in DD-MM-YYYY format.')

            conservation.update_entry(name, species, age, zone, date_rescued)

    elif choice == '3':
        name = input('Enter the name of the animal to delete: ')
        conservation.delete_entry(name)

    elif choice == '4':
        conservation.display_entries()

    elif choice == '5':
        while True:
            zone_input = input('Enter the zone to search (1-6): ')
            if zone_input.isdigit() and 1 <= int(zone_input) <= 6:
                zone = int(zone_input)
                break
            else:
                print('Sorry, that zone does not exist. Please enter a zone between 1 and 6.')

        conservation.search_by_zone(zone)

    elif choice == '6':
        print('Thanks for using the Conservation System! Booting down... ')
        break

    else:
        print('Sorry, that is not a listed option. Please enter a number between 1 and 6.')
