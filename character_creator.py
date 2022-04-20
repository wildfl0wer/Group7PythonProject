import data

#########################################################################
# A Character Creator program for a role-playing game.                  #
# The user chooses a name, race, class and special item for the         #
# character. The user is able to spend points from the pool on any      #
# attribute and is also able to take points from an attribute and put   #
# them back into the pool. When the user finishes assigning points to   #
# the character's attributes, the program determines the character's    #
# attribute modifiers, hit die, HP, and AC. The character is then saved #
# to a list, and the user has the option to create another character.   #
# When the user finished creating characters, the characters' datails   #
# are displayed, and the program closes                                 #
#########################################################################

## Global dictionaries imported from data.py
dict_attributes = dict(data.attributes)
dict_races = dict(data.races)
dict_classes = dict(data.classes)
dict_items = dict(data.special_items)
dict_modifiers = dict(data.modifiers)

## Global points variables imported from data.py
point_pool = data.PURCHASE_POINTS
min_base_points = data.MIN_BASE_POINTS
max_base_points = data.MAX_BASE_POINTS

## Lists of attributes' names and descriptions
list_att_names = list(dict_attributes.keys())
list_att_descriptions = list(dict_attributes.values())

## Constructs Character class
class Character:
    # Character's attributes
    c_strength = 10
    c_dexterity = 10
    c_constitution = 10
    c_knowledge = 10
    c_charisma = 10

    # Character's attribute modifiers
    c_strength_mod = 0
    c_dexterity_mod = 0
    c_constitution_mod = 0
    c_knowledge_mod = 0
    c_charisma_mod = 0

    # Character's traits
    c_race = "Human"
    c_class = "Fighter"
    c_firstname = "Leeroy"
    c_lastname = "Jenkins"
    c_item = "Polearm of Valor"

    # Character's hit die, hit points and armor class
    c_hd = '1d10'             # hit die, dice player should roll for character
    c_hp = 10                 # character "health points"
    c_ac= 10                  # character "armor points" (base = 10)

    # Returns object as String
    def __str__(self):
        return "Name: {} {}\nRace: {}\nClass: {}".format(
            self.c_firstname, self.c_lastname, 
            self.c_race, self.c_class)

## Introduction
def introduction():
    print("\n\n\t\tWelcome to the Character Creator!"
        "\n\nYou can create custom characters with a custom names and"
        " choose their race and class."
        "\nFor each character you have a pool of {} points to spend on {}"
        " attributes: \n\t{}, {}, {}, and {}\nYou can spend points from"
        " the pool on any attribute as well as reassign those points."
        "\nThe program will calculate each character's hit die, HP, and AC"
        " for you."
        .format(point_pool, len(list_att_names),
        list_att_names[0], list_att_names[1], list_att_names[2],
        list_att_names[3], list_att_names[4]))

## Assigns traits to current character
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
    # Adds a description to menu if it exists
    print("\nPick a {} for your character:".format(trait))
    # Displays if no description
    if not description_list:
        for t in trait_list:
            print("\t",trait_list.index(t) + 1, "-", t)
    # Displays if description
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

## Assigns base attribute points
def assign_base_points(race_name, attribute, special_item):
    # Assigns race attribute modifier
    race_att_modifier = dict_races[race_name][attribute]
    
    # Assigns item attribute modifier value
    item_bonus_type = dict_items[special_item]['Item Bonus Type']
    # Adds bonus points if item modifies attribute points 
    if (item_bonus_type == attribute):
        item_bonus = dict_items[special_item]['Item Bonus Number']
    else:
        item_bonus = 0
    # Returns base attribute points
    return (min_base_points + race_att_modifier + item_bonus)

## Attribute points menu
def attribute_menu(list_updated_att_points, updated_point_pool,
                   character_class, list_imp_class_att):
    ''' Displays menu with attributes '''
    print("\n\n\t{:12}Available Points ({})".format(" ", updated_point_pool))
    print("\t{:11}-----------------------".format(" "))
    # Recommends attributes based on charater class
    print("\t[{}s should focus their points on".format(character_class),
                                                 end=" ")
    # Ensures recommended attributes displayed properly
    for att in list_imp_class_att:
        if ((list_imp_class_att.index(att) == len(list_imp_class_att) - 2) and
            len(list_imp_class_att) == 2):
            print("{}".format(att), end=" ")
        elif (list_imp_class_att.index(att) != len(list_imp_class_att) - 1):
            print("{},".format(att), end=" ")
        else:
            print("and {}.]".format(att))
    print("\tEnter:")
    # Iterates through lists for variables
    for (att_n, att_p, att_d) in zip(list_att_names, list_updated_att_points,
                                     list_att_descriptions):
        name = att_n
        points = att_p
        description = att_d
        print("\t{:7}{} - {:13} ({})\t [{}]".format(
                                         " ", list_att_names.index(att_n) + 1,
                                         name, points, description))
    print("\t{:7}X - To exit the menu".format(" "))

