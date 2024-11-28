#Goal: Objective
#box =+---+---+---+---+---+---+
#     | 	| 1 | 2 | 3 | 4 | 5 |
#     +---+---+---+---+---+---+
#     |'a'|1a |2a |3a |4a |5a |
#     +---+---+---+---+---+---+
#     |'b'|1b |2b |3b |4b |5b |
#     +---+---+---+---+---+---+
#			|'c'|1c |2d |3c |4c |5c |
#			+---+---+---+---+---+---+
#			|'d'|1d |2e |3e |4e |5e |
#			+---+---+---+---+---+---+
#

#Plan:
	#1. Gen. (x,y) co-ordinates in range nx, ny
	#2. Gen. grid table (rows, column), and assign display to index co-ordiantes (x,y)
	#3. Test select (x,y) index co-ordinate replace display value
	#4. 
#Assign

import console
console.clear()



###>>>Prep. Empty dictionary
grid = {}
for x in range(11): 
    for y in range(11):  
        grid[(x, y)] = f"・"

###>>>Prep. grid gen. function
def display_grid(dict, x, y):
    for x in range(x):
        rows = [str(dict[(x, y)]) for y in range(y)]
        print(" |".join(rows))
        
###>>>Prep. modify grid (key:value) value function
###>>>Variables: [grid = dictionary], [x,y = key], [value = key:value]
def update_cell(dict, x, y, value):
    if (x, y) in dict:
        dict[(x, y)] = value
    ###>>>This is expaining how to id a valid dictionary, stating it has to have (x, y) key and a value
    else:
        print(f"Cell ({x}, {y}) is out of bounds.")


				###>>>AXIS labeling
for y in range(11):  
	grid[(0, y)] = f"{y}X" 
for x in range(11):
	grid[(x, 0)] = f"{x}Y"
for y in range(1):
	grid[(0,y)] = f"XY"



				###>>>hidden 'ship' id grid
ship_grid = {}
for x in range(12): 
    for y in range(12):  
        ship_grid[(x, y)] = 0
        
				###>>>random battleship coordinate generation
import random
random.randint(1, 10)

bship1 = [random.randint(2, 9), random.randint(2, 9)]
bship1a = [bship1[0], bship1[1] + 1]
bship1b = [bship1[0], bship1[1] - 1]

bship2 = [random.randint(2, 9), random.randint(2, 9)]
while bship2[0] == bship1[0] and bship2[1] == bship1[1]:
	bship2 = [random.randint(2, 9), random.randint(2, 9)]	
bship2a = [bship2[0] + random.randint(-1, 1), bship2[1]]

bship3 = [random.randint(4, 7), random.randint(4, 7)]
while (bship3[0] == bship1[0] and bship3[1] == bship1[1]) or (bship3[0] == bship2[0] and bship3[1] == bship2[1]):
	bship3 = [random.randint(4, 7), random.randint(4, 7)]

bship3a = [bship3[0], bship3[1] - 1]
bship3b = [bship3[0], bship3[1] + 1]
bship3c = [bship3[0] + 1, bship3[1]]
bship3d = [bship3[0] - 1, bship3[1]]

print("\nShip1: ", bship1)
print("Ship2: ", bship2)
print("Ship3: ", bship3)

					###>>>battleship coordinate mapping onto id-grid
for x in range(11):
	ship_grid[(bship1[0], bship1[1])] = 1
	ship_grid[(bship2[0], bship2[1])] = 1
	ship_grid[(bship3[0], bship3[1])] = 1
	
	ship_grid[(bship1a[0], bship1a[1])] = 1
	ship_grid[(bship1b[0], bship1b[1])] = 1
	
	ship_grid[(bship2a[0], bship2a[1])] = 1
	
	ship_grid[(bship3a[0], bship3a[1])] = 1
	ship_grid[(bship3b[0], bship3b[1])] = 1
	ship_grid[(bship3c[0], bship3c[1])] = 1
	ship_grid[(bship3d[0], bship3d[1])] = 1
	
	

print("\n")
display_grid(ship_grid, 11, 11)

print("\n")
display_grid(grid, 11, 11)

screen = "__________________"
count = 20

print(screen * 5)
print("\n\nThis is battleships! Pirates are hiding in the coast, and planning to pillage the village!")
print("The villagers have requested your wisdom defend their village.")
print("You have been given control over the coastal defense canon.")
print("However, the poor village only has: {", count, "} cannon balls.")
print("Use your wisdom to efficently shoot down the pirates with the cannon balls available!.")
print("HINT: From the information the villagers gathered, the Pirates operate 3 ships with silouttes of the following: ")
print("ship1:{   |	  ")
print(" 		 --+--  ")
print(" 	  		|    }")
print("\nship2:{ --+-- }")
print("\nship3:{   +   }")


					###>>>Active battleship id=1, so as long as any [key in ship_grid as assigned value = 1], continue game
					###>>>If all [key-value not 1], indicates all ship hit so exit while loop
while any(value == 1 for value in ship_grid.values()):
	print("\n Please selecet a Co-ordinate to hit: ")		
	py = int(input("\nChoose a X-Coordinate:"))
	while py > 10 or py < 1:
		py = int(input("\nThats not a Coordinate on the Map! \nPlease choose a X-Coordinate between (1, 1) to (10, 10):"))
	px = int(input("Choose a Y-Coordinate:"))
	while px > 10 or px < 1:
		px = int(input("\nThats not a Coordinate on the Map! \nPlease choose a Y-Coordinate between (1, 1) to (10, 10): "))
	


	bomb = random.randint(0,2)
	g = 0
	if ship_grid[(px, py)] == 2:
		bomb = 1
		g = g + 1
		print("\n!!EXSPLOOOOJION!!")
		print("The obliterated Pirate ship exploded and scattered to the surrounding! ƪ( ̆⌣ ̆)ʃ ")
	if bomb == 1:
		if g == 1:
			print("")
		else:
			print("\n!!DOKAAN!! ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ")
			print("A surprise Cluster Bomb!")
		bombardment = [(px + 1, py), (px - 1, py), (px, py + 1), (px, py - 1)]
		for n in bombardment:
			if ship_grid[n] == 1 or ship_grid[n] == 2:
				update_cell(grid, n[0] , n[1], '打')
				update_cell(ship_grid, n[0], n[1], 2)
			if ship_grid[n] == 0:
				update_cell(grid, n[0], n[1], '外')
			
			
	
	
	
	if ship_grid[(px, py)] == 1:
		update_cell(grid, px, py, '打')
		update_cell(ship_grid, px, py, 2)
		count = count - 1
		print("\nKABOOM!! ᕦ(ò_óˇ)ᕤ")
		print("You hit a Pirate Ship!")
	elif ship_grid[(px, py)] == 0:
		if grid[px, py] == '外':
			print("You already hit water there silly!")
			print("Choose a different co-ordinate.")
		else:
			update_cell(grid, px, py, '外')
			count = count - 1
			print("\nSPLOOSH!!")
			print("You missed! (*´ー｀*)")
		
		if ship_grid[(px + 1, py)] == 1 or ship_grid[(px - 1, py)] == 1 or ship_grid[(px, py + 1)] == 1 or ship_grid[(px, py - 1)] == 1:
			print("A Pirates shivers nearby... ٩( ᐛ )و")
		else:
			print("No presence of Pirates nearby... ") 
		print(screen * 5)
	elif ship_grid[(px, py)] == 2:
		print("\nYou already hit the Pirate Ship there!")
		print("Choose a different Co-ordinate")
		
	if count == 10:
		print("The Villagers information network intercepted the Pirates communication!")
		print("However, the information was encrypted and they don't know how to read it...'")
		print(display_grid(ship_grid, 11, 11))
		
	if count == 0:
		break
	print("You have: {", count, "} cannon balls left.")
	print(screen * 5)
	print("\nThis is update grid: ")
	print(display_grid(grid, 11, 11))
	

if count == 0:
		print("\nYou don't have any more cannon balls left!'")
		print("Oh no! The Pirates made it to land...")
		print("You were kidnapped by the Pirates, never to be seen again... (T-T)7")
else: 
	print("\nHullay!! Hullay!! You are a saviour! You sent all the Pirates to the bottom of the sea! ^_^ ")
	print("And thus, you became the hero of the village, forever to be sung in legends...")
		
	





