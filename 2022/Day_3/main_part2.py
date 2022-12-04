def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def find_duplicate(list):
    def find_duplicate(s, list, index):
        if index > len(list) -1 :
            return s
        
        for current in list[index]:
            if current == s:
                found = find_duplicate(current, list, index+1)
                if found != "":
                    return found
        return ""
                      
    for compartment in list:
        for s in compartment:
            found = find_duplicate(s, list, 1)
            
            if found != "":
                return found

with open("input.txt") as file_in:
    answer = 0
    l = []
    for idx,line in enumerate(file_in):
        l.append(line.split("\n")[0])
    chunks = list(divide_chunks(l, 3))
    
    for c in chunks:
        found_letter = find_duplicate(c)
        if found_letter >= 'a' and found_letter <= 'z':
            answer += ord(found_letter) - 96
        else:
            answer += ord(found_letter) - 38
    print(answer)