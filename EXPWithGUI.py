# Python 3.9/3.10
import tkinter as tk
from tkinter import ttk
from math import floor

# Function definitions
# Updates opponent's level display
def levelChanged(event):
    L = level.get()
    msg = f"Opponent's Level: {L}"
    levelDisplay.config(text = msg)
# Enabes/Disables EXP Share field on check/uncheck of EXP Share checkbox
def shareNumberUpdate():
    global shareGate
    if shareGate == tk.DISABLED:
        shareNumber.config(state = tk.NORMAL, values = (1, 2, 3, 4, 5, 6))
        holdingShare.set(1)
        shareGate = tk.NORMAL
    else:
        shareNumber.config(state = tk.DISABLED, values = (0))
        holdingShare.set(0)
        shareGate = tk.DISABLED
# EXP calculation for pokemon on field
def gen3Main():
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

    return(floor((a*t*b*e*L)/(7*s)))
# EXP calculation for pokemon in party holding EXP Share
def gen3Shared():
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
        s = holdingShare.get()

    s = s*2

    L = level.get()

    b = gen3Yield[pokemon.get().lower()]

    return(floor((a*t*b*e*L)/(7*s)))
# Calls calculation functions, and updates output
def go():
    if expShare.get():
        exp = gen3Main()
        shared = gen3Shared()
        msg = f'Main EXP Points Gained: {exp}, Shared EXP Points Gained: {shared}'
        resultLabel.config(text = msg)
    else:
        exp = gen3Main()
        msg = msg = f'Main EXP Points Gained: {exp}'
        resultLabel.config(text = msg)

# EXP yields by generation
gen1Yield = {'bulbasaur': 64, 'ivysaur': 141, 'venusaur': 208, 'charmander': 65,
             'charmeleon': 142, 'charizard': 209, 'sqirtle': 66,
             'wartortle': 143, 'blastoise': 210, 'caterpie': 53, 'metapod': 72,
             'butterfree': 160, 'weedle': 52, 'kakuna': 71, 'beedrill': 159,
             'pidgey': 55, 'pidgeotto': 113, 'pidgeot': 172, 'rattata': 57,
             'raticate': 116, 'spearow': 58, 'fearow': 162, 'ekans': 62,
             'arbok': 147, 'pikachu': 82, 'raichu': 122, 'sandshrew': 93,
             'sandslash': 163, 'nidoran♀': 59, 'nidorina': 117,
             'nidoqueen': 194, 'nidoran♂': 60, 'nidorino':118, 'nidoking': 195,
             'clefairy': 68,'clefable': 129, 'vulpix': 63, 'ninetails': 178,
             'jigglypuff': 76, 'wigglytuff': 109, 'zubat': 54, 'golbat': 171,
             'oddish': 78, 'gloom': 132, 'vileplume': 184, 'paras': 70,
             'parasect': 128, 'venonat': 75, 'venomoth': 138, 'diglett': 81,
             'dugtrio': 153, 'meowth': 69, 'persian': 148, 'psyduck': 80,
             'golduck': 174, 'mankey': 74, 'primeape': 149, 'growlithe': 91,
             'arcanine': 213, 'poliwag': 77, 'poliwhirl': 131, 'poliwrath': 185,
             'abra': 73, 'kadabra': 145, 'alakazam': 186, 'machop': 88,
             'machoke': 146, 'machamp': 193, 'bellsprout': 84,
             'weepinbell': 151, 'victreebel': 191, 'tentacool': 105,
             'tentacruel': 205, 'geodude': 86, 'graveler': 134, 'golem': 177,
             'ponyta': 152, 'rapidash': 192, 'slowpoke': 99, 'slowbro': 164,
             'magnemite': 89, 'magneton': 161, "farfetch'd": 94, 'doduo': 96,
             'dodrio': 158, 'seel': 100, 'dewgong': 176, 'grimer': 90,
             'muk': 157, 'shellder': 97, 'cloyster': 203, 'gastly': 95,
             'haunter': 126, 'gengar': 190, 'onix': 108, 'drowzee': 102,
             'hypno': 165, 'krabby': 115, 'kingler': 206, 'voltorb': 103,
             'electrode': 150, 'exeggcute': 98, 'exeggutor': 212, 'cubone': 87,
             'marowak': 124, 'hitmonlee': 139, 'hitmonchan': 140,
             'lickitung': 127, 'koffing': 114, 'weezing': 173, 'rhyhorn': 135,
             'rhydon': 204, 'chansey': 255, 'tangela': 166, 'kangaskhan': 175,
             'horsea': 83, 'seadra': 155, 'goldeen': 111, 'seaking': 170,
             'staryu': 106, 'starmie': 207, 'mr. mime': 136, 'scyther': 187,
             'jynx': 137, 'electabuzz': 156, 'magmar': 167, 'pinsir': 200,
             'tauros': 211, 'magikarp': 20, 'gyarados': 214, 'lapras': 219,
             'ditto': 61, 'eevee': 92, 'vaporeon': 196, 'jolteon': 197,
             'flareon': 198, 'porygon': 130, 'omanyte': 120, 'lord helix': 120,
             'omastar': 199, 'kabuto': 119, 'kabutops': 201, 'aerodactyl': 202,
             'snorlax': 154, 'articuno': 215, 'zapdos': 216, 'moltres': 217,
             'dratini': 67, 'dragonair': 144, 'dragonite': 218, 'mewtwo': 220,
             'mew': 64}
