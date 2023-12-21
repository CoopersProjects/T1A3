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

