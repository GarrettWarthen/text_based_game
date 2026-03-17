from enemy import Enemy
from avatar import Avatar

file_1 = open("game_rules.txt", "r")
file_contents_1 = file_1.read()
file_2 = open("encounter.txt", "r")
file_contents_2 = file_2.read()

character_1 = Avatar("Ash", "Dark Red", 100, 20, 1 )
character_2 = Avatar("Aang", "Blue", 200, 10, 1)

enemy_1 = Enemy("Goblin", "Damage Dealer", 50, 15)


#function used to check that the player inputed valid traits
#just checking to make sure its not an empty string and returning their input

def get_valid_string(message):
    character_traits = input(f"What would you like your {message} to be?: ").strip()
    while character_traits == "":
        character_traits = input(f"   {message} must include at least one character. Enter {message}: ").strip()
    return character_traits

# attack function used to ask the player if they would like to attack and if so calls the attack method from the avatar class

def avatar_attack(player):
    entry = input(f"\nWould you like {player.name} to attack the {enemy_1.name}? (Y or N): ").strip().lower()

    while entry not in ("y", "n"):
        entry = input("  Please enter Y or N: ").strip().lower()

    if entry == "y":
        player.attack()
        return True
    else:
        print(f"{player.name} has skipped this attacking phase.")
        return False

def select_character():

    while True:
        print("\n Select Your Character!")
        print("Character 1: Ash")
        print("Character 2: Aang")

        choice = input("Enter 1 or 2 to select your avatar: ")

        if choice == "1":
            player = character_1
        elif choice == "2":
            player = character_2
        else:
            print(f"{choice} is not a valid entry")
            continue

        print("\n" + player.avatar_traits())

        confirm_choice = input(f"after seeing {player.name}'s stats would you like to use {player.name} (Y or N)?:").lower()
        if confirm_choice == "y":
            return player
        
        

def continue_game():
    entry = input("Are you ready to start the game (Y or N)?: ").strip().lower()

    while entry not in ("y", "n"):
        entry = input("  Please enter Y or N: ").strip().lower()

    if entry == "y":
        return True
    else:
        print("The game has concluded!")
        return False

def customize_avatar(player):
    valid_entry = False

    entry = input(f"Would you like to change your avatars name and color (Y or N)?: ").strip().lower()
    while not valid_entry:
        if entry in ("y", "n"):
            valid_entry = True
        else:
            entry = input("  Please enter Y or N: ").strip().lower()
    if entry == "y":
        avatar_name = get_valid_string("avatars name")
        avatar_color = get_valid_string("avatars color")
        player.name = avatar_name
        player.color = avatar_color
        print("\n   Avatar Has Been Updated!   ")
    else:
        print("Avatar was unchanged!")

def enter_attack_phase(player):

    entry = input(f"Would you like to enter a battle with the {enemy_1.name}? (Y or N): ").strip().lower()
    while entry not in ("y", "n"):
        entry = input("  Please enter Y or N: ").strip().lower()

    if entry == "y":
        print("\n   ATTACKING PHASE HAS BEGUN!!!   ")
        battle(player, enemy_1)
        return True
    else:
        print(f"You chose not to battle the {enemy_1.name} and the game has ended!")
        return False
    
def battle(player, enemy):

    print(f"\n You have enterd a battle with the {enemy.name}!")
    print(enemy.enemy_traits())

    while player.health > 0 and enemy.health > 0:

        if avatar_attack(player):
            enemy.take_damage(player.power)

        if enemy_1.health <= 0:
            print(f"\n{enemy.name} has been defeated!")
            break


        print(f"\nThe {enemy.name} attacks!")
        enemy.attack()

        player.take_damage(enemy.power)

        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    print("\n   ATTACKING PHASE OVER!!!   ")

#main function used to print all of the inputs and prompts 

def main():

    print ("\n   GAME RULES!!!   ")
    print (file_contents_1)
    file_1.close()

    if not continue_game():
        return

    player = select_character()

    print("\n   Customize Avatar   ")
    customize_avatar(player)

    print("\nBased on what you enterd: ", end="")
    print(player.name, end=", ")
    print(player.color, end=" ")

    print("\n" + player.avatar_traits())

    print (file_contents_2)
    file_2.close()

    # attack with avatar
    if not enter_attack_phase(player):
        return
    
    print("\n   Game Over!!!   ")


if __name__ == "__main__":
    main()