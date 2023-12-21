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

