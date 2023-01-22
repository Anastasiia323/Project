def pet_names(pets):
    new_pets = {v: k for k, v in pets.items()}
    return new_pets

pets = {'Cat':'Tom', 'Mouse': 'Jerry', 'Dod': 'Spike'}

print(pet_names(pets))


