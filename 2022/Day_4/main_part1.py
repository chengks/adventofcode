with open("input.txt") as file:
    l = []
    while (line := file.readline().rstrip()):
        l.append(line)

    answer = 0
    for ps in l:
        p1 = [int(i) for i in ps.split(',')[0].split('-')] 
        p2 = [int(i) for i in ps.split(',')[1].split('-')] 
        if (p2[0] in range(p1[0], p1[1]+1) and p2[1] in range(p1[0], p1[1]+1)) or p1[0] in range(p2[0], p2[1]+1) and p1[1] in range(p2[0], p2[1]+1):
            answer += 1
    print(answer)