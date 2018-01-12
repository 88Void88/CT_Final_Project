input = input()

grammar = {
    "S'": ["S"],
    "S": ["GA", "ZA", "LA", "HB"],
    "A": ["PC"],
    "B": ["PE"],
    "C": ["YD", "VD"],
    "D": ["QE"],
    "E": ["YR", "VR"],
    "Y": ["VY", "VV"],
    "H": ["c"],
    "G": ["g"],
    "Z": ["r"],
    "L": ["l"],
    "P": ["("],
    "R": [")"],
    "Q": [","],
    "V": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

grammar_reverse = {
    "S": "S'",
    # goto
    "GA": "S",
    # rectangle
    "ZA": "S",
    # line
    "LA": "S",
    # circle
    "HB": "S",
    # 2 params
    "PC": "A",
    # 1 params
    "PE": "B",
    "YD": "C",
    "VD": "C",
    "QE": "D",
    "YR": "E",
    "VR": "E",
    # number
    "VY": "Y",
    "VV": "Y",
    "0": "V",
    "1": "V",
    "2": "V",
    "3": "V",
    "4": "V",
    "5": "V",
    "6": "V",
    "7": "V",
    "8": "V",
    "9": "V",
    # other terminals
    "(": "P",
    ")": "R",
    ",": "Q",
    "c": "H",
    "g": "G",
    "r": "Z",
    "l": "L"
}

# ex input: c(3)
layers = [[]]
divisions = [[]]
# create input divisions
for i in range(0, len(input)):
    divisions.append([])
    for x in range(0, len(input) - i):
        segment = ""
        curr_index = x
        for i in range(0, i + 1):
            segment = segment + input[curr_index]
            curr_index = curr_index + 1
        divisions[i].append(segment)

divisions.pop()
# print(divisions)

count = 0
for i in divisions:
    layers.append([])
    for j in i:
        if len(j) == 1:
            layers[count].append(grammar_reverse.get(j))
        else:
            for x in range(1, len(j)):
                segmentA = j[:x]
                rowA = len(segmentA) - 1
                segmentB = j[x:]
                rowB = len(segmentB) - 1
                ruleA = layers[rowA][divisions[rowA].index(segmentA)]
                ruleB = layers[rowB][divisions[rowB].index(segmentB)]
                if ruleA is None and ruleB is None:
                    layers[count].append(None)
                else:
                    layers[count].append(grammar_reverse.get(ruleA + ruleB))
    count += 1

print(layers)
