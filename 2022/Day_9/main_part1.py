from enum import Enum
import re

class Direction(Enum):
    R = (0, 1)
    L = (0, -1)
    U = (1, 0)
    D = (-1, 0)
    
        
    
print(Direction["R"])
regexDirection = re.compile(r'^([a-z]) ([0-9]*)$', flags=re.IGNORECASE)
H = (0, 0)
T = (0, 0)
tailPath = {(0,0)}
surroundings = [
    (0, 0),
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)
]

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        d = regexDirection.findall(line)[0]

        for i in range(int(d[1])):
            prevHpos = (H[0], H[1])
            H = (H[0] + Direction[d[0]].value[0], H[1] + Direction[d[0]].value[1])
            print(f'1 {T} {H}')
            distance = (H[0] - T[0], H[1] - T[1])
            if distance not in surroundings:
                T = prevHpos
                print(f'2 {T} {H}')
                tailPath.add(T)

print(len(list(tailPath)))        