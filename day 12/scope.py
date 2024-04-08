############ SCOPE ############

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # It can be acessed. because it is in local scope (inside the function)

# Global Scope
player_hp = 10

def drink_potion():
    potion_strength = 2
    print(player_hp)

drink_potion()

# There is no Block Scope

game_level = 3

def spawn_mob():
    mob = ['Zombie', 'Skeleton', 'Creeper']
    if game_level < 5:     # Create a loop or while doesn't create a local scope, but creating a def...
        new_mob = mob[0] 

    print(new_mob)
