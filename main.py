from enemy import Enemy
from avatar import Avatar

#function used to check that the player inputed valid traits
#just checking to make sure its not an empty string and returning their input

def get_valid_string(message):
    character_traits = input(f"What would you like your {message} to be?: ").strip()
    while character_traits == "":
        character_traits = input(f"   {message} must include at least one character. Enter {message}: ").strip()
    return character_traits

#checking to see if the player inputed an int for level and health attributes 

def get_valid_int(message):
    valid_num = False
    number_input = input(f"what is your {message}?: ").strip()
    while not valid_num:
        if number_input == "":
            number_input = input(f"   must not be empty value. Enter {message}: ")
        else:
            try:
                number = int(number_input)
                return number
            except ValueError:
                number_input = input(f"  Must be a valid number. Enter {message}: ")

# attack function used to ask the player if they would like to attack and if so calls the attack method from the avatar class

def avatar_attack(player):
    valid_entry = False

    entry = input(f"Would you like {player.name} to attack (Y or N)?: ").strip().lower()
    while not valid_entry:
        if entry in ("y", "n"):
            valid_entry = True
        else:
            entry = input("  Please enter Y or N: ").strip().lower()
    if entry == "y":
        player.attack()
    else:
        print(f"{player.name} has skipped this attacking phase.")


#main function used to print all of the inputs and prompts 

def main():

    print("\n   CREATE YOUR AVATAR   ")
    avatar_name = get_valid_string("avatars name")
    avatar_color = get_valid_string("avatars color")
    avatar_health = get_valid_int("avatars health")
    avatar_level = get_valid_int("avatars level")

    # create an avatar
    player_1 = Avatar(avatar_name, avatar_color, avatar_health, avatar_level)

    print("\nBased on what you enterd: ", end="")
    print(player_1.name, end=" ")
    print(player_1.color, end=" ")
    print(player_1.health, end =" ")
    print(player_1.level)

    print(player_1.avatar_traits())

    # attack with avatar 
    print("\n   ATTACKING PHASE HAS BEGUN!!!   ")
    avatar_attack(player_1)
    print("\n The opposing player has chosen to attack!")
    player_1.take_damage(30)
    print("\n   ATTACKING PHASE OVER!!!   ")
    player_1.level_up()



if __name__ == "__main__":
    main()