gen2Update = {'chikorita': 64, 'bayleef': 141, 'meganium': 208, 'cyndaquil': 65,
             'quilava': 142, 'typhlosion': 209, 'totodile': 66, 'croconaw': 143,
             'feraligatr': 210, 'sentret': 57, 'furret': 116, 'hoothoot': 58,
             'noctowl': 162, 'ledyba': 54, 'ledian': 134, 'spinarak': 54,
             'ariados': 134, 'crobat': 204, 'chinchou': 90, 'lanturn': 156,
             'pichu': 42, 'cleffa': 37, 'igglybuff': 39, 'togepi': 74,
             'togetic': 114, 'natu': 73, 'xatu': 171, 'mareep': 59,
             'flaaffy': 117, 'ampharos': 194, 'bellossom': 184, 'marill': 58,
             'azumarill': 153, 'sudowoodo': 135, 'politoed': 185, 'hoppip': 74,
             'skiploom': 136, 'jumpluff': 176, 'aipom': 94, 'sunkern': 52,
             'sunflora': 146, 'yanma': 147, 'wooper': 52, 'quagsire': 137,
             'espeon': 197, 'umbreon': 197, 'murkrow': 107, 'slowking': 164,
             'misdreavus': 147, 'unown': 61, 'wobbuffet': 177, 'girafarig': 149,
             'pineco': 60, 'forretress': 118, 'dunsparce': 75, 'gligar': 108,
             'steelix': 196, 'snubbull': 63, 'granbull': 178, 'quilfish': 100,
             'scizor': 200, 'shuckle': 80, 'heracross': 200, 'sneasel': 132,
             'teddiursa': 124, 'ursaring': 189, 'slugma': 78, 'magcargo': 154,
             'swinub': 78, 'piloswine': 160, 'corsola': 113, 'remoraid': 78,
             'octillery': 164, 'delibird': 183, 'mantine': 168, 'skarmory': 168,
             'houndour': 114, 'houndoom': 204, 'kingdra': 207, 'phanpy': 124,
             'donphan': 189, 'porygon2': 180, 'stantler': 165, 'smeargle': 106,
             'tyrogue': 91, 'hitmontop': 138, 'smoochum': 87, 'elekid': 106,
             'magby': 117, 'miltank': 200, 'blissey': 255, 'raikou': 216,
             'entei': 217, 'suicune': 215, 'larvitar': 67, 'pupitar': 114,
             'tyranitar': 218, 'lugia': 220, 'ho-oh': 220, 'celebi': 64}
