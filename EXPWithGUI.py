import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from math import floor

gen3Yield = {'abra': 73, 'absol': 174, 'aerodactyl': 202, 'aggron': 205,
             'aipom': 94, 'alakazam': 186, 'altaria': 188, 'ampharos': 194,
             'anorith': 119, 'arbok': 147, 'arcanine': 213, 'ariados': 134,
             'armaldo': 200, 'aron': 96, 'articuno': 215, 'azumarill': 153,
             'azurill': 33, 'bagon': 89, 'baltoy': 58, 'banette': 179,
             'barboach': 92, 'bayleef': 141, 'beautifly': 161, 'beedrill': 159,
             'beldum': 103, 'bellossom': 184, 'bellsprout': 84,
             'blastoise': 210, 'blaziken': 209, 'blissey': 255, 'breloom': 165,
             'bulbasaur': 64, 'butterfree': 160, 'cacnea': 97, 'cacturne': 177,
             'camerupt': 175, 'carvanha': 88, 'cascoon': 72, 'castform': 145,
             'caterpie': 53, 'celebi': 64, 'chansey': 255, 'charizard': 209,
             'charmander': 65, 'charmeleon': 142, 'chikorita': 64,
             'chimecho': 147, 'chinchou': 90, 'clamperl': 142, 'claydol': 189,
             'clefable': 129, 'clefairy': 68, 'cleffa': 37, 'cloyster': 203,
             'combusken': 142, 'corphish': 111, 'corsola': 113, 'cradily': 201,
             'crawdaunt': 161, 'crobat': 204, 'croconaw': 143, 'cubone': 87,
             'cyndaquil': 65, 'delcatty': 138, 'delibird': 183, 'deoxys': 215,
             'dewgong': 176, 'diglett': 81, 'ditto': 61, 'dodrio': 158,
             'doduo': 96, 'donphan': 189, 'dragonair': 144, 'dragonite': 218,
             'dratini': 67, 'drowzee': 102, 'dugtrio': 153, 'dunsparce': 75,
             'dusclops': 179, 'duskull': 97, 'dustox': 160, 'eevee': 92,
             'ekans': 62, 'electabuzz': 156, 'electrike': 104,
             'electrode': 150, 'elekid': 106, 'entei': 217, 'espeon': 197,
             'exeggcute': 98, 'exeggutor': 212, 'exploud': 184,
             "farfetch'd": 94, 'farfetchd': 94, 'fearow': 162, 'feebas': 61,
             'feraligatr': 210, 'flaaffy': 117, 'flareon': 198, 'flygon': 197,
             'forretress': 118, 'furret': 116, 'gardevoir': 208, 'gastly': 95,
             'gengar': 190, 'geodude': 86, 'girafarig': 149, 'glalie': 187,
             'gligar': 108, 'gloom': 132, 'golbat': 171, 'goldeen': 111,
             'golduck': 174, 'golem': 177, 'gorebyss': 178, 'granbull': 178,
             'graveler': 134, 'grimer': 90, 'groudon': 218, 'grovyle': 141,
             'growlithe': 91, 'grumpig': 164, 'gulpin': 75, 'gyarados': 214,
             'hariyama': 184, 'haunter': 126, 'heracross': 200,
             'hitmonchan': 140, 'hitmonlee': 139, 'hitmontop': 138,
             'ho-oh': 220, 'hoothoot': 58, 'hoppip': 74, 'horsea': 83,
             'houndoom': 204, 'houndour': 114, 'huntail': 178, 'hypno': 165,
             'igglybuff': 39, 'illumise': 146, 'ivysaur': 141, 'jigglypuff': 76,
             'jirachi': 215, 'jolteon': 197, 'jumpluff': 176, 'jynx': 137,
             'kabuto': 119, 'kabutops': 201, 'kadabra': 145, 'kakuna': 71,
             'kangaskhan': 175, 'kecleon': 132, 'kingdra': 207, 'kingler': 206,
             'kirlia': 140, 'koffing': 114, 'krabby': 115, 'kyogre': 218,
             'lairon': 152, 'lanturn': 156, 'lapras': 219, 'larvitar': 67,
             'latias': 211, 'latios': 211, 'ledian': 134, 'ledyba': 54,
             'lickitung': 127, 'lileep': 121, 'linoone': 128, 'lombre': 141,
             'lotad': 74, 'loudred': 216, 'ludicolo': 181, 'lugia': 220,
             'lunatone': 150, 'luvdisc': 110, 'machamp': 193, 'machoke': 146,
             'machop': 88, 'magby': 117, 'magcargo': 154, 'magikarp': 20,
             'magmar': 167, 'magnemite': 89, 'magneton': 161, 'makuhita': 87,
             'manectric': 168, 'mankey': 74, 'mantine': 168, 'mareep': 59,
             'marill': 58, 'marowak': 124, 'marshtomp': 143, 'masquerain': 128,
             'mawile': 98, 'medicham': 153, 'meditite': 91, 'meganium': 208,
             'meowth': 69, 'metagross': 210, 'metang': 153, 'metapod': 72,
             'mew': 64, 'mewtwo': 220, 'mightyena': 218, 'milotic': 213,
             'miltank': 200, 'minun': 120, 'misdreavus': 147, 'moltres': 217,
             'mr. mime': 136, 'mr.mime': 136, 'mr mime': 136, 'mrmime': 136,
             'mudkip': 65, 'muk': 157, 'murkrow': 107, 'natu': 73,
             'nidoking': 195, 'nidoqueen': 194, 'nidoran': 59.5,
             'nidorina': 117, 'nidorino': 118, 'nincada': 65, 'ninetails': 178,
             'ninjask': 155, 'noctowl': 162, 'nosepass': 108, 'numel': 88,
             'nuzleaf': 141, 'octillery': 164, 'oddish': 78, 'omanyte': 120,
             'lord helix': 120, 'omastar': 199, 'onix': 108, 'paras': 70,
             'parasect': 128, 'pelipper': 164, 'persian': 148, 'phanpy': 124,
             'pichu': 42, 'pidgeot': 172, 'pidgeotto': 113, 'pidgey': 55,
             'pikachu': 82, 'piloswine': 160, 'pineco': 60, 'pinsir': 200,
             'plusle': 120, 'politoed': 185, 'poliwag': 77, 'poliwhirl': 131,
             'poliwrath': 185, 'ponyta': 152, 'poochyena': 55, 'porygon': 130,
             'porygon2': 180, 'primeape': 149, 'psyduck': 80, 'pupitar': 144,
             'quagsire': 137, 'quilava': 142, 'quilfish': 100, 'raichu': 122,
             'raikou': 216, 'ralts': 70, 'rapidash': 192, 'raticate': 116,
             'rattata': 57, 'rayquaza': 220, 'regice': 216, 'regirock': 217,
             'registeel': 215, 'relicanth': 198, 'remoraid': 78, 'rhydon': 204,
             'rhyhorn': 135, 'roselia': 152, 'sableye': 98, 'salamence': 218,
             'sandshrew': 93, 'sandslash': 163, 'sceptile': 208, 'scizor': 200,
             'scyther': 187, 'seadra': 155, 'seaking': 170, 'sealeo': 128,
             'seedot': 74, 'seel': 100, 'sentret': 57, 'seviper': 165,
             'sharpedo': 175, 'shedinja': 95, 'shelgon': 144, 'shellder': 97,
             'shiftry': 181, 'shroomish': 65, 'shuckle': 80, 'shuppet': 97,
             'silcoon': 71, 'skarmory': 168, 'skiploom': 136, 'skitty': 65,
             'slaking': 210, 'slakoth': 83, 'slowbro': 164, 'slowking': 164,
             'slowpoke': 99, 'slugma': 78, 'smeargle': 106, 'smoochum': 87,
             'sneasel': 132, 'snorlax': 154, 'snorunt': 74, 'snubbull': 63,
             'solrock': 150, 'spearow': 58, 'spheal': 75, 'spinarak': 54,
             'spinda': 85, 'spoink': 89, 'squirtle': 66, 'stantler': 165,
             'starmie': 207, 'staryu': 106, 'steelix': 196, 'sudowoodo': 135,
             'suicune': 215, 'sunflora': 146, 'sunkern': 52, 'surskit': 63, 
             'swablu': 74, 'swalot': 168, 'swampert': 210, 'swellow': 162,
             'swinub': 78, 'taillow': 59, 'tangela': 166, 'tauros': 211,
             'teddiursa': 124, 'tentacool': 105, 'tentacruel': 205,
             'togepi': 74, 'togetic': 114, 'torchic': 65, 'torkoal': 161,
             'totodile': 66, 'trapinch': 73, 'treeko': 65, 'tropius': 169,
             'typhlosion': 209, 'tyranitar': 218, 'tyrogue': 91, 'umbreon': 197,
             'unown': 61, 'ursaring': 189, 'vaporeon': 196, 'venomoth': 138,
             'venonat': 75, 'venusaur': 208, 'vibrava': 126, 'victreebel': 191,
             'vigoroth': 126, 'vileplume': 184, 'volbeat': 146, 'voltorb': 103,
             'vulpix': 63, 'wailmer': 137, 'wailord': 206, 'walrein': 192,
             'wartortle': 143, 'weedle': 52, 'weepinbell': 151, 'weezing': 173,
             'whishcash': 158, 'whismur': 68, 'wigglytuff': 109, 'wingull': 64,
             'wobbuffet': 177, 'wooper': 52, 'wurmple': 54, 'wynaut': 44,
             'xatu': 171, 'yanma': 147, 'zangoose': 165, 'zapdos': 216,
             'zigzagoon': 60, 'zubat': 54}

