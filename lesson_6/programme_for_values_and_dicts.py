def pet_names(pets):
    return {v: k for k, v in pets.items()}


pets = {'Cat':'Tom', 'Mouse': 'Jerry', 'Dog': 'Spike'}

print(pet_names(pets))


