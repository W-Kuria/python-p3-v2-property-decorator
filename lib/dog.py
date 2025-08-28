#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
    "Mutt",  # include Mutt because your __init__ default uses it
]

class Dog:
    def __init__(self, name="Fido", breed="Mutt"):
        # go through property setters so validation applies
        self.name = name
        self.breed = breed

    # ---- Name Property ----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    # ---- Breed Property ----
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in list of approved breeds.")