def levelChanged(event):
    L = level.get()
    msg = f"Opponent's Level: {L}"
    levelDisplay.config(text = msg)

# Will actually do the exp calculation
def go():
    if trainer.get() == 1:
        a = 1.5
    else:
        a = 1

    if egg.get() == 1:
        e = 1.5
    else:
        e = 1

    if ot.get():
        t = 1
    else:
        t = 1.5

    if expShare.get():
        s = 2
    else:
        s = 1

    s = s*number.get()

    L = level.get()

    b = gen3Yield[pokemon.get().lower()]

    exp = floor((a*t*b*e*L)/(7*s))

    msg = f'EXP Points gained: {exp}'
    resultLabel.config(text = msg)

# Create main window
root = tk.Tk()
root.title("EXP Calculator")

# Return values from UI
pokemon = tk.StringVar()
pokemon.set("Abra")
trainer = tk.BooleanVar()
egg = tk.BooleanVar()
ot = tk.BooleanVar()
expShare = tk.BooleanVar()
level = tk.IntVar()
level.set(1)
number = tk.IntVar()
number.set(1)

# Create container frames
pokemonFrame = ttk.Frame(root)
pokemonFrame.pack(padx = 10, pady = 10, fill = "x")

defeatedFrame = ttk.Frame(root)
defeatedFrame.pack(padx = 10, pady = 10, fill = "x")

