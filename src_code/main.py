import json
import os
from colorama import Fore, Style
from datetime import datetime

class WildlifeConservation:
    def __init__(self):
        self.entries = {}
        self.filename = 'entries.json'  #file name to store animal info

