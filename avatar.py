
class Avatar:

# constructor method used to create multiple unique attributes for each individual avatar
    def __init__(self, name: str, color: str, health: int, power: int, level:int):

        self._name = name 
        self._color = color
        self.health = health 
        self.power = power
        self.level = level

#getter methods for each attribute used to read attribute values for given class instance
    @property
    def name(self):
        return self._name
    
    @property
    def color(self):
        return self._color
    
    @property
    def health(self):
        return int(self._health)
    
    @property
    def power(self):
        return int(self._power)
    
    @property
    def level(self):
        return int(self._level)
    
    #setter methods used to write or alter class attributes for any given player
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @color.setter
    def color(self, new_color):
        self._color = new_color

    #checks if the health is negative and if it is sets it to zero

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self.health = 0
            print("Avatar must have at least 1 health")
        else:
            self._health = new_health

    @power.setter
    def power(self, new_power):
        if new_power < 0:
            self._power = 1
            print("Avatar must have at least 1 attack power")
        else:
            self._power = new_power

    #checks if the level is less than or equal to zero and if so sets the level to 1

    @level.setter
    def level(self, new_level):
        if new_level <= 0:
            self.level = 1
            print("Avatar's level must be positive")
        else:
            self._level = new_level

    #simple attack method that sets the power of the players attack equal to their level
    
    def attack(self):
        print(f"{self.name} attacks and deals {self._power} health points of damage!")

    #taking damage method that checks to see if the damage taken is a positive value and if so removes it from the platers health
    #then check the health value again and prints differnt statements depending in what the players health is at
    #also doesn't allow for damage to be negative

    def take_damage(self, damage_taken):
        if damage_taken > 0:
            self._health -= damage_taken
            if self._health > 0:
                print(f"{self.name} has taken {damage_taken} damage and has {self._health} health points remaining!")
            elif self._health <= 0:
                self.health = 0
                print(f"{self.name} has taken {damage_taken} damage and has been knocked unconscious!")
        else:
            print("Damage must be a positive amount.")

    #level up method that first checks to see if the player is still alive and if they are adds one level and 1o hp 
    #if the player was knocked out it will print a different statement and reset the players health back to 100

    def level_up(self):
        if self._health > 0:
            self._level += 1
            self._health += 10
            print(f"{self._name} has leveled up to level {self._level}!")
            print(f"{self.name} has gained 10 extra hit points from leveling up and now has {self._health} health points!")
        else:
            self._health += 100
            print(f"\n{self.name} has gotten some rest and regaind {self.health} health points!")

    #simple method to see the current players avater traits

    def avatar_traits(self):
        return f"Your avatar {self._name} is {self._color}, has {self._health} health points, {self._power} attack power, and is level {self._level}"
        



    
    