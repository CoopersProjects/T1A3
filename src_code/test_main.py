import os
import json
import pytest
import uuid
from datetime import datetime, timedelta
from main import WildlifeConservation

@pytest.fixture
def conservation_instance():
    return WildlifeConservation()

def generate_unique_name():
    return f'TestAnimal_{uuid.uuid4().hex[:8]}'

def load_entries_safely(conservation_instance):
    try:
        conservation_instance.load_entries()
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading entries: {e}")
        conservation_instance.entries = {}

def test_add_entry(conservation_instance):
    # Load entries manually to handle possible exceptions
    load_entries_safely(conservation_instance)

    name = generate_unique_name()
    species = 'TestSpecies'
    age = 5
    zone = 3
    date_rescued = datetime.now().strftime('%d-%m-%Y')

    conservation_instance.add_entry(name, species, age, zone, date_rescued)

    assert name in conservation_instance.entries
    assert conservation_instance.entries[name]['species'] == species
    assert conservation_instance.entries[name]['age'] == age
    assert conservation_instance.entries[name]['zone'] == zone
    assert conservation_instance.entries[name]['date_rescued'] == date_rescued

def test_update_entry(conservation_instance):
    # Load entries manually to handle possible exceptions
    load_entries_safely(conservation_instance)

    name = generate_unique_name()
    species = 'TestSpecies'
    age = 5
    zone = 3
    date_rescued = datetime.now().strftime('%d-%m-%Y')


    conservation_instance.add_entry(name, species, age, zone, date_rescued)

    new_species = 'NewTestSpecies'
    new_age = 6
    new_zone = 4
    new_date_rescued = (datetime.now() - timedelta(days=365)).strftime('%d-%m-%Y')  # Example: One year ago


    conservation_instance.update_entry(name, new_species, new_age, new_zone, new_date_rescued)

    assert conservation_instance.entries[name]['species'] == new_species
    assert conservation_instance.entries[name]['age'] == new_age
    assert conservation_instance.entries[name]['zone'] == new_zone
    assert conservation_instance.entries[name]['date_rescued'] == new_date_rescued


# Requires terminal command: pytest -s test_main.py
# Note: This test will succeed on the first attempt, but will fail to add new entry on a second run due to the name being taken by the first attempt (New test species).
