from enum import Enum
import re

class Direction(Enum):
    N = (0, 0)
    R = (0, 1)
    L = (0, -1)
    U = (1, 0)
    D = (-1, 0)
    RU = (1, 1)
    RD = (-1, 1)
    LU = (1, -1)
    LD = (-1, -1)
       
regexDirection = re.compile(r'^([a-z]) ([0-9]*)$', flags=re.IGNORECASE)
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

start = (0, 0)
snake = []
for i in range(10):
    snake.append(start)
    
def moveTo(distance) -> Direction:
    if distance ==  (0, 2): return Direction.R
    if distance == (0, -2): return Direction.L
    if distance == (2, 0): return Direction.U
    if distance == (-2, 0): return Direction.D
    if distance == (1, 2) or distance == (2, 1) or distance == (2, 2): return Direction.RU
    if distance == (1, -2) or distance == (2, -1) or distance == (2, -2): return Direction.LU
    if distance == (-1, 2) or distance == (-2, 1) or distance == (-2, 2): return Direction.RD
    if distance == (-1, -2) or distance == (-2, -1) or distance == (-2, -2): return Direction.LD
    
    return Direction.N

with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        d = regexDirection.findall(line)[0]

        for i in range(int(d[1])):
            for idx, cn in enumerate(snake):
                # print(f'Step 1 {idx} {snake}')
                
                if idx == 0:
                    snake[0] = (snake[0][0] + Direction[d[0]].value[0], snake[0][1] + Direction[d[0]].value[1])
                    # print(f'Step 2 {idx} {snake}')
                else:
                    prevN = snake[idx-1]
                    distance = (prevN[0] - cn[0], prevN[1] - cn[1])
                    
                    if distance not in surroundings:
                        move = moveTo(distance)
                        # print(f'{distance} {move}')
                        snake[idx] = (snake[idx][0] + move.value[0], snake[idx][1] + move.value[1])
                        if idx == 9:
                            tailPath.add(snake[idx])
                    # print(f'Step 3 {idx} {snake}')
                
            # print(f'===============================')
print(len(list(tailPath)))        
