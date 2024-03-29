# EXP.py - A program to create lists of Pokemon names and base EXP values.
# Copyright (C) 2023 Kirk Rieberger
# Issued under GPLv2 or later
# See LICENCE.txt for full license
# Last updated May 17, 2023

from math import floor
from sys import exit

# TODO: Add file based calculation/batch calculation
# TODO: Try sys.version_info to enforce Python 3.9+

# Dictionaries containing the exp values for each Pokemon
# Pokemon Red/Blue/Green/Yellow
gen1Yield = {'bulbasaur': 64, 'ivysaur': 141, 'venusaur': 208, 'charmander': 65,
             'charmeleon': 142, 'charizard': 209, 'sqirtle': 66,
             'wartortle': 143, 'blastoise': 210, 'caterpie': 53, 'metapod': 72,
             'butterfree': 160, 'weedle': 52, 'kakuna': 71, 'beedrill': 159,
             'pidgey': 55, 'pidgeotto': 113, 'pidgeot': 172, 'rattata': 57,
             'raticate': 116, 'spearow': 58, 'fearow': 162, 'ekans': 62,
             'arbok': 147, 'pikachu': 82, 'raichu': 122, 'sandshrew': 93,
             'sandslash': 163, 'nidoran♀': 59, 'nidorina': 117,
             'nidoqueen': 194, 'nidoran♂': 60, 'nidorino': 118, 'nidoking': 195,
             'clefairy': 68, 'clefable': 129, 'vulpix': 63, 'ninetails': 178,
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
# Pokemon Gold/Silver/Crystal
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
# Pokemon Ruby/Sapphire/Emerald/Fire Red/Leaf Green
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
# Pokemon Diamond/Pearl/Platinum/Heart Gold/Soul Silver
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
              'shaymin': 64, 'arceus': 255, 'abra': 75, 'machop': 75,
              'geodude': 73, 'omanyte': 99, 'kabuto': 99, 'kabutops': 199,
              'dunsparce': 125, 'silcoon': 72, 'dustox': 161, 'lileep': 99,
              'cradily': 199, 'anorith': 99, 'armaldo': 99}