gen2Yield = gen1Yield | gen2Update
gen3Update = {'treeko': 65, 'grovyle': 141, 'sceptile': 208, 'torchic': 65, 
              'combusken': 142, 'blaziken': 209, 'mudkip': 65, 'marshtomp': 143,
              'swampert': 210, 'poochyena': 55, 'mightyena': 128,
              'zigzagoon': 60, 'linoone': 128, 'wurmple': 54, 'silcoon': 71,
              'beautifly': 161, 'cascoon': 72, 'dustox': 160, 'lotad': 74,
              'lombre': 141, 'ludicolo': 181, 'seedot': 74, 'nuzleaf': 141,
              'shiftry': 181, 'taillow': 59, 'swellow': 162, 'wingull': 64,
              'pelipper': 164, 'ralts': 70, 'kirlia': 140, 'gardevoir': 208,
              'surskit': 63, 'masquerain': 128, 'shroomish': 65, 'breloom': 165,
              'slakoth': 83, 'vigoroth': 126, 'slaking': 210, 'nincada': 65,
              'ninjask': 155, 'shedinja': 95, 'whismur': 68, 'loudred': 126,
              'exploud': 184, 'makuhita': 87, 'hariyama': 184, 'azurill': 33,
              'nosepass': 108, 'skitty': 65, 'delcatty': 138, 'sableye': 98,
              'mawile': 98, 'aron': 96, 'lairon': 152, 'aggron': 205,
              'meditite': 91, 'medicham': 153, 'electrike': 104,
              'manectric': 168, 'plusle': 120, 'minun': 120, 'volbeat': 146,
              'illumise': 146, 'roselia': 152, 'gulpin': 75, 'swalot': 168,
              'carvanha': 88, 'sharpedo': 175, 'wailmer': 137, 'wailord': 206,
              'numel': 88, 'camerupt': 175, 'torkoal': 161, 'spoink': 89,
              'grumpig': 164, 'spinda': 85, 'trapinch': 73, 'vibrava': 126,
              'flygon': 197, 'cacnea': 97, 'cacturne': 177, 'swablu': 74,
              'altaria': 188, 'zangoose': 165, 'seviper': 165, 'lunatone': 150,
              'solrock': 150, 'barboach': 92, 'whishcash': 158, 'corphish': 111,
              'crawdaunt': 161, 'baltoy': 58, 'claydol': 189, 'lileep': 121,
              'cradily': 201, 'anorith': 119, 'armaldo': 200, 'feebas': 61,
              'milotic': 213, 'castform': 145, 'kecleon': 132, 'shuppet': 97,
              'banette': 179, 'duskull': 97, 'dusclops': 179, 'tropius': 169,
              'chimecho': 147, 'absol': 174, 'wynaut': 44, 'snorunt': 74,
              'glalie': 187, 'spheal': 75, 'sealeo': 128, 'walrein': 192,
              'clamperl': 142, 'huntail': 178, 'gorebyss': 178,
              'relicanth': 198, 'luvdisc': 110, 'bagon': 89, 'shelgon': 144,
              'salamence': 218, 'beldum': 103, 'metang': 153, 'metagross': 210,
              'regirock': 217, 'regice': 216, 'registeel': 215, 'latias': 211,
              'latios': 211, 'kyogre': 218, 'groudon': 218, 'rayquaza': 220,
              'jirachi': 215, 'deoxys': 215}
gen3Yield = gen2Yield | gen3Update
gen4Update = {'turtwig': 64, 'grotle': 141, 'torterra': 208, 'chimchar': 65,
             'monferno': 142, 'infernape': 209, 'piplup': 66, 'prinplup': 143,
             'empoleon': 210, 'starly': 56, 'staravia': 113, 'staraptor': 172,
             'bidoof': 58, 'bibarel': 116, 'kricketot': 54, 'kricketune': 159,
             'shinx': 60, 'luxio': 117, 'luxray': 194, 'budew': 68,
             'roserade': 204, 'cranidos': 99, 'rampardos': 199, 'shieldon': 99,
             'bastiodon': 199, 'burmy': 61, 'wormadam': 159, 'mothim': 159,
             'combee': 63, 'vespiquen': 188, 'patchirisu': 120, 'buizel': 75,
             'floatzel': 178, 'cherubi': 68, 'cherrim': 133, 'shellos': 73,
             'gastrodon': 176, 'ambipom': 186, 'drifloon': 127, 'drifblim': 204,
             'buneary': 84, 'lopunny': 178, 'mismagius': 187, 'honchkrow': 187,
             'glameow': 71, 'purugly': 183, 'chingling': 74, 'stunky': 79,
             'skuntank': 209, 'bronor': 72, 'bronzong': 188, 'bonsly': 68,
             'mime jr.': 78, 'happiny': 255, 'chatot': 107, 'spiritomb': 168,
             'gible': 67, 'gabite': 144, 'garchomp': 218, 'munchlax': 94,
             'riolu': 72, 'lucario': 204, 'hippopotas': 95, 'hippowdon': 198,
             'skorupi': 114, 'drapion': 204, 'croagunk': 83, 'toxicroak': 181,
             'carnivine': 164, 'finneon': 90, 'lumineon': 156, 'mantyke': 108,
             'snover': 131, 'abomasnow': 214, 'weavile': 199, 'magnezone': 211, 
             'lickilicky': 193, 'rhyperior': 217, 'tangrowth': 211,
             'electivire': 199, 'magmortar': 199, 'togekiss': 220,
             'yanmega': 198, 'leafeon': 196, 'glaceon': 196, 'gliscor': 192,
             'mamoswine': 207, 'porygon-z': 185, 'gallade': 208,
             'probopass': 198, 'dusknoir': 210, 'froslass': 187, 'rotom': 132,
             'uxie': 210, 'mespirit': 210, 'azelf': 210, 'dialga': 220,
             'palkia': 220, 'heatran': 215, 'regigigas': 220, 'giratina': 220,
             'cresselia': 210, 'phione': 165, 'manaphy': 215, 'darkrai': 210,
             'shaymin': 64, 'arceus': 255, 
             # ↓↓↓ Updates over previous generations ↓↓↓
             'abra': 75, 'machop': 75, 'geodude': 73, 'omanyte': 99,
             'kabuto': 99, 'kabutops': 199, 'dunsparce': 125, 'silcoon': 72,
             'dustox': 161, 'lileep': 99, 'cradily': 199, 'anorith': 99,
             'armaldo': 99}
gen4Yield = gen3Yield | gen4Update

# Create main window
root = tk.Tk()
root.title("EXP Calculator")
root.resizable(False, False)
#root.iconbitmap('./pokeball.ico')

# Return values from UI
pokemon = tk.StringVar()
pokemon.set("Bulbasaur")

trainer = tk.BooleanVar()

egg = tk.BooleanVar()

ot = tk.BooleanVar()

expShare = tk.BooleanVar()

level = tk.IntVar()
level.set(50)

number = tk.IntVar()
number.set(1)

holdingShare = tk.IntVar()
holdingShare.set(0)

shareGate = tk.DISABLED

generation = tk.IntVar()
generation.set(3)

generations = (('Gen 1', 1),
               ('Gen 2', 2),
               ('Gen 3', 3),
               ('Gen 4', 4),
               ('Gen 5', 5),
               ('Gen 6', 6),
               ('Gen 7', 7),
               ('Gen 8', 8),
               ('Gen 9', 9))


# Create container frames
generationLabelFrame = ttk.LabelFrame(root, text = "Generation")
generationLabelFrame.pack(padx = 20, pady = 10, fill = 'x')

opponentLabelFrame = ttk.LabelFrame(root, text = "Opponent Pokemon")
opponentLabelFrame.pack(padx = 20, pady = 10, fill = 'x')

yourLabelFrame = ttk.LabelFrame(root, text = "Your Pokemon")
yourLabelFrame.pack(padx = 20, pady = 10, fill = 'x')

generationFrame = ttk.Frame(generationLabelFrame)
generationFrame.pack(padx = 10, pady = 10, fill = "x")

pokemonFrame = ttk.Frame(opponentLabelFrame)
pokemonFrame.pack(padx = 10, pady = 10, fill = "x")

defeatedFrame = ttk.Frame(opponentLabelFrame)
defeatedFrame.pack(padx = 10, pady = 10, fill = "x")

checkboxFrame = ttk.Frame(yourLabelFrame)
checkboxFrame.pack(padx = 10, pady = 10, fill = "x")

numberFrame = ttk.Frame(yourLabelFrame)
numberFrame.pack(padx = 10, pady = 10)

bottomFrame = ttk.Frame(root)
bottomFrame.pack(padx = 10, pady = 10, fill = "x")

# Generation Frame
i = 0
for gen in generations:
    r = ttk.Radiobutton(
        generationFrame,
        text = gen[0],
        value = gen[1],
        variable = generation)
    r.grid(column = i, row = 0, padx = 5, pady = 5)
    i += 1

# Pokemon frame
pokemonLabel = ttk.Label(pokemonFrame, text = "Pokemon: ")
pokemonLabel.pack()

pokemonBox = ttk.Combobox(pokemonFrame, textvariable = pokemon)
gen3Names = []
for key in gen3Yield.keys():
    gen3Names.append(key.capitalize())
pokemonBox['values'] = [gen3Names[i] for i in range(0, len(gen3Names))]
pokemonBox['state'] = 'readonly'
pokemonBox.pack()

# Defeated frame
levelDisplay = ttk.Label(defeatedFrame,
                         text = "Opponent's Level: 50")
levelDisplay.pack()

levelSlider = ttk.Scale(defeatedFrame,
                        from_ = 1,
                        to = 100,
                        orient = 'horizontal',
                        variable = level,
                        command = levelChanged)
levelSlider.pack(fill = 'x', side = 'bottom')

# Checkbox frame
ttk.Checkbutton(checkboxFrame, 
                text = "Trainer Battle",
                variable = trainer,
                onvalue = True,
                offvalue = False
).grid(column = 0, row = 0)

ttk.Checkbutton(checkboxFrame, 
                text = "Lucky Egg",
                variable = egg,
                onvalue = True,
                offvalue = False
).grid(column = 1, row = 0)

ttk.Checkbutton(checkboxFrame, 
                text = "Original Trainer",
                variable = ot,
                onvalue = True,
                offvalue = False
).grid(column = 2, row = 0)

ttk.Checkbutton(checkboxFrame, 
                text = "EXP Share",
                variable = expShare,
                onvalue = True,
                offvalue = False,
                command = shareNumberUpdate
).grid(column = 3, row = 0)

numberLabel = ttk.Label(numberFrame, text = "Number that battled: ")
numberLabel.pack(side = 'left')

pokemonNumber = ttk.Spinbox(numberFrame,
                            from_ = 1,
                            to = 6,
                            values = (1, 2, 3, 4, 5, 6),
                            textvariable = number,
                            wrap = True,
                            width = 3)
pokemonNumber.pack(side = 'left')

shareLabel = ttk.Label(numberFrame, text = "Number that held exp share: ")
shareLabel.pack(side = 'left')

shareNumber = ttk.Spinbox(numberFrame,
                            from_ = 0,
                            to = 6,
                            values = (0),
                            textvariable = holdingShare,
                            wrap = True,
                            width = 3,
                            state = shareGate)
shareNumber.pack(side = 'left')

# bottom frame
goButton = ttk.Button(bottomFrame, text="Go", command=go)
goButton.pack()

resultLabel = ttk.Label(bottomFrame)
resultLabel.pack(side = 'bottom')

root.mainloop()