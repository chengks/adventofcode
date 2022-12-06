with open("input.txt") as file_in:
    number = []
    answer = 0
    current = 0
    l = []
    for line in file_in:
        if(line == "\n"):
            answer = current if current > answer else answer
            l.append(current)
            current = 0
            continue
        current += int(line)
    sorted_list = sorted(l, reverse=True)
print(answer)
print(sorted_list[0] + sorted_list[1] + sorted_list[2])