## Validates input for attribute points menu
def validate_attribute_menu_input(attribute_names):
    # Prompts user for attribute menu choice
    attribute_choice = input("Make your selection: ")
    # Validates user input
    # Continues to prompt user until input valid
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

## Prompts user for update amount for attribute points
def prompt_for_points(att_name, list_att_values, att_bonus,
                      updated_point_pool, user_input):
    # Retrieves attribute value from list
    att_value = list_att_values[user_input - 1]
    # Calculates base attribute value
    base_value = att_value - att_bonus
    # Displays remaining points from pool
    print("\n\nAvailable Points: {}".format(updated_point_pool), end=" ")
    # Displays minimum and maximum points for attribute
    print("  |  Minimum Base {}: {}  |  Maximum Base {}: {}".format(
                                                  att_name, min_base_points,
                                                  att_name, max_base_points))
    # Displays base and total attribute values
    print("\n\t\tBase {}: {}\tTotal {}: {}".format(att_name, base_value,
                                                   att_name, att_value))
    # Prompts user for points amount to update
    print("\nHow many points would you like to add or remove?")
    print("\tEnter a positive number to add points.")
    print("\tEnter a negative number to remove points.")
    # Displays valid amounts of points to update
    if ((max_base_points - base_value) <= updated_point_pool):
        print("\t- You can add a maximum of {} points."
            .format(max_base_points - base_value))
    else:
        print("\t- You can add a maximum of {} points."
            .format(updated_point_pool))
    print("\t- You can remove a maximum of {} points."
          .format(base_value - min_base_points))
    print("\nAssign points to {}:".format(att_name), end=" ")
    # Validates user input
    # Continues to prompt user until input valid
    while True:
        try:
            # Accepts whole number input
            points_to_update = int(input())
            break
        except:
            # Rejects non-number input
            print("Please enter a whole number value:", end=" ")
    # Returns quantity of point to update for attribute
    return points_to_update

# Modifies attribute points according to user input
def assign_points(updated_point_pool, list_att_values, att_name,
                  att_bonus, att_choice, user_input):
    # Retrieves attribute value from list
    att_value = list_att_values[att_choice - 1]
    # Calculates base attribute value
    base_value = att_value - att_bonus

    # Test if points amount to update valid
    while True:
        # Accepts updated points value IF point change isn't greater than 
        # or less than total point pool value AND updated points are greater 
        # than or equal to attribute min value AND updated points are less
        # than or equal to attribute max value
        if (((updated_point_pool - user_input) <= point_pool) and
            ((updated_point_pool - user_input) >= 0) and
            (base_value + user_input >= min_base_points) and
            (base_value + user_input <= max_base_points)):
            # Updates attribute total value
            att_value = int(att_value + user_input)
            # Updates attribute base value (without modifiers)
            base_value = att_value - att_bonus
            # Updates attribute value in attributes values list
            list_att_values[att_choice - 1] = att_value
            # Updates point pool
            updated_point_pool = updated_point_pool - user_input
            # Returns to attribute menu
            break
        else:
            # Displays message indicating not enough attribute points
            # available for point change IF (point change requires removing
            # more points from point pool than the total value of point pool
            # OR point change would make attribute value less than attribute
            # min value) AND amount to be updated is less than or  equal to
            # current value of point pool
            if ((((updated_point_pool - user_input) > point_pool) or
                 ( base_value + user_input < min_base_points)) and
                   user_input <= updated_point_pool):
                print("\nYou do not have enough {} points available for "
                      "that.".format(att_name))
                print("The minimum {} base value is {}.".format(att_name, min_base_points))
                # Displays base and total attribute values
                print("\n\tBase {}: {}\tTotal {}: {}".format(
                                                        att_name, base_value,
                                                        att_name, att_value))
            # Displays message indicating point amount entered is greater
            # than attribute max value IF point change would make attribute
            # value greater than attribute max value AND amount to be updated
            # is less than or equal to the current value of point pool
            elif (base_value + user_input > max_base_points and
                  user_input <= updated_point_pool):
                print("\nYou cannot add that many points to {}."
                      .format(att_name))
                print("The maximum {} value is {}.".format(att_name, max_base_points))
                # Displays base and total attribute values
                print("\n\tBase {}: {}\tTotal {}: {}".format(
                                                        att_name, base_value,
                                                        att_name, att_value))
            # Displays message indicating not enough points in current point
            # pool for point change
            else:
                print("\nYou do not have enough points available for that.")
                print("Available Points:", updated_point_pool)
            # Prompts user for valid input
            else_choice = input("\nEnter a valid value or press 'x' to return "
                           "to the main menu: ")
            # Converts input to lowercase
            else_choice = else_choice.lower()
            # Returns to attribute menu
            if (else_choice == 'x'):
                break
            while (else_choice != 'x'):
                # Accepts number input
                try:
                    user_input = int(else_choice)
                    break
                except:
                    # Returns to attribute menu
                    if (else_choice == 'x'):
                        break
                    # Prompts user for valid input
                    else:
                        print("Please make a valid selection.")
                        else_choice = input("\nEnter a valid value or press"
                                        " 'x' to to return to the main menu. ")
            input("\nPress enter to continue.")
    # Returns updated attribute value and updated point pool
    return att_value, updated_point_pool

