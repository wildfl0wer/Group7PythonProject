import data

#########################################################################
# A Character Creator program for a role-playing game.                  #
# The player is able to spend points from the pool on any attribute and #
# is also able to take points from an attribute and put them back into  #
# the pool.                                                             #
#########################################################################

# Constructs Character class
class Character:
    c_strength = 10
    c_dexterity = 10
    c_constitution = 10
    c_knowledge = 10
    c_charisma = 10

    c_strength_mod = 0
    c_dexterity_mod = 0
    c_constitution_mod = 0
    c_knowledge_mod = 0
    c_charisma_mod = 0

    c_race = "Human"
    c_class = "Fighter"
    c_firstname = "Leeroy"
    c_lastname = "Jenkins"
    c_item = ["Armor of Valor"]
    c_hp = 6                       # character "health points"
    c_ac= 10                       # character "armor points" (base = 10)

    # Returns object as String
    def __str__(self):
        return "Name: {} {}\nRace: {}\nClass: {}".format(
            self.c_firstname, self.c_lastname, 
            self.c_race, self.c_class)

# Assigns traits to current character
def assign_traits(trait, trait_dict):
    # Creates list of traits
    trait_list = list(trait_dict.keys())

    # Creates list of trait descriptions if 
    # 'Description' key exists in dictionary
    description_list = []
    for item in trait_dict.keys():
        for key in trait_dict[item].keys():
            if key.find('Description') > - 1:
                description_list.append(trait_dict[item][key])
    
    # Creates menu of traits for user to choose from
    print("\nPick a {} for your character:".format(trait))
    # Adds a description to menu if it exists
    if not description_list:
        for t in trait_list:
            print("\t",trait_list.index(t) + 1, "-", t)
    else:
        for t in trait_list:
            print("\t {} - {:22} [{}]".format(trait_list.index(t) + 1, t,
                                    description_list[trait_list.index(t)]))
    # Prompts user for choice from trait menu
    trait_choice = input("Enter a number from 1 to {}: "
                         .format(len(trait_list)))

    # Validates user input
    # Continues to prompt user until input valid
    while True:
        # Accepts valid numbers
        try:
            trait_choice = int(trait_choice)
            if (trait_choice > 0 and trait_choice <= len(trait_list)):
                break
            # Rejects invalid numbers
            else:
                # Converts choice to non-number input
                trait_choice = ""
                continue
        # Rejects non-number inputs
        except:
            print("\nPlease make a valid selection.")
            # Prompts user for valid input
            trait_choice = input("Enter a number from 1 to {}: "
                           .format(len(trait_list)))

    # Returns selected trait from trait list
    return trait_list[trait_choice - 1]

# Assigns base attribute points
def assign_base_points(race_name, attribute, min_base_points, special_item):
    # Assigns race attribute modifier
    race_modifier_attribute = data.races[race_name][attribute]
    # Assigns item attribute modifier
    item_bonus_type = data.special_items[special_item]['Item Bonus Type']
    if (item_bonus_type == attribute):
        item_bonus = data.special_items[special_item]['Item Bonus Number']
    else:
        item_bonus = 0
    # Returns base attribute points
    return (min_base_points + race_modifier_attribute + item_bonus)

# Attribute points menu
def attribute_menu(attribute_names, attribute_points, updated_point_pool):
    # Displays menu with attributes
    print("\n\n\t{:7}Available Points ({})".format(" ", updated_point_pool))
    print("\n\tEnter:")
    # Iterates through attribute_names and attribute_points lists
    for (att_n, att_p) in zip(attribute_names, attribute_points):
        name = att_n
        points = att_p
        print("\t{:7}{} - {} ({})".format(" ", attributes.index(att_n) + 1, name, points))
    print("\t{:7}X - To exit the program".format(" "))

# Validates input for attribute points menu
def validate_attribute_menu_input(attribute_names):
    # Prompts user for attribute menu choice
    attribute_choice = input("Make your selection: ")
    # Validates attribute choice
    while True:
        try:
            # Accepts valid numbers
            attribute_choice = int(attribute_choice)
            if (attribute_choice > 0 and 
                attribute_choice <= len(attribute_names)):
                break
            # Rejects invalid numbers
            else:
                # Converts choice to non-number input
                attribute_choice = ""
        except:
            # Accepts 'x' to exit menu
            if (attribute_choice == 'x' or attribute_choice == 'X'):
                attribute_choice = 'x'
                break
            # Rejects all other non-number inputs
            else:
                print("\nPlease make a valid selection.")
                statement =("Enter a number from 1 to " +
                            str(len(attribute_names)) +
                            " or press 'x' to exit. ")
                # Prompts user for valid input
                attribute_choice = input(statement)
    # Returns attribute choice
    return attribute_choice

