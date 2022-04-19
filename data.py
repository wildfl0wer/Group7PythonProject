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

# Races and traits
races = {
    'Dwarf' : {
        'Strength' : 2,
        'Dexterity' : 0,
        'Constitution' : 2,
        'Knowledge' : 0,
        'Charisma' : 0
    },
    'Elf' : {
        'Strength' : 0,
        'Dexterity' : 2,
        'Constitution' : 0,
        'Knowledge' : 2,
        'Charisma' : 0
    },
    'Halfling' : {
        'Strength' : 0,
        'Dexterity' : 2,
        'Constitution' : 0,
        'Knowledge' : 1,
        'Charisma' : 1
    },
    'Half-Elf' : {
        'Strength' : 0,
        'Dexterity' : 1,
        'Constitution' : 0,
        'Knowledge' : 1,
        'Charisma' : 2
    },
    'Human' : {
        'Strength' : 1,
        'Dexterity' : 1,
        'Constitution' : 1,
        'Knowledge' : 1,
        'Charisma' : 1
    }
}

# Classes and traits
classes = {
    'Bard' : {
        'Hit Die' : '1d8',
        'Base HP' : 8,
        'Important Attributes' : ('Charisma', 'Constitution')
    },
    'Fighter' : {
        'Hit Die' : '1d10',
        'Base HP' : 10,
        'Important Attributes' : ('Strength', 'Constitution')
    },
    'Ranger' : {
        'Hit Die' : '1d10',
        'Base HP' : 10,
        'Important Attributes' : ('Dexterity', 'Knowledge', 'Constitution')
    },
    'Rogue' : {
        'Hit Die' : '1d8',
        'Base HP' : 8,
        'Important Attributes' : ('Dexterity', 'Constitution')
    },
    'Wizard' : {
        'Hit Die' : '1d6',
        'Base HP' : 6,
        'Important Attributes' : ('Knowledge', 'Constitution')
    }
}

# Special items and traits
special_items = {
    'Orb of Foresight' : {
        'Item Description' : 'Knowledge + 1',
        'Item Bonus Type' : 'Knowledge',
        'Item Bonus Number' : 1
    },
    'Champion\'s Cloak' : {
        'Item Description' : 'Constitution + 1',
        'Item Bonus Type' : 'Constitution',
        'Item Bonus Number' : 1
    },
    'Amulet of Siren Song' : {
        'Item Description' : 'Charisma + 1',
        'Item Bonus Type' : 'Charisma',
        'Item Bonus Number' : 1
    },
    'Polearm of Valor' : {
        'Item Description' : 'Strength + 1',
        'Item Bonus Type' : 'Strength',
        'Item Bonus Number' : 1
    },
    'Dagger of Shadowstep' : {
        'Item Description' : 'Dexterity + 1',
        'Item Bonus Type' : 'Dexterity',
        'Item Bonus Number' : 1
    },
}