gen4Yield = gen3Yield | gen4Update
# Pokemon Black/White/Black 2/White 2
gen5Yield = {'bulbasaur': 64, 'ivysaur': 142, 'venusaur': 236, 'charmander': 62,
             'charmeleon': 142, 'charizard': 240, 'sqirtle': 63,
             'wartortle': 142, 'blastoise': 239, 'caterpie': 39, 'metapod': 72,
             'butterfree': 173, 'weedle': 39, 'kakuna': 72, 'beedrill': 173,
             'pidgey': 50, 'pidgeotto': 122, 'pidgeot': 211, 'rattata': 51,
             'raticate': 145, 'spearow': 52, 'fearow': 155, 'ekans': 58,
             'arbok': 153, 'pikachu': 105, 'raichu': 214, 'sandshrew': 60,
             'sandslash': 159, 'nidoran♀': 55, 'nidorina': 128,
             'nidoqueen': 223, 'nidoran♂': 55, 'nidorino': 128, 'nidoking': 223,
             'clefairy': 113, 'clefable': 213, 'vulpix': 60, 'ninetails': 177,
             'jigglypuff': 95, 'wigglytuff': 191, 'zubat': 49, 'golbat': 159,
             'oddish': 64, 'gloom': 138, 'vileplume': 216, 'paras': 57,
             'parasect': 142, 'venonat': 61, 'venomoth': 158, 'diglett': 53,
             'dugtrio': 142, 'meowth': 58, 'persian': 154, 'psyduck': 64,
             'golduck': 175, 'mankey': 61, 'primeape': 159, 'growlithe': 70,
             'arcanine': 194, 'poliwag': 60, 'poliwhirl': 135, 'poliwrath': 225,
             'abra': 62, 'kadabra': 140, 'alakazam': 221, 'machop': 61,
             'machoke': 142, 'machamp': 227, 'bellsprout': 60,
             'weepinbell': 137, 'victreebel': 216, 'tentacool': 67,
             'tentacruel': 180, 'geodude': 60, 'graveler': 137, 'golem': 218,
             'ponyta': 82, 'rapidash': 175, 'slowpoke': 63, 'slowbro': 172,
             'magnemite': 65, 'magneton': 163, "farfetch'd": 123, 'doduo': 62,
             'dodrio': 161, 'seel': 65, 'dewgong': 166, 'grimer': 65,
             'muk': 175, 'shellder': 61, 'cloyster': 184, 'gastly': 62,
             'haunter': 142, 'gengar': 225, 'onix': 77, 'drowzee': 66,
             'hypno': 169, 'krabby': 65, 'kingler': 166, 'voltorb': 66,
             'electrode': 168, 'exeggcute': 65, 'exeggutor': 182, 'cubone': 64,
             'marowak': 149, 'hitmonlee': 159, 'hitmonchan': 159,
             'lickitung': 77, 'koffing': 68, 'weezing': 172, 'rhyhorn': 69,
             'rhydon': 170, 'chansey': 395, 'tangela': 87, 'kangaskhan': 172,
             'horsea': 59, 'seadra': 154, 'goldeen': 64, 'seaking': 158,
             'staryu': 68, 'starmie': 182, 'mr. mime': 161, 'scyther': 100,
             'jynx': 159, 'electabuzz': 172, 'magmar': 173, 'pinsir': 175,
             'tauros': 172, 'magikarp': 40, 'gyarados': 189, 'lapras': 187,
             'ditto': 101, 'eevee': 65, 'vaporeon': 184, 'jolteon': 184,
             'flareon': 184, 'porygon': 79, 'omanyte': 71, 'lord helix': 71,
             'omastar': 173, 'kabuto': 71, 'kabutops': 173, 'aerodactyl': 180,
             'snorlax': 189, 'articuno': 261, 'zapdos': 261, 'moltres': 261,
             'dratini': 60, 'dragonair': 147, 'dragonite': 270, 'mewtwo': 306,
             'mew': 270, 'chikorita': 64, 'bayleef': 142, 'meganium': 236,
             'cyndaquil': 62, 'quilava': 142, 'typhlosion': 240, 'totodile': 63,
             'croconaw': 142, 'feraligatr': 239, 'sentret': 43, 'furret': 145,
             'hoothoot': 52, 'noctowl': 155, 'ledyba': 53, 'ledian': 137,
             'spinarak': 50, 'ariados': 137, 'crobat': 241, 'chinchou': 66,
             'lanturn': 161, 'pichu': 41, 'cleffa': 44, 'igglybuff': 42,
             'togepi': 49, 'togetic': 142, 'natu': 64, 'xatu': 165,
             'mareep': 56, 'flaaffy': 128, 'ampharos': 225, 'bellossom': 216,
             'marill': 88, 'azumarill': 185, 'sudowoodo': 144, 'politoed': 225,
             'hoppip': 50, 'skiploom': 119, 'jumpluff': 203, 'aipom': 72,
             'sunkern': 36, 'sunflora': 149, 'yanma': 78, 'wooper': 42,
             'quagsire': 151, 'espeon': 184, 'umbreon': 184, 'murkrow': 81,
             'slowking': 172, 'misdreavus': 87, 'unown': 118, 'wobbuffet': 142,
             'girafarig': 159, 'pineco': 58, 'forretress': 163,
             'dunsparce': 145, 'gligar': 86, 'steelix': 179, 'snubbull': 60,
             'granbull': 158, 'quilfish': 158, 'scizor': 175, 'shuckle': 177,
             'heracross': 175, 'sneasel': 86, 'teddiursa': 66, 'ursaring': 175,
             'slugma': 50, 'magcargo': 144, 'swinub': 50, 'piloswine': 158,
             'corsola': 133, 'remoraid': 60, 'octillery': 168, 'delibird': 116,
             'mantine': 163, 'skarmory': 163, 'houndour': 66, 'houndoom': 175,
             'kingdra': 243, 'phanpy': 66, 'donphan': 175, 'porygon2': 180,
             'stantler': 163, 'smeargle': 88, 'tyrogue': 42, 'hitmontop': 159,
             'smoochum': 61, 'elekid': 72, 'magby': 73, 'miltank': 172,
             'blissey': 608, 'raikou': 261, 'entei': 261, 'suicune': 261,
             'larvitar': 60, 'pupitar': 144, 'tyranitar': 270, 'lugia': 306,
             'ho-oh': 306, 'celebi': 270, 'treeko': 62, 'grovyle': 142,
             'sceptile': 239, 'torchic': 62, 'combusken': 142, 'blaziken': 239,
             'mudkip': 62, 'marshtomp': 142, 'swampert': 241, 'poochyena': 44,
             'mightyena': 147, 'zigzagoon': 48, 'linoone': 147, 'wurmple': 39,
             'silcoon': 72, 'beautifly': 173, 'cascoon': 41, 'dustox': 135,
             'lotad': 44, 'lombre': 119, 'ludicolo': 216, 'seedot': 44,
             'nuzleaf': 119, 'shiftry': 216, 'taillow': 54, 'swellow': 151,
             'wingull': 54, 'pelipper': 151, 'ralts': 40, 'kirlia': 97,
             'gardevoir': 233, 'surskit': 54, 'masquerain': 145,
             'shroomish': 59, 'breloom': 161, 'slakoth': 56, 'vigoroth': 154,
             'slaking': 252, 'nincada': 53, 'ninjask': 160, 'shedinja': 83,
             'whismur': 48, 'loudred': 126, 'exploud': 216, 'makuhita': 47,
             'hariyama': 166, 'azurill': 38, 'nosepass': 75, 'skitty': 52,
             'delcatty': 133, 'sableye': 133, 'mawile': 133, 'aron': 66,
             'lairon': 151, 'aggron': 239, 'meditite': 56, 'medicham': 144,
             'electrike': 59, 'manectric': 166, 'plusle': 142, 'minun': 142,
             'volbeat': 140, 'illumise': 140, 'roselia': 140, 'gulpin': 60,
             'swalot': 163, 'carvanha': 61, 'sharpedo': 161, 'wailmer': 80,
             'wailord': 175, 'numel': 61, 'camerupt': 161, 'torkoal': 165,
             'spoink': 66, 'grumpig': 165, 'spinda': 126, 'trapinch': 58,
             'vibrava': 119, 'flygon': 234, 'cacnea': 67, 'cacturne': 166,
             'swablu': 62, 'altaria': 172, 'zangoose': 160, 'seviper': 160,
             'lunatone': 154, 'solrock': 154, 'barboach': 58, 'whishcash': 164,
             'corphish': 62, 'crawdaunt': 164, 'baltoy': 60, 'claydol': 175,
             'lileep': 71, 'cradily': 173, 'anorith': 71, 'armaldo': 173,
             'feebas': 40, 'milotic': 189, 'castform': 147, 'kecleon': 154,
             'shuppet': 59, 'banette': 159, 'duskull': 59, 'dusclops': 159,
             'tropius': 161, 'chimecho': 149, 'absol': 163, 'wynaut': 52,
             'snorunt': 60, 'glalie': 168, 'spheal': 58, 'sealeo': 144,
             'walrein': 239, 'clamperl': 69, 'huntail': 170, 'gorebyss': 170,
             'relicanth': 170, 'luvdisc': 116, 'bagon': 60, 'shelgon': 147,
             'salamence': 270, 'beldum': 60, 'metang': 147, 'metagross': 270,
             'regirock': 261, 'regice': 261, 'registeel': 261, 'latias': 270,
             'latios': 270, 'kyogre': 302, 'groudon': 302, 'rayquaza': 306,
             'jirachi': 270, 'deoxys': 270, 'turtwig': 64, 'grotle': 142,
             'torterra': 236, 'chimchar': 62, 'monferno': 142, 'infernape': 240,
             'piplup': 63, 'prinplup': 142, 'empoleon': 239, 'starly': 49,
             'staravia': 119, 'staraptor': 214, 'bidoof': 50, 'bibarel': 144,
             'kricketot': 39, 'kricketune': 134, 'shinx': 53, 'luxio': 127,
             'luxray': 235, 'budew': 56, 'roserade': 227, 'cranidos': 70,
             'rampardos': 173, 'shieldon': 70, 'bastiodon': 173, 'burmy': 45,
             'wormadam': 148, 'mothim': 148, 'combee': 49, 'vespiquen': 166,
             'patchirisu': 142, 'buizel': 66, 'floatzel': 173, 'cherubi': 55,
             'cherrim': 158, 'shellos': 65, 'gastrodon': 166, 'ambipom': 169,
             'drifloon': 70, 'drifblim': 174, 'buneary': 70, 'lopunny': 168,
             'mismagius': 173, 'honchkrow': 177, 'glameow': 62, 'purugly': 158,
             'chingling': 57, 'stunky': 66, 'skuntank': 168, 'bronor': 60,
             'bronzong': 175, 'bonsly': 58, 'mime jr.': 62, 'happiny': 110,
             'chatot': 144, 'spiritomb': 170, 'gible': 60, 'gabite': 144,
             'garchomp': 270, 'munchlax': 78, 'riolu': 57, 'lucario': 184,
             'hippopotas': 66, 'hippowdon': 184, 'skorupi': 66, 'drapion': 175,
             'croagunk': 60, 'toxicroak': 172, 'carnivine': 159, 'finneon': 66,
             'lumineon': 161, 'mantyke': 69, 'snover': 67, 'abomasnow': 173,
             'weavile': 179, 'magnezone': 241, 'lickilicky': 180,
             'rhyperior': 241, 'tangrowth': 187, 'electivire': 243,
             'magmortar': 243, 'togekiss': 245, 'yanmega': 180, 'leafeon': 184,
             'glaceon': 184, 'gliscor': 179, 'mamoswine': 239, 'porygon-z': 241,
             'gallade': 233, 'probopass': 184, 'dusknoir': 236, 'froslass': 168,
             'rotom': 154, 'uxie': 261, 'mespirit': 261, 'azelf': 261,
             'dialga': 306, 'palkia': 306, 'heatran': 270, 'regigigas': 302,
             'giratina': 306, 'cresselia': 270, 'phione': 216, 'manaphy': 270,
             'darkrai': 270, 'shaymin': 270, 'arceus': 324, 'victini': 270,
             'snivy': 62, 'servine': 145, 'serperior': 238, 'tepig': 62,
             'pignite': 146, 'emboar': 238, 'oshawott': 62, 'dewott': 145,
             'samurott': 238, 'patrat': 51, 'watchog': 147, 'lillipup': 55,
             'herdier': 130, 'stoutland': 211, 'purrloin': 56, 'liepard': 156,
             'pansage': 63, 'simisage': 174, 'pansear': 63, 'simisear': 174,
             'panpour': 63, 'simipour': 174, 'munna': 58, 'musharna': 170,
             'pidove': 53, 'tranquill': 125, 'unfezant': 215, 'blitzle': 59,
             'zebstrika': 174, 'roggenrola': 56, 'boldore': 137,
             'gigalith': 227, 'woobat': 63, 'swoobat': 149, 'drilbur': 66,
             'excadrill': 178, 'audino': 390, 'timburr': 61, 'gurdurr': 142,
             'conkeldurr': 227, 'tympole': 59, 'palpitoad': 134,
             'seismitoad': 225, 'throh': 163, 'sawk': 163, 'sewaddle': 62,
             'swadloon': 133, 'leavanny': 221, 'venipede': 52,
             'whirlipede': 126, 'scolipede': 214, 'cottonee': 56,
             'whimsicott': 168, 'petilil': 56, 'lilligant': 168,
             'basculin': 161, 'sandile': 58, 'krokorok': 123, 'krookodile': 229,
             'darumaka': 63, 'darmanitan': 168, 'maractus': 161, 'dwebble': 65,
             'crustle': 166, 'scraggy': 70, 'scrafty': 171, 'sigilyph': 172,
             'yamask': 61, 'cofagrigus': 169, 'tirtouga': 71, 'carracosta': 173,
             'archen': 71, 'archeops': 177, 'trubbish': 66, 'garbodor': 166,
             'zorua': 66, 'zoroark': 179, 'minccino': 60, 'cinccino': 165,
             'gothita': 58, 'gothorita': 137, 'gothitelle': 221, 'solosis': 58,
             'duosion': 130, 'reuniclus': 221, 'ducklett': 61, 'swanna': 166,
             'vanillite': 61, 'vanillish': 138, 'vanilluxe': 214,
             'deerling': 67, 'sawsbuck': 166, 'emolga': 150, 'karrablast': 63,
             'escavalier': 173, 'foongus': 59, 'amoonguss': 162, 'frillish': 67,
             'jellicent': 168, 'alomomola': 165, 'joltik': 64,
             'galvantula': 165, 'ferroseed': 61, 'ferrothorn': 171, 'klink': 60,
             'klang': 154, 'klinklang': 234, 'tynamo': 55, 'eelektrik': 142,
             'eelektross': 232, 'elgyem': 67, 'beheeyem': 170, 'litwick': 55,
             'lampent': 130, 'chandelure': 234, 'axew': 64, 'fraxure': 144,
             'haxorus': 243, 'cubchoo': 61, 'beartic': 170, 'cryogonal': 170,
             'shelmet': 61, 'accelgor': 173, 'stunfisk': 165, 'mienfoo': 70,
             'mienshao': 179, 'druddigon': 170, 'golett': 61, 'golurk': 169,
             'pawniard': 68, 'bisharp': 172, 'bouffalant': 172, 'rufflet': 70,
             'braviary': 179, 'vullaby': 74, 'mandibuzz': 179, 'heatmor': 169,
             'durant': 169, 'deino': 60, 'zweilous': 147, 'hydreigon': 270,
             'larvesta': 72, 'volcorona': 248, 'cobalion': 261,
             'terrakion': 261, 'virizion': 261, 'tornadus': 261,
             'thundurus': 261, 'reshiram': 306, 'zekrom': 306, 'landorus': 270,
             'kyurem': 297, 'keldeo': 261, 'meloetta': 270, 'genesect': 270}
