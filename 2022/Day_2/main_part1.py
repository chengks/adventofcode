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
        result = rps_combinations[input[1]][input[0]]
        answer += points[input[1]] + points[result]
    print(answer)