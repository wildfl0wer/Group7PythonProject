# Points Variables
PURCHASE_POINTS = 27
MIN_BASE_POINTS = 8
MAX_BASE_POINTS = 15

# Attributes
attributes = {
    'Strength' : 'Athleticism and bodily power',
    'Dexterity' : 'Agility and reflexes',
    'Constitution' : 'Stamina and vitality',
    'Knowledge' : 'Analytical skills and insight',
    'Charisma' : 'Confidence and eloquence'
}

# Attribute modifiers
modifiers = {
    8 : -1,
    9 : -1,
    10 : 0,
    11 : 0,
    12 : 1,
    13 : 1,
    14 : 2,
    15 : 2,
    16 : 3,
    17 : 3,
    18 : 4,
}

# Races and traits
races = {
    'Dwarf' : {
        'Strength' : 2,
        'Dexterity' : 0,
        'Constitution' : 2,
        'Knowledge' : 0,
        'Charisma' : 0,
        'Character Description' : ('Strong & Vigorous | Bonus: Strength(2)'
                                   ' & Constitution(2)')
    },
    'Elf' : {
        'Strength' : 0,
        'Dexterity' : 2,
        'Constitution' : 0,
        'Knowledge' : 2,
        'Charisma' : 0,
        'Character Description' : ('Wise & Graceful | Bonus: Knowledge(2)'
                                   ' & Dexterity(2)')
    },
    'Halfling' : {
        'Strength' : 0,
        'Dexterity' : 2,
        'Constitution' : 0,
        'Knowledge' : 1,
        'Charisma' : 1,
        'Character Description' : ('Nimble, Creative & Gregarious | Bonus:'
                                   ' Dexterity(2) Knowledge(1) & Charisma(1)')
    },
    'Half-Elf' : {
        'Strength' : 0,
        'Dexterity' : 1,
        'Constitution' : 0,
        'Knowledge' : 1,
        'Charisma' : 2,
        'Character Description' : ('Charismatic, Clever & Quick | Bonus:'
                                   ' Charisma(2) Knowledge(1) & Dexterity(1)')
    },
    'Human' : {
        'Strength' : 1,
        'Dexterity' : 1,
        'Constitution' : 1,
        'Knowledge' : 1,
        'Charisma' : 1,
        'Character Description' : ('Jack-of-All-Trades | Bonus(1)'
                                   ' to all attributes')
    }
}

# Classes and traits
classes = {
    'Bard' : {
        'Hit Die' : '1d8',
        'Base HP' : 8,
        'Important Attributes' : ('Charisma', 'Constitution'),
        'Class Description' : ('Musical Magician | Best for charismatic'
                               ' characters')
    },
    'Fighter' : {
        'Hit Die' : '1d10',
        'Base HP' : 10,
        'Important Attributes' : ('Strength', 'Constitution'),
        'Class Description' : ('Skilled Warrior | Best for strong characters')
    },
    'Ranger' : {
        'Hit Die' : '1d10',
        'Base HP' : 10,
        'Important Attributes' : ('Dexterity', 'Knowledge', 'Constitution'),
        'Class Description' : ('Nature Guardian | Best for knowledgeable'
                               ' and dexterous characters')
    },
    'Rogue' : {
        'Hit Die' : '1d8',
        'Base HP' : 8,
        'Important Attributes' : ('Dexterity', 'Constitution'),
        'Class Description' : ('Stealthy Trickster | Best for dexterous'
                               ' characters')
    },
    'Wizard' : {
        'Hit Die' : '1d6',
        'Base HP' : 6,
        'Important Attributes' : ('Knowledge', 'Constitution'),
        'Class Description' : ('Learned Spellcaster | Best for knowledgeable'
                               ' characters')
    }
}

# Special items and traits
special_items = {
    'Orb of Foresight' : {
        'Item Description' : 'Knowledge + 1 | Best for Wizards and Rangers',
        'Item Bonus Type' : 'Knowledge',
        'Item Bonus Number' : 1
    },
    'Champion\'s Cloak' : {
        'Item Description' : 'Constitution + 1 | Useful to all classes',
        'Item Bonus Type' : 'Constitution',
        'Item Bonus Number' : 1
    },
    'Amulet of Siren Song' : {
        'Item Description' : 'Charisma + 1 | Best for Bards',
        'Item Bonus Type' : 'Charisma',
        'Item Bonus Number' : 1
    },
    'Polearm of Valor' : {
        'Item Description' : 'Strength + 1 | Best for Fighters',
        'Item Bonus Type' : 'Strength',
        'Item Bonus Number' : 1
    },
    'Dagger of Shadowstep' : {
        'Item Description' : 'Dexterity + 1 | Best for Rogues and Rangers',
        'Item Bonus Type' : 'Dexterity',
        'Item Bonus Number' : 1
    },
}