# TODO: Megas have a different EXP yield from base forms
# Pokemon X/Y/Omega Ruby/Alpha Sapphire
gen6Update = {'chespin': 63, 'quilladin': 162, 'chesnaught': 239,
              'fennekin': 61, 'braixen': 143, 'delphox': 240, 'froakie': 63,
              'frogadier': 142, 'greninja': 239, 'bunnelby': 47,
              'diggersby': 148, 'fletchling': 56, 'fletchinder': 134,
              'talonflame': 175, 'scatterbug': 40, 'spewpa': 75,
              'vivillon': 185, 'litleo': 74, 'pyroar': 177, 'flabébé': 61,
              'floette': 130, 'florges': 248, 'skiddo': 70, 'gogoat': 186,
              'pancham': 70, 'pangoro': 173, 'furfrou': 165, 'espurr': 71,
              'meowstic': 163, 'honedge': 65, 'doublade': 157, 'aegislash': 234,
              'spritzee': 68, 'aromatisse': 162, 'swirlix': 68, 'slurpuff': 168,
              'inkay': 58, 'malamar': 169, 'binacle': 61, 'barbaracle': 175,
              'skrelp': 64, 'dragalge': 173, 'clauncher': 66, 'clawitzer': 100,
              'helioptile': 58, 'heliolisk': 168, 'tyrunt': 72,
              'tyrantrum': 182, 'amaura': 72, 'aurorus': 104, 'sylveon': 184,
              'hawlucha': 175, 'dedenne': 151, 'carbink': 100, 'goomy': 60,
              'sliggoo': 158, 'goodra': 270, 'klefki': 165, 'phantump': 62,
              'trevenant': 166, 'pumpkaboo': 67, 'gourgeist': 173,
              'bergmite': 61, 'avalugg': 180, 'noibat': 49, 'noivern': 187,
              'xerneas': 306, 'yveltal': 306, 'zygarde': 270, 'diancie': 270,
              'hoopa': 270, 'hoopa (unbound)': 306, 'volcanion': 270}