## Updates attributes points
def update_attributes(dict_base_attributes, c_class):
    # Holds updated point pool
    updated_point_pool = point_pool
    # Holds base attribute points
    list_base_att_points = list(dict_base_attributes.values())
    # List and dictionary that hold updated attribute points
    list_updated_att_points = list(list_base_att_points)
    dict_updated_att_points = dict(dict_base_attributes)
    # List of attributes special to character class
    list_imp_class_att = dict_classes[c_class]['Important Attributes']

    # Displays attribute menu and updates att points selected by user
    while True:
        attribute_menu(list_updated_att_points, updated_point_pool,
                       c_class, list_imp_class_att)
        # Prompts user for menu choice and validates input
        update_att_choice = validate_attribute_menu_input(list_att_names)
        # Continues to update points until user exits
        if (update_att_choice == 'x'):
            break
        # Updates points
        else:
            # Name attribute to update
            att_name = list_att_names[update_att_choice - 1]
            # Attribute points to update
            att_points = list_base_att_points[update_att_choice - 1]
            # Bonus added attribute
            att_bonus = att_points - min_base_points
            # Prompts user for point value to update and validates input
            updated_points = prompt_for_points(
                             att_name, list_updated_att_points, att_bonus,
                             updated_point_pool, update_att_choice)
            # Updates attribute points and point pool
            updated_att, updated_point_pool = assign_points(updated_point_pool,
                                    list_updated_att_points,
                                    att_name, att_bonus,
                                    update_att_choice, updated_points)
            # Updates attribute value in attributes list
            dict_updated_att_points[att_name] = updated_att
    # Returns updated attributes in dictionary and updated point pool
    return dict_updated_att_points, updated_point_pool

## Displays character information
def display_character(new_character):
    print("Name:  {} {}\nRace:  {}\nClass: {}".format(
                                                 new_character.c_firstname,
                                                 new_character.c_lastname,
                                                 new_character.c_race,
                                                 new_character.c_class))
    print("----------------------------------")
    print("Special Item:", new_character.c_item)
    print("Hit die (HD):", new_character.c_hd)
    print("Hit points (HP):", new_character.c_hp)
    print("Armor class (AC):", new_character.c_ac)
    print("----------------------------------")
    print("Strength: {:8}\t[{:+}] MOD"
          "\nDexterity: {:7}\t[{:+}] MOD"
          "\nConstitution: {:4}\t[{:+}] MOD"
          "\nKnowledge: {:7}\t[{:+}] MOD"
          "\nCharisma: {:8}\t[{:+}] MOD".format(
                new_character.c_strength, new_character.c_strength_mod,
                new_character.c_dexterity, new_character.c_dexterity_mod,
                new_character.c_constitution, new_character.c_constitution_mod,
                new_character.c_knowledge, new_character.c_knowledge_mod,
                new_character.c_charisma, new_character.c_charisma_mod,))

