elements = {'Hydrogen': 'H', 'Helium': 'He', 'Lithium': 'Li', 'Beryllium': 'Be', 'Boron': 'B',
'Carbon': 'C', 'Nitrogen': 'N', 'Oxygen': 'O', 'Flourine': 'F', 'Neon': 'Ne', 'Sodium': 'Na', 'Magnesium': 'Mg',
'Aluminum': 'Al', 'Silicon': 'Si', 'Phosphorus': 'P',
'Sulfur': "S", 'Chlorine': 'Cl', 'Argon': 'Ar', 'Potassium': 'K',
'Calcium': 'Ca', 'Scandium': 'Sc', 'Titanium': 'Ti', 'Vanadium': 'V',
'Chromium': 'Cr', 'Manganese': 'Mn', 'Iron': 'Fe', 'Cobalt': 'Co',
'Nickle': 'Ni', 'Copper': 'Cu', "Zinc": "Zn", "Galium": "Ga",
'Germanium': 'Ge', 'Arsenic': 'As', 'Selenium': 'Se', 'Bromine': 'Br',
'Krypton': 'Kr', 'Rubidium': 'Rb', 'Strontium': 'Sr', "Yttrium": 'Y',
'Zirconium': 'Zr', 'Niobium': 'Nb', 'Molybdenum': 'Mo', 'Technetium': "Tc",
'Ruthenium': 'Ru', 'Rhodium': 'Rh', 'Palladium': 'Pd', 'Silver': 'Ag',
'Cadmium': 'Cd', "Indium": "In", "Tin": "Sn", "Antimony": "Sb", "Tellurium": "Te",
"Iodine": "I", "Xenon": "Xe", "Caesium": "Ce", "Barium": "Ba", "Lanthanum": "La", "Cerium": "Ce", "Praseodymium": "Pr",
"Neodymium": "Nd", "Promethium": "Pm", "Samarium": "Sm", "Europium": "Eu",
"Gadolinium": "Gd", "Terbium": "Tb", "Dysprosium": "Dy", "Holmium": "Ho", "Erbium": "Er", "Thulium": "Tm", "Ytterbium": "Yb",
"Lutetium": "Lu", "Hafnium": "Hf", "Tantalum": "Ta", "Tungsten": "W", "Rhenium": "Re", "Osmium": "Os", "Iridium": "Ir",
"Platinum": "Pt", "Gold": "Au", "Mercury": "Hg", "Thallium": "Tl", "Lead": "Pb", "Bismuth": "Bi", "Polonium": "Po",
"Astatine": "At", }


print("Starting quiz!")
print("Type Forgot element if you don't any elements.")
print("Type Forgot symbol if you don't remember the compound.")
print("Please type your answers with correct capitalization.")

while len(elements) > 0:
    print('Enter an element: ')
    answer = input()
    if answer.lower().startswith('forgot element'):
        print(elements.keys())

    if answer not in elements and answer.lower() != "forgot element":
        print('Sorry, that is not in the periodic table.')
    if answer in elements:
        print('Enter ' + answer + "'s symbol.")
        symbol = input()
        if symbol.lower().startswith('forgot symbol') or symbol not in elements:
            print("Sorry, that's not correct. The correct answer is " + elements.get(answer))
        if elements.get(answer) == symbol:
            elements.pop(answer)
            print("Nice! That's the right answer... Removed %s" % answer)

print("Congrats you passed!")