gen6Yield = gen5Yield | gen6Update
# Pokemon Sun/Moon
gen7RegUpdate = {'rowlet': 64, 'dartrix': 147, 'decidueye': 239, 'litten': 64,
                 'torracat': 147, 'incineroar': 239, 'popplio': 64,
                 'brionne': 147, 'primarina': 239, 'pikipek': 53,
                 'trumbeak': 124, 'toucannon': 218, 'yungoos': 51,
                 'gumshoos': 146, 'grubbin': 60, 'charjabug': 140,
                 'vikavolt': 225, 'crabrawler': 68, 'crabominable': 167,
                 'oricorio': 167, 'cutiefly': 61, 'ribombee': 162,
                 'rockruff': 56, 'lycanroc': 170, 'wishiwashi (solo)': 61,
                 'wishiwashi (school)': 217, 'mareanie': 61, 'toxapex': 173,
                 'mudbray': 77, 'mudsdale': 175, 'dewpider': 54,
                 'araquanid': 159, 'fomantis': 50, 'lurantis': 168,
                 'morelull': 57, 'shiinotic': 142, 'salandit': 64,
                 'salazzle': 168, 'stufful': 68, 'bewear': 175, 'bounsweet': 42,
                 'steenee': 102, 'tsareena': 230, 'comfey': 170,
                 'oranguru': 172, 'passimian': 172, 'wimpod': 46,
                 'golisopod': 186, 'sandyhast': 64, 'palossand': 168,
                 'pyukumuku': 144, 'type: null': 107, 'silvally': 114,
                 'minior (meteor)': 154, 'minior (core)': 175, 'komala': 168,
                 'turtonator': 170, 'togedemaru': 152, 'mimikyu': 167,
                 'bruxish': 166, 'drampa': 170, 'dhelmise': 181, 'jangmo-o': 60,
                 'hakamo-o': 147, 'kommo-o': 270, 'tapu-koko': 114,
                 'tapu lele': 114, 'tapu bulu': 114, 'tapu fini': 114,
                 'cosmog': 40, 'cosmoem': 80, 'solgaleo': 136, 'lunala': 136,
                 'nihilego': 114, 'buzzwole': 114, 'pheromosa': 114,
                 'xurkitree': 114, 'celesteela': 114, 'kartana': 114,
                 'guzzlord': 114, 'necrozma': 120, 'magearna': 120,
                 'marshadow': 120,
                 # ↓↓↓ Updates over previous generations ↓↓↓
                 'zygarde (10%)': 219, 'zygarde': 270,
                 'zygarde (complete)': 319}
