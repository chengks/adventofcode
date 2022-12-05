from collections import deque
import re

stack1 = deque(["N", "D", "M", "Q", "B", "P", "Z"])
stack2 = deque(["C", "L", "Z", "Q", "M", "D", "H", "V"])
stack3 = deque(["Q", "H", "R", "D", "V", "F", "Z", "G"])
stack4 = deque(["H", "G", "D", "F", "N"])
stack5 = deque(["N", "F", "Q"])
stack6 = deque(["D", "Q", "V", "Z", "F", "B", "T"])
stack7 = deque(["Q", "M", "T", "Z", "D", "V", "S", "H"])
stack8 = deque(["M", "G", "F", "P", "N", "Q"])
stack9 = deque(["B", "W", "R", "M"])

stacks = {
    1: stack1,
    2: stack2,
    3: stack3,
    4: stack4,
    5: stack5,
    6: stack6,
    7: stack7,
    8: stack8,
    9: stack9,
}

regex = re.compile(r'move ([0-9]*) from ([0-9]*) to ([0-9]*)', flags=re.IGNORECASE)

with open("input.txt") as file:
    l = []
    while (line := file.readline().rstrip()):
        l.append(regex.findall(line)[0])
        
    for s in l: 
        from_stack = stacks[int(s[1])]
        to_stack = stacks[int(s[2])]
        move = int(s[0])
        
        idx = 0
        tmp = deque()
        while idx < move:
            tmp.append(from_stack.pop())
            idx += 1
        
        while len(tmp) > 0:
            to_stack.append(tmp.pop())
            
    print(f"{stack1.pop()}{stack2.pop()}{stack3.pop()}{stack4.pop()}{stack5.pop()}{stack6.pop()}{stack7.pop()}{stack8.pop()}{stack9.pop()}")
        
