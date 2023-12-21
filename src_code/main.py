import json
import os
from colorama import Fore, Style
from datetime import datetime

class WildlifeConservation:
    def __init__(self):
        self.entries = {}
        self.filename = 'entries.json'  #file name to store animal info

def add_entry(self, name, species, age, zone, date_rescued):
        if name not in self.entries:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.entries[name] = {'species': species, 'age': age, 'zone': zone, 'date_rescued': date_rescued, 'added_at': current_date}
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