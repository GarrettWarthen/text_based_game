
class Enemy:

    def __init__(self, name, enemy_type, health, power):

        self._enemy_type = enemy_type
        self.health = health
        self._name = name
        self.power = power

    @property
    def name(self):
        return self._name
    
    @property
    def enemy_type(self):
        return self._enemy_type
    
    @property
    def health(self):
        return int(self._health)
    
    @property
    def power(self):
        return int(self._power)
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @enemy_type.setter
    def enemy_type(self, new_enemy_type):
        self._enemy_type = new_enemy_type

    @power.setter
    def power(self, new_power):
        self._power = new_power

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
            print("Enemy must have at least 1 health")
        else:
            self._health = new_health

    def attack(self):
        print(f"{self._name} attacks and deals {self._power} health points of damage!")

    def take_damage(self, damage_taken):
        if damage_taken > 0:
            self._health -= damage_taken
            if self._health > 0:
                print(f"{self._name} has taken {damage_taken} damage and has {self._health} health points remaining!")
            elif self.health <= 0:
                self.health = 0
                print(f"{self._name} has taken {damage_taken} damage and has been knocked unconscious!")
        else:
            print("Damage must be a positive amount.")

    def enemy_traits(self):
        return f"This enemy is a {self._name} whos enemy type is a {self._enemy_type} that deals {self._power} points of damage and has {self._health} health points"
    