gen7RegYield = gen6Yield | gen7RegUpdate
# Pokemon Ultra Sun/Ultra Moon/Let's Go Pikachu/Let's Go Eevee
gen7UltUpdate = gen7RegUpdate | {'silvally': 257, 'tapu koko': 257,
                                 'tapu lele': 257, 'tapu bulu': 257,
                                 'tapu fini': 257, 'cosmoem': 140,
                                 'solgaleo': 306, 'lunala': 306, 'nihlego': 257,
                                 'buzzwole': 257, 'pheromosa': 257,
                                 'xurkitree': 257, 'celesteela': 257,
                                 'kartana': 257, 'guzzlord': 257,
                                 'necrozma': 270, 'necrozma (dusk mane)': 306,
                                 'necrozma (dawn wings)': 306,
                                 'ultra necrozma': 339, 'magearna': 270,
                                 'marshadow': 270, 'poipole': 189,
                                 'naganadel': 243, 'stakataka': 257,
                                 'blacephalon': 257, 'zeraora': 270,
                                 'meltan': 135, 'melmetal': 270}
gen7UltYield = gen7RegYield | gen7UltUpdate
# Pokemon Sword/Shield/Brilliant Diamond/Shining Pearl/Legends Arceus
gen8Update = {'grookey': 62, 'thwackey': 147, 'rillaboom': 265, 'scorbunny': 62,
              'raboot': 147, 'cinderace': 265, 'sobble': 62, 'drizzile': 147,
              'inteleon': 265, 'skwovet': 55, 'greedent': 161, 'rookidee': 49,
              'corvisquire': 128, 'corviknight': 248, 'blipbug': 36,
              'dottler': 117, 'orbeetle': 253, 'nickit': 49, 'thievul': 159,
              'gossifleur': 50, 'eldegoss': 161, 'wooloo': 122, 'dubwool': 172,
              'chewtle': 57, 'drednaw': 170, 'yamper': 54, 'boltund': 172,
              'rolycoly': 48, 'carkol': 144, 'coalossal': 255, 'applin': 52,
              'flapple': 170, 'appletun': 170, 'silicobra': 63,
              'sandaconda': 179, 'cramorant': 166, 'arrokuda': 56,
              'barraskewda': 172, 'toxel': 48, 'toxtricity': 176,
              'sizzlipede': 61, 'centiskorch': 184, 'clobbopus': 62,
              'grapploct': 168, 'sinistea': 62, 'polteageist': 178,
              'hatenna': 53, 'hattrem': 130, 'hatterene': 255, 'impidimp': 53,
              'morgrem': 130, 'grimmsnarl': 255, 'obstagoon': 260,
              'perrserker': 154, 'cursola': 179, "sirfetch'd": 177,
              'mr. ryme': 182, 'runerigus': 169, 'milcery': 54, 'alcremie': 173,
              'falinks': 165, 'pincurchin': 152, 'snom': 37, 'frosmoth': 166,
              'stonjourner': 165, 'eiscue': 165, 'indeedee': 166,
              'morpeko': 153, 'cufant': 66, 'copperajah': 175, 'dracozolt': 177,
              'arctozolt': 177, 'dracovish': 177, 'arctovish': 177,
              'duraludon': 187, 'dreepy': 54, 'drakloak': 144, 'dragapult': 300,
              'zacian (hero)': 335, 'zacian (crowned)': 360,
              'zamazenta (hero)': 335, 'zamazenta (crowned)': 360,
              'eternatus': 345, 'eternatus (eternamax)': 563, 'kubfu': 77,
              'urshifu': 275, 'zarude': 300, 'regieleki': 290, 'regidrago': 290,
              'glastrier': 290, 'spectrier': 290, 'calyrex': 250,
              'calyrex (ice rider)': 340, 'calyrex (shadow rider)': 340,
              # Legends - Unknown EXP Yields
              'wyrdeer': -1, 'kleavor': -1, 'ursaluna': -1, 'basculegion': -1,
              'sneasler': -1, 'overquill': -1, 'enamorus': -1}