checkboxFrame = ttk.Frame(root)
checkboxFrame.pack(padx = 10, pady = 10, fill = "x")

bottomFrame = ttk.Frame(root)
bottomFrame.pack(padx = 10, pady = 10, fill = "x")

# Pokemon (Top) frame
pokemonLabel = ttk.Label(pokemonFrame, text = "Pokemon: ")
pokemonLabel.pack(side = 'left')

pokemonBox = ttk.Combobox(pokemonFrame, textvariable = pokemon)
gen3Names = []
for key in gen3Yield.keys():
    gen3Names.append(key.capitalize())
pokemonBox['values'] = [gen3Names[i] for i in range(0, len(gen3Names))]
pokemonBox['state'] = 'readonly'
pokemonBox.pack(side = 'left')

numberLabel = ttk.Label(pokemonFrame, text = "Number that battled: ")
numberLabel.pack(side = 'left')

pokemonNumber = ttk.Spinbox(pokemonFrame,
                            from_ = 1,
                            to = 6,
                            values = (1, 2, 3, 4, 5, 6),
                            textvariable = number,
                            wrap = True,
                            width = 3)
pokemonNumber.pack(side = 'left')

# Defeated (2nd) frame
levelDisplay = ttk.Label(defeatedFrame,
                         text = "Opponent's Level: 1")
levelDisplay.pack()

levelSlider = ttk.Scale(defeatedFrame,
                        from_ = 1,
                        to = 100,
                        orient = 'horizontal',
                        variable = level,
                        command = levelChanged)
levelSlider.pack(fill = 'x', side = 'bottom')

# Checkbox (Middle) frame
ttk.Checkbutton(checkboxFrame, 
                text = "Trainer Battle",
                variable = trainer,
                onvalue = True,
                offvalue = False
).pack(side = 'left')

ttk.Checkbutton(checkboxFrame, 
                text = "Lucky Egg",
                variable = egg,
                onvalue = True,
                offvalue = False
).pack(side = 'left')

ttk.Checkbutton(checkboxFrame, 
                text = "Original Trainer",
                variable = ot,
                onvalue = True,
                offvalue = False
).pack(side = 'left')

ttk.Checkbutton(checkboxFrame, 
                text = "EXP Share",
                variable = expShare,
                onvalue = True,
                offvalue = False
).pack(side = 'left')

# bottom frame
goButton = ttk.Button(bottomFrame, text="Go", command=go)
goButton.pack()

resultLabel = ttk.Label(bottomFrame)
resultLabel.pack(side = 'bottom')

root.mainloop()