# Prompts user for update amount for attribute points
def prompt_for_points(att_name, att_value_list, 
                      min_base_points, max_base_points, att_bonus,
                      updated_point_pool, user_input):
    # Retrieves attribute value from list
    att_value = att_value_list[user_input - 1]
    # Calculates base attribute value
    base_value = att_value - att_bonus
    # Displays remaining points from pool
    print("\n\nAvailable Points: {}".format(updated_point_pool), end=" ")
    # Display minimum and maximum points for attribute
    print("  |  Minimum Base {}: {}  |  Maximum Base {}: {}".format(
                                                  att_name, min_base_points,
                                                  att_name, max_base_points))
    # Displays base and total attribute values
    print("\n\t\tBase {}: {}\tTotal {}: {}".format(att_name, base_value,
                                                   att_name, att_value))
    # Prompts user for points amount to update
    print("\nHow many point would you like to add or remove?")
    print("\tEnter a positive number to add points.")
    print("\tEnter a negative number to remove points.")
    # Displays valid amounts of points to update
    if ((max_base_points - base_value) <= updated_point_pool):
        print("\t-You can add a maximum of {} points."
            .format(max_base_points - base_value))
    else:
        print("\t-You can add a maximum of {} points."
            .format(updated_point_pool))
    print("\t-You can remove a maximum of {} points."
          .format(base_value - min_base_points))
    print("\nAssign points to {}:".format(att_name), end=" ")
    # Validates user input
    while True:
        try:
            # Accepts whole number input
            points_to_update = int(input())
            break
        except:
            # Rejects non-number input
            print("Please enter a whole number value:", end=" ")
    return points_to_update

# Modifies attribute points according to user input
def assign_points(total_points, updated_point_pool, min_base_points, max_base_points, attribute_points_list, att_name, att_bonus, att_choice, user_input):
    # Retrieves attribute value from list
    att_value = attribute_points_list[att_choice - 1]
    # Calculates base attribute value
    base_value = att_value - att_bonus
    choice = ""
    while True:
        if (((updated_point_pool - user_input) <= total_points) and
            ((updated_point_pool - user_input) >= 0) and
            (base_value + user_input >= min_base_points) and
            (base_value + user_input <= max_base_points)):
            att_value = int(att_value + user_input)
            base_value = att_value - att_bonus
            attribute_points_list[att_choice - 1] = att_value
            updated_point_pool = updated_point_pool - user_input
            print("Base value:", base_value)
            break
        else:
            if (((updated_point_pool - user_input) > total_points) or
                 (base_value + user_input < min_base_points)):
                print("\nYou do not have enough {} points available for "
                      "that.".format(att_name))
                print("The minimum {} base value is {}.".format(att_name, min_base_points))
                # Displays base and total attribute values
                print("\n\tBase {}: {}\tTotal {}: {}".format(
                                                        att_name, base_value,
                                                        att_name, att_value))
            elif (base_value + user_input > max_base_points):
                print("\nYou cannot add anymore points to {}.".format(att_name))
                print("The maximum {} value is {}.".format(att_name, max_base_points))
                # Displays base and total attribute values
                print("\n\tBase {}: {}\tTotal {}: {}".format(
                                                        att_name, base_value,
                                                        att_name, att_value))
            else:
                print("\nYou do not have enough points available for that.")
                print("Available Points:", updated_point_pool)
            # Prompts user for valid choice
            choice = input("\nEnter a valid value or press 'x' to return "
                           "to the main menu: ")
            if (choice == 'x' or choice == 'X'):
                break
            while (choice != 'x' or choice != 'X'):
                try:
                    user_input = int(choice)
                    break
                except:
                    if (choice == 'x' or choice == 'X'):
                        break
                    else:
                        print("Please make a valid selection.")
                        choice = input("\nEnter a valid value or press 'x' to "
                                       "to return to the main menu. ")
            input("\nPress enter to continue.")
    return att_value, att_name, updated_point_pool

# Updates attributes points
def update_attributes(point_pool, min_base_points,
                   max_base_points, dict_base_attributes):

    attribute_names = list(dict_base_attributes.keys())
    attribute_points = list(dict_base_attributes.values())
    updated_point_pool = point_pool
    updated_points_list = list(attribute_points)
    updated_attributes = dict(dict_base_attributes)


    while True:
        attribute_menu(attribute_names, updated_points_list, updated_point_pool)
        choice = validate_attribute_menu_input(attribute_names)
        if (choice == 'x'):
            break
        else:
            att_name = attribute_names[choice - 1]
            att_points = attribute_points[choice - 1]
            att_bonus = att_points - min_base_points

            updated_points = prompt_for_points(att_name, updated_points_list,
                                               min_base_points,max_base_points,
                                               att_bonus, updated_point_pool,
                                               choice)
            
            updated_att, att_name, updated_point_pool = assign_points(
                                    point_pool, updated_point_pool,
                                    min_base_points, max_base_points,
                                    updated_points_list, att_name, att_bonus,
                                    choice, updated_points)
            updated_attributes[att_name] = updated_att

    return updated_attributes, updated_point_pool