gen8Yield = gen7UltYield | gen8Update
# Pokemon Scarlet/Violet
gen9Update = {'Sprigatito': 62, 'Floragato': 144, 'Meowscarada': 265,
              'Fuecoco': 62, 'Crocalor': 144, 'Skeledirge': 265, 'Quaxly': 62,
              'Quaxwell': 144, 'Quaquaval': 265, 'Lechonk': 51,
              'Oinkologne': 171, 'Tarountula': 42, 'Spidops': 141, 'Nymble': 42,
              'Lokix': 158, 'Pawmi': 48, 'Pawmo': 123, 'Pawmot': 245,
              'Tandemaus': 61, 'Maushold': 165, 'Fidough': 62, 'Dachsbun': 167,
              'Smoliv': 52, 'Dolliv': 124, 'Arboliva': 255, 'Squawkabilly': 146,
              'Nacli': 56, 'Naclstack': 124, 'Garganacl': 250, 'Charcadet': 51,
              'Armarouge': 263, 'Ceruledge': 263, 'Tadbulb': 54,
              'Bellibolt': 173, 'Wattrel': 56, 'Kilowattrel': 172,
              'Maschiff': 68, 'Mabosstiff': 177, 'Shroodle': 58,
              'Grafaiai': 170, 'Bramblin': 55, 'Brambleghast': 168,
              'Toedscool': 67, 'Toedscruel': 180, 'Klawf': 158, 'Capsakid': 61,
              'Scovillain': 170, 'Rellor': 54, 'Rabsca': 165, 'Flittle': 51,
              'Espathra': 168, 'Tinkatink': 59, 'Tinkatuff': 133,
              'Tinkaton': 253, 'Wiglett': 49, 'Wugtrio': 149, 'Bombirdier': 243,
              'Finizen': 63, 'PalafinZero Form': 160, 'PalafinHero Form': 160,
              'Varoom': 60, 'Revavroom': 175, 'Cyclizar': 175, 'Orthworm': 240,
              'Glimmet': 70, 'Glimmora': 184, 'Greavard': 58, 'Houndstone': 171,
              'Flamigo': 175, 'Cetoddle': 67, 'Cetitan': 182, 'Veluza': 167,
              'Dondozo': 265, 'Tatsugiri': 166, 'Annihilape': 268,
              'Clodsire': 151, 'Farigiraf': 260, 'Dudunsparce': 182,
              'Kingambit': 275, 'Great Tusk': 285, 'Scream Tail': 285,
              'Brute Bonnet': 285, 'Flutter Mane': 285, 'Slither Wing': 285,
              'Sandy Shocks': 285, 'Iron Treads': 285, 'Iron Bundle': 285,
              'Iron Hands': 285, 'Iron Jugulis': 285, 'Iron Moth': 285,
              'Iron Thorns': 285, 'Frigibax': 64, 'Arctibax': 148,
              'Baxcalibur': 300, 'Gimmighoul': 60, 'Gholdengo': 275,
              'Wo-Chien': 285, 'Chien-Pao': 285, 'Ting-Lu': 285, 'Chi-Yu': 285,
              'Roaring Moon': 295, 'Iron Valiant': 295,
              'KoraidonApex Build': 335, 'MiraidonUltimate Mode': 335,
              'Walking Wake': 295, 'Iron Leaves': 295}
gen9Yield = gen8Yield | gen9Update


def genThree():
    """
    Calculates the Experience Yield of a particular Pokemon in Generation III
    Uses command line input to test functionality

        Parameters: None, command line

        Returns: None, prints to stdout
    """
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


def makeNames(gen: int = -1):
    """
    Creates a .xml file with the Pokemon names formatted to be used with 
        Android Studio

        Parameters:
            gen: The generation whose names should be exported, defaults to most
                 recent generation
        Returns: 
            None, creates output file
    """
    match gen:
        case -1:
            keysList = gen8Yield.keys()

            out = open(f'XMLNameFormat.txt', "w", encoding="utf-8")
            for key in keysList:
                out.write('<item>"' + key.capitalize() + '"</item>\n')
            out.close()
            return

        case 1:
            keysList = gen1Yield.keys()
        case 2:
            keysList = gen2Yield.keys()
        case 3:
            keysList = gen3Yield.keys()
        case 4:
            keysList = gen4Yield.keys()
        case 5:
            keysList = gen5Yield.keys()
        case 6:
            keysList = gen6Yield.keys()
        case 7:
            keysList = gen7UltYield.keys()
        case 8:
            keysList = gen8Yield.keys()

    out = open(f'Gen{gen}XMLNameFormat.xml', "w", encoding="utf-8")
    for key in keysList:
        out.write('<item>"' + key.capitalize() + '"</item>\n')
    out.close()


def makeHashMap(gen: int = -1, map:  str = "gen5_7Values"):
    """
    Generates a .txt file containing the Java syntax for creating a Hash Map for
    the input generation.

    Parameters:
        gen: The generation whose values should be output
        map: The name of the Java Hash Map

    Returns:
        None, generates output file
    """
    match gen:
        case -1:
            keysList = gen8Update.keys()

            out = open(f'JavaHashMap.txt', "w", encoding="utf-8")
            for item in keysList:
                out.write('gen5_7Values.put("' + item + '", ' +
                          str(gen6Update.get(item)) + ');\n')
            out.close()
            return

        case 1:
            keysList = gen1Yield.keys()
            dict = gen1Yield
        case 2:
            keysList = gen2Update.keys()
            dict = gen2Yield
        case 3:
            keysList = gen3Update.keys()
            dict = gen3Yield
        case 4:
            keysList = gen4Update.keys()
            dict = gen4Yield
        case 5:
            keysList = gen5Yield.keys()
            dict = gen5Yield
        case 6:
            keysList = gen6Update.keys()
            dict = gen6Yield
        case 7:
            keysList = gen7UltUpdate.keys()
            dict = gen7UltYield
        case 8:
            keysList = gen8Update.keys()
            dict = gen8Yield

    out = open(f"Gen{gen}JavaHashMap.txt", "w", encoding="utf-8")
    for item in keysList:
        out.write(f'{map}.put("' + item + '", ' +
                  str(dict.get(item)) + ');\n')
    out.close()


def getMax():
    """Print key with highest value"""
    # TODO: Output based on generation
    allValues = gen3Yield.values()
    print(max(gen3Yield, key=gen3Yield.get), max(allValues))


def run():
    """
    Runs the calculator function in a loop

    Parameters:
        None, command line input to continue

    Returns:
        None, prints to command line
    """
    while True:
        print("Generation 3 experience points gained: ", genThree(), "\n")
        again = input('Again?(y/n): ').lower()
        if again == 'n':
            exit(0)


def utility():
    """
    Runs the program in utility mode

    Parameters:
        None, command line input of desired generation

    Returns:
        None, generates Java format hash map and xml containing Pokemon names
    """
    try:
        gen = int(input("What generation?\n(1-7); leave blank for most recent): "))
    except ValueError:
        gen = -1

    makeHashMap(gen)
    makeNames(gen)


def startup():
    """
    Determines what mode to run the program in

    Parameters:
        None, command line input

    Returns:
        None, begins running program    
    """
    # Should be factored out to a config file
    mode = input("Run or Utility?(R/U): ")
    while True:
        if mode.lower() == "r":
            run()
        elif mode.lower() == "u":
            utility()
        else:
            mode = input("Please type R or U: ")


if __name__ == "__main__":
    startup()
