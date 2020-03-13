from random import choice
"""Function Definations"""
cave_numbers = list(range(0,20))
unvisited_caves = list(range(0,20))
cave_names=["Arched cavern",
           "Twisty Passage",
           "Drpping cave",
           "Dusty crawlspace",
           "Underground lake",
           "Black pit",
           "Fallen acve",
           "Shallow pool",
           "Icy Underground river",
           "Sandy hollow",
           "Wolf firepit",
           "Tree root cave",
           "Narrow edge",
           "Winding steps",
           "Echoing chamber",
           "Dusty cave",
           "Gloomy cave",
           "Low ceilinged cave",
           "wumpus lair",
           "spooky chasm"]

def setup_caves(cave_number):
    """Creates a starting list of cave"""
    caves=[]
    for cave in cave_number:
        caves.append([])
    return caves
def create_tunnel(cave_from, cave_to):
    """Creates a tunnel from cave_from to cave_to"""
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)
def visit_caves(cave_number):
    """Mark a cave as visited"""
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)
def choose_cave(cave_list):
    """Pick a cave from list, provided that the cave has less than three tunnels"""
    cave_number= choice(cave_list)
    while(len(caves[cave_number])>=3):
        cave_number=choice(cave_list)
    return cave_number

def print_caves():
    """print out the current cave structure"""
    for number in cave_numbers:
        print(str(number) + " : " +str(caves[number]) )
    print ("_______________________")

def link_caves():
    """make sure all of the caves are connected with two way tunnel"""
    while unvisited_caves!=[]:
        this_cave=choose_cave(visited_caves)
        next_cave=choose_cave(unvisited_caves)
        create_tunnel(this_cave,next_cave)
        visit_caves(next_cave)
def finish_caves():
    """link the one way tunnel with one way tunnel"""
    for cave in cave_numbers:
        while(len(caves[cave])<3):
            passage_to = choose_cave(cave_numbers)
            caves[cave].append(passage_to)
def print_location(player_location):
    """Tell the player where thay are"""
    print("You are in : ",cave_names[player_location])
    print("From here you can see caves: ")
    neighbors = caves[player_location]
    for tunnel in range(0,3):
        next_cave=neighbors[tunnel]
        print("      "+str(tunnel+1)+"-" + cave_names[next_cave])
    if wumpus_location in neighbors:
        print("I smell a wumpus")
def ask_for_cave():
    """Ask the player to choose a cave from their curreent cave location"""
    player_input=int(input("Which cave "))
    if player_input in [1,2,3,]:
        index = player_input-1
        neighbors = caves[player_location]
        cave_number = neighbors[index]
        return cave_number
        
    else:
        print (str(player_input) + " ?")
        print("thats not the direction i can see")
        return False
def get_action():
    """Find out what player wants to do"""
    print("what do you do next? ")
    print("m) Move")
    print("a) Fire an Arrow!")
    action = str(input("> "))
    if action == 'a' or action == 'm':
        return action
    else:
        print(action + "?")
        print("Wrong Input")
        return None
def do_movement():
    print("Moving ----")
    new_location = ask_for_cave()
    if new_location is None:
        return player_location
    else:
        return new_location
def do_shooting():
    print ("Firing-----")
    shoot_at = ask_for_cave()
    if shoot_at is None:
        return False
    if shoot_at == wumpus_location:
        print("Twang ----- Argh! You shot the wumpus")
        print("well done mighty wumpus hunter !")
    else:
        print("Twang ---- Clatter Clatter Clatter ! ")
        print("You wasted your arrow !")
        print("Game Over ")
    return True
visited_caves =[]
caves = setup_caves(cave_numbers)
visit_caves(0)
link_caves()
finish_caves()
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
print("Use Arrow wisely! You only have one arrow")
while player_location == wumpus_location:
    player_location = choice(cave_numbers)
while True:
    print_location(player_location)
    action = get_action()
    if action is None:
        continue
    if action == 'm':
        player_location = do_movement()
        if player_location == wumpus_location:
            print("Argh!! You got eaten by wumpus")
            break
    if action=='a':
        game_over = do_shooting()
        if game_over:
            break
