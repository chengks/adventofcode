with open("input.txt") as file_in:
    answer = 0 
    for line in file_in:
        input = line.split("\n")[0]
        # seperate in 2 compartments
        middle_index = int(len(input)/2)
        first_compartment = input[:middle_index] 
        second_compartment = input[middle_index:len(input)] 

        # find duplicate letter
        found = False
        for fcl in first_compartment: 
            if found: 
                break
            for scl in second_compartment:
                if fcl == scl: 
                    # sum the duplicate letter
                    if fcl >= 'a' and fcl <= 'z':
                        answer += ord(fcl) - 96
                    else:
                        answer += ord(fcl) - 38
                    found = True
                    break
                    
    print(answer)