## Creates new character
def create_character():
    # Creates Character object
    new_character = Character()

    ## CHARACTER TRAITS ##
    # Prompts user for character's name
    new_character.c_firstname = input("Enter your character's first name: ")
    new_character.c_lastname = input("Enter your character's last name:  ")
    # Prompts user for character's race
    new_character.c_race = assign_traits('race', dict_races)
    # Prompts user for character's class
    new_character.c_class = assign_traits('class', dict_classes)
    # Prompts user for character's special item
    new_character.c_item = assign_traits('special item', dict_items)

    ## STARTING BASE ATTRIBUTES ##
    # Assigns character base strength
    new_character.c_strength = assign_base_points(
                                   new_character.c_race, 'Strength',
                                   new_character.c_item)
    # Assigns character base dexterity
    new_character.c_dexterity = assign_base_points(
                                    new_character.c_race, 'Dexterity',
                                    new_character.c_item)
    # Assigns character base constitution
    new_character.c_constitution = assign_base_points(
                                       new_character.c_race, 'Constitution',
                                       new_character.c_item)
    # Assigns character base knowledge
    new_character.c_knowledge = assign_base_points(
                                    new_character.c_race, 'Knowledge',
                                    new_character.c_item)
    # Assigns character base charisma
    new_character.c_charisma = assign_base_points(
                                   new_character.c_race, 'Charisma',
                                   new_character.c_item)
    # Holds starting base values for attributes
    base_attributes = {
        'Strength' : new_character.c_strength,
        'Dexterity' : new_character.c_dexterity,
        'Constitution' : new_character.c_constitution,
        'Knowledge' : new_character.c_knowledge,
        'Charisma' : new_character.c_charisma
    }

    # Updates attribute points and point pool
    dict_updated_att_points, updated_point_pool = update_attributes(
                                    base_attributes, new_character.c_class)

    ## Total Attributes ##
    # Assigns character total strength
    new_character.c_strength = dict_updated_att_points['Strength']
    # Assigns character total dexterity
    new_character.c_dexterity = dict_updated_att_points['Dexterity']
    # Assigns character total constitution
    new_character.c_constitution = dict_updated_att_points['Constitution']
    # Assigns character total knowledge
    new_character.c_knowledge = dict_updated_att_points['Knowledge']
    # Assigns character total charisma
    new_character.c_charisma = dict_updated_att_points['Charisma']

    ## MODIFIERS ##
    # Assigns character strength modifier
    new_character.c_strength_mod = dict_modifiers[
                                       new_character.c_strength]
    # Assigns character dexterity modifier
    new_character.c_dexterity_mod = dict_modifiers[
                                       new_character.c_dexterity]
    # Assigns character constitution modifier
    new_character.c_constitution_mod = dict_modifiers[
                                       new_character.c_constitution]
    # Assigns character knowledge modifier
    new_character.c_knowledge_mod = dict_modifiers[
                                       new_character.c_knowledge]
    # Assigns character charisma modifier
    new_character.c_charisma_mod = dict_modifiers[
                                       new_character.c_charisma]

    ## HD HP & AC ##
    # Assigns character hit die
    new_character.c_hd = dict_classes[new_character.c_class]['Hit Die']
    # Assigns character hit points
    base_hp = dict_classes[new_character.c_class]['Base HP']
    new_character.c_hp = base_hp + new_character.c_constitution_mod
    # Assigns character armor class
    base_ac = 10
    new_character.c_ac = base_ac + new_character.c_dexterity_mod

    # Returns Character object
    return new_character

## Main portion of program
if __name__ == '__main__':
    # Introduces user to program
    introduction()

    # Holds characters created
    character_list = []

    # Holds user input
    new_input = ""

    # Creates new characters until user chooses to exit
    while new_input != "exit":
        new_input = input("\nCreate a new character? (Y/N): ")
        # Converts input to lowercase
        new_input = new_input.lower()
        if (new_input == "yes" or new_input == "y"):
            print("Ok, let's make a character!\n")
            print("===========================================================")
            # Creates new character
            new_character = create_character()
            # Adds new character to list
            character_list.append(new_character)
        # Exits program
        elif (new_input == "no" or new_input == "n" or
              new_input == "exit" or new_input == "x"):
            new_input = "exit"
            # Displays characters created
            for character in character_list:
                print("\n----------------------------------")
                print("\tCharacter", character_list.index(character) + 1)
                print("----------------------------------")
                display_character(character)
                print("----------------------------------")
            input("\nPress enter to exit.")
            break