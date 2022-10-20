# Pokemon Experience Gain Calculator V1
# Update to Python 3.9 dipshit
# https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-taking-union-of-dictiona
# Kirk Rieberger
from math import floor
from sys import exit
# Dictionaries containing the exp values for each Pokemon
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
             'shaymin': 64, 'arceus': 255, 'abra': 75, 'machop': 75,
             'geodude': 73, 'omanyte': 99, 'kabuto': 99, 'kabutops': 199,
             'dunsparce': 125, 'silcoon': 72, 'dustox': 161, 'lileep': 99,
             'cradily': 199, 'anorith': 99, 'armaldo': 99}
gen4Yield = gen3Yield | gen4Update
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
             'larvitar': 60, 'pupitar': 144, 'tyranitar': 270, 'lugia':306,
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
    print(len(gen3Update))
    return 0

def makeNames():
    out = open("XMLNameFormat.txt", "w", encoding="utf-8")
    keysList = gen3Yield.keys()
    for key in keysList:
        out.write('<item>"' + key.capitalize() + '"</item>\n')
    out.close()
    
def makeGen5Names():
    out = open("XMLNameFormatGen5.txt", "w", encoding="utf-8")
    keysList = gen5Yield.keys()
    for key in keysList:
        out.write('<item>"' + key.capitalize() + '"</item>\n')
    out.close()
    
def makeHashMap():
    out = open("JavaHashMap.txt", "w", encoding="utf-8")
    keysList = gen3Yield.keys()
    for item in keysList:
        out.write('gen1_3Values.put("' + item + '", ' + str(gen4Yield.get(item)) + ');\n')
    out.close()
    
def makeHashMapGen5():
    out = open("JavaHashMapGen5.txt", "w", encoding="utf-8")
    keysList = gen5Yield.keys()
    for item in keysList:
        out.write('gen5Values.put("' + item + '", ' + str(gen5Yield.get(item)) + ');\n')
    out.close()


run = 1
while run:
    #print("Generation 3 experience points gained: ", genThree(), "\n")
    #again = input('Again?(y/n): ').lower()
    #if again == 'n':
    #    exit(0)
    #genOne()
    #genSeven()
    makeHashMap()
    makeHashMapGen5()
    makeNames()
    makeGen5Names()
    exit(0)
    break

def getMax():
# Print key with highest value
    allValues = gen3Yield.values()
    print(max(gen3Yield, key=gen3Yield.get), max(allValues))
    