# Displays character information
def display_character(new_character):
    print("Name:  {} {}\nRace:  {}\nClass: {}".format(
                                                 new_character.c_firstname,
                                                 new_character.c_lastname,
                                                 new_character.c_race,
                                                 new_character.c_class))
    print("----------------------------------")
    print("Special Item:",new_character.c_item)
    print("----------------------------------")
    print("Strength: {:8}\nDexterity: {:7}\nConstitution: {:4}"\
          "\nKnowledge: {:7}\nCharisma: {:8}".format(
                                        new_character.c_strength,
                                        new_character.c_dexterity,
                                        new_character.c_constitution,
                                        new_character.c_knowledge,
                                        new_character.c_charisma))

# Creates new character
def create_character():
    new_character = Character()

    new_character.c_firstname = input("Enter your character's first name: ")
    new_character.c_lastname = input("Enter your character's last name:  ")

    dict_races = dict(data.races)
    dict_classes = dict(data.classes)
    dict_items = dict(data.special_items)

    # Prompts user for character race
    new_character.c_race = assign_traits('race', dict_races)

    # Prompts user for character class
    new_character.c_class = assign_traits('class', dict_classes)

    # Prompts user for character special item
    new_character.c_item = assign_traits('special item', dict_items)

    # Points variables
    point_pool = data.PURCHASE_POINTS
    min_base_points = data.MIN_BASE_POINTS
    max_base_points = data.MAX_BASE_POINTS


    # Assigns character base strength
    new_character.c_strength = assign_base_points(new_character.c_race, 
                                                  'Strength', 
                                                  min_base_points,
                                                  new_character.c_item)

    # Assigns character base dexterity
    new_character.c_dexterity = assign_base_points(new_character.c_race, 
                                                   'Dexterity', 
                                                   min_base_points,
                                                   new_character.c_item)

    # Assigns character constitution
    new_character.c_constitution = assign_base_points(new_character.c_race, 
                                                      'Constitution', 
                                                      min_base_points,
                                                      new_character.c_item)

    # Assigns character base knowledge
    new_character.c_knowledge = assign_base_points(new_character.c_race, 
                                                   'Knowledge', 
                                                   min_base_points,
                                                   new_character.c_item)

    # Assigns character base knowledge
    new_character.c_charisma = assign_base_points(new_character.c_race, 
                                                  'Charisma', 
                                                  min_base_points,
                                                  new_character.c_item)

    base_attributes = {
        'Strength' : new_character.c_strength,
        'Dexterity' : new_character.c_dexterity,
        'Constitution' : new_character.c_constitution,
        'Knowledge' : new_character.c_knowledge,
        'Charisma' : new_character.c_charisma
    }

    updated_attributes, updated_point_pool = update_attributes(point_pool, min_base_points, max_base_points, base_attributes)

    # Assigns character base strength
    new_character.c_strength = updated_attributes['Strength']

    # Assigns character base dexterity
    new_character.c_dexterity = updated_attributes['Dexterity']

    # Assigns character constitution
    new_character.c_constitution = updated_attributes['Constitution']

    # Assigns character base knowledge
    new_character.c_knowledge = updated_attributes['Knowledge']

    # Assigns character base knowledge
    new_character.c_charisma = updated_attributes['Charisma']

    return new_character


# Introduction
attributes = []
for att in data.attributes:
    attributes.append(att)

character_list = []

print("\n\n\t\tWelcome to the Character Creator!"
      "\nYou can create custom characters with a custom names and choose their"
      " race and class."
      "\nFor each character you have a pool of {} points to spend on {}"
      " attributes: \n\t{}, {}, {}, and {}\nYou can spend points from"
      " the pool on any attribute as well as reassign those points."
      .format(data.PURCHASE_POINTS, len(attributes), attributes[0],
      attributes[1], attributes[2], attributes[3], attributes[4]))
input("\nPress enter to continue.")

new_input = ""

while new_input != "exit":
    new_input = input("\nCreate a new character? (Y/N): ")

    new_input = new_input.lower()
    if (new_input == "yes" or new_input == "y" or 
        new_input == "Yes" or new_input == "Y"):
        print("Ok, let's make a character!\n")
        print("===============================================================")
        new_character = create_character()
        character_list.append(new_character)
    elif (new_input == "no" or new_input == "NO" or
          new_input == "n" or new_input == "N" or
          new_input == "exit" or new_input == "EXIT" or
          new_input == "x" or new_input == "X"):
        new_input = "exit"
        for character in character_list:
            print("\n----------------------------------")
            print("\tCharacter", character_list.index(character) + 1)
            print("----------------------------------")
            display_character(character)
            print("----------------------------------")
        input("\nPress enter to exit.")
        break