x = 1
cyclus = 0
next_calc = 20
sum = 0
sprite_pos = 0
sprite = []
for idx, i in enumerate(range(40)):
    sprite.append(' ')

sprite[sprite_pos] = '1'
sprite[sprite_pos+1] = '1'
sprite[sprite_pos+2] = '1'

grid = []

for i in range(6):
    horizontal = []
    for j in range(40):
        horizontal.append(' ')
    grid.append(horizontal)

row = 0
with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        # start of new cycle
        cyclus += 1
        if cyclus % 40 == 0:
            row +=1
        
        if row <= 5:
            grid[row][(cyclus % 40)-1] = '1' if sprite[(cyclus % 40)-1] == '1' else ' ' 

        if cyclus == next_calc:
            sum += cyclus * x
            next_calc += 40
        
        if line.find("addx") == 0:
            cyclus += 1 
            if cyclus % 40 == 0:
                row +=1
            if row <= 5:
                grid[row][(cyclus % 40)-1] = '1' if sprite[(cyclus % 40)-1] == '1' else ' '
                 
            if cyclus == next_calc:
                sum += cyclus * x
                next_calc += 40

            x += int(line.split(" ")[1])
            for idx, i in enumerate(range(40)):
                sprite[idx] = idx

            sprite[x-1] = '1'
            if x <= 39:
                sprite[x] = '1'
            if x+1 <= 39:
                sprite[x+1] = '1'
            continue

print(sum)
for i in grid:
    print(''.join(str(e) for e in i))

        
        