
trees=[]
with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        tmp = []
        for t in line:
            
            tmp.append(int(t))
        trees.append(tmp)

total = 0
total += (len(trees[0])) * 2 + (len(trees) * 2 - 4)

for idx1, i in enumerate(trees):
    if idx1 == 0 or idx1 == len(trees)-1:
        continue
    
    for idx2, j in enumerate(i):
        if idx2 == 0 or idx2 == len(trees)-1:
            continue
        
        right = all(l < j for l in i[idx2+1::])
        left = all(l < j for l in i[::-1][len(i)-idx2::])
        pointer = 0
        vertarr = []
        while pointer < len(trees):
            vertarr.append(trees[pointer][idx2])
            pointer += 1
        up = all(l < j for l in vertarr[::-1][len(vertarr)-idx1::])
        down = all(l < j for l in vertarr[idx1+1::])

        if right or left or up or down:
            total += 1
    
print(total) 