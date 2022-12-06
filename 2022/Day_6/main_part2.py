with open("input.txt") as file:
    input = ""
    while (line := file.readline().rstrip()):
        input = line
    
    answer = 0
    for idx, s in enumerate(input):
        pos = 1
        duplicate = False       
        sub_list = [s]
        while pos < 14 and idx + pos < len(input):
            sub_list.append(input[idx + pos])
            pos += 1

        for idx2,c in enumerate(sub_list):
            duplicate = any([c in c2 for c2 in sub_list[idx2+1::]])
            if duplicate:
                break;
            
            
        if not duplicate:
            answer = idx + 14
            break;
    
    print(answer)    