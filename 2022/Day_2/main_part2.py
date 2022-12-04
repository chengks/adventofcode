rps_combinations = {
    "X": {
        "A": "D",
        "B": "L",
        "C": "W"
    },
    "Y": {
        "A": "W",
        "B": "D",
        "C": "L"
    },
    "Z": {
        "A": "L",
        "B": "W",
        "C": "D"
    }
}

forced_results = {
    "X" : "L",
    "Y" : "D",
    "Z" : "W"
}

points = {
    "W" : 6,
    "D" : 3,
    "L" : 0,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

with open("input.txt") as file_in:
    answer = 0 
    for line in file_in:
        input = line.split("\n")[0].split(" ")
        result = forced_results[input[1]]
        chosen_hand = ""
        for i in ["X", "Y", "Z"]:
            chosen_hand = i if rps_combinations[i][input[0]] == result else chosen_hand       
        answer += points[chosen_hand] + points[result]
    print(answer)
   