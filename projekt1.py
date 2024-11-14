'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Dvořák
email: d.dvorak601@gmail.com
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("Přihlašovací jméno:")
if jmeno in users:
    heslo = input("Přihlašovací heslo:")
    if users[jmeno] == heslo:
        print("Vítej", jmeno, "v aplikaci na analýzu textu.")
    else:
        print("Přihlašovací heslo je neplatné. Ukončuji program")
        quit()
else:
    print("Přihlašovací jméno je neplatné. Ukončuji program.")
    quit()
print("----------------------------------------")

pocet_jednotek = len(set(TEXTS))
print("V současné době máte k analýze nachystané", pocet_jednotek, "texty.") 
print("Zvolte číslo textu, který chcete analyzovat:")
for nmbr, _ in enumerate(TEXTS, start=1):
    print(nmbr, end=" ")
print()
print("----------------------------------------")

vybrany_text = input()
print("----------------------------------------")
if vybrany_text.isdigit() and 1 <= int(vybrany_text) <= len(TEXTS):
    index = int(vybrany_text) - 1 
    vybrany_text = TEXTS[index]
    pocet_slov = len(vybrany_text.split())
    print("Počet slov ve vybraném textu:", pocet_slov)
    slova = vybrany_text.split()
    pocet_slov_s_velkym_pismenem = sum(1 for slovo in slova if slovo.istitle())
    print("Počet slov začínajících velkým písmenem:", pocet_slov_s_velkym_pismenem)
    pocet_slov_psany_kapitalkami = sum(1 for slovo in slova if slovo.isupper() and slovo.isalpha())
    print("Počet slov psaných velkými pismeny:", pocet_slov_psany_kapitalkami)
    pocet_slov_psany_malymi_pismeny = sum (1 for slovo in slova if slovo.islower())
    print("Počet slov psaný malými písmeny:", pocet_slov_psany_malymi_pismeny)
    pocet_cisel = sum(1 for slovo in slova if slovo.isnumeric())
    print("Počet čísel:", pocet_cisel)
    suma_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())
    print("Suma všech čísel:", suma_cisel)
else:
    print("Zvolené číslo textu není v povoleném rozsahu, nebo byl vložen nečíselný znak.")
    print("Ukončuji program.")
    quit()
print("----------------------------------------")
    
import string
slova = [slovo.strip(string.punctuation) for slovo in slova]

delky_slov = {}
for slovo in slova:
    delka = len(slovo)
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1

print("LEN | OCCURRENCES        | NR.")
print("----------------------------------------")
for delka, pocet in sorted(delky_slov.items()):
    print("{:3} | {:<18} | {}".format(delka, '*' * pocet, pocet))
print("----------------------------------------")