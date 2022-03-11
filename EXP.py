# Pokemon Experience Gain Calculator V1
# Update to Python 3.9 dipshit
# https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-taking-union-of-dictiona
# Kirk Rieberger
from math import floor
from sys import exit
# Dictionaries containing the exp values for each Pokemon
gen1Yield = {}
gen2Yield = {}
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
gen4Updates = {'turtwig': 64, 'grotle': 141, 'torterra': 208, 'chimchar': 65,
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
             'shaymin': 64, 'arceus': 255, 'abra': 75, 'machop': 75,
             'geodude': 73, 'omanyte': 99, 'kabuto': 99, 'kabutops': 199,
             'dunsparce': 125, 'silcoon': 72, 'dustox': 161, 'lileep': 99,
             'cradily': 199, 'anorith': 99, 'armaldo': 99}
gen4Yield = gen3Yield | gen4Updates
gen5Yield = {}
gen6Yield = {}
gen7Yield = {}

def genOne():
    for key in gen4Yield:
        print(key, gen4Yield[key])
    return 0

def genTwo():
    return 0

def genThree():
    a = input('Was this a trainer battle?(y/n): ').lower()
    if a == 'y':
        a = 1.5
    else:
        a = 1

    b = input('Pokemon that was battled: ').lower()
    while b not in gen3Yield:
        print('Please enter a valid generation 3 Pokemon name.')
        b = input('Pokemon that was battled: ').lower()
    b = gen3Yield[b]

    e = input('Is your Pokemon holding a Lucky Egg?(y/n): ').lower()
    if e == 'y':
        e = 1.5
    else:
        e = 1

    while True:
        try:
            L = int(input('Level of defeated Pokemon: '))
            while L < 1 or L > 100:
                print('Pokemon level must be between 1 and 100 inclusive.')
                L = int(input('Level of defeated Pokemon: '))
            break
        except ValueError:
            print('Please enter a valid level from 1 to 100 inclusive.')

    s = input('Are any of your Pokemon holding EXP Shares?(y/n): ').lower()
    if s == 'y':
        s = 2*int(input('How many of your Pokemon participated in battle? '))
        while s < 1 or s > 6:
            print("Number of Pokemon that battled must be between 1 and 6 inclusive.")
            s = 2*int(input('How many of your Pokemon participated in battle? '))
    else:
        s = int(input('How many of your Pokemon participated in battle? '))
        while s < 1 or s > 6:
            print("Number of Pokemon that battled must be between 1 and 6 inclusive.")
            s = int(input('How many of your Pokemon participated in battle? '))

    t = input("Are you the battling Pokemon's original trainer?(y/n): ").lower()
    if t == 'y':
        t = 1
    else:
        t = 1.5

    exp = (a*t*b*e*L)/(7*s)

    return floor(exp)

def genFour():
    return 0

def genFive():
    return 0

def genSix():
    return 0

def genSeven():
    return 0


run = 1
while run:
    print("Generation 3 experience points gained: ", genThree(), "\n")
    again = input('Again?(y/n): ').lower()
    if again == 'n':
        exit(0)
    #genOne()
    break

def getMax():
# Print key with highest value
    allValues = gen3Yield.values()
    print(max(gen3Yield, key=gen3Yield.get), max(allValues))
