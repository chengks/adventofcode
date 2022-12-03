with open("input.txt") as file_in:
    number = []
    answer = 0
    current = 0
    for line in file_in:
        if(line == "\n"):
            answer = current if current > answer else answer
            current = 0
            continue
        current += int(line)
        
print(answer)
