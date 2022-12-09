
trees=[]
with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        tmp = []
        for t in line:
            
            tmp.append(int(t))
        trees.append(tmp)

total = 0

def countTrees(tree, listOfTrees) -> int:
    for idx, t in enumerate(listOfTrees):  
        if tree <= t:
            return idx + 1
        
    return len(listOfTrees)

for idx1, i in enumerate(trees):
    for idx2, j in enumerate(i):
        right = countTrees(j, i[idx2+1::])
        left = countTrees(j, i[::-1][len(i)-idx2::])
        pointer = 0
        vertarr = []
        while pointer < len(trees):
            vertarr.append(trees[pointer][idx2])
            pointer += 1
        up = countTrees(j, vertarr[::-1][len(vertarr)-idx1::])
        bottom = countTrees(j, vertarr[idx1+1::])

        treeScenic = left * right * up * bottom
        print(f'{idx1} {idx2} {j} l {left} r {right} u {up} b {bottom} t {treeScenic}')
            
        if total < treeScenic:
            total = treeScenic
    
print(total) 