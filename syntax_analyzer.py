input = input("Enter string to be evaluated: ")

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
layers = []
divisions = []
# create input divisions
for i in range(0, len(input)):
    divisions.append([])
    for x in range(0, len(input) - i):
        segment = input[x:x+i+1]
        divisions[i].append(segment)

print(divisions)

count = 0
for i in divisions:
    count_col = 0
    layers.append([])
    for j in i:
        layers[count].append([])
        if len(j) == 1:
            layers[count][count_col].append(grammar_reverse.get(j))
        else:
            for x in range(1, len(j)):
                segmentA = j[:x]
                rowA = len(segmentA) - 1
                segmentB = j[x:]
                rowB = len(segmentB) - 1
                ruleA = layers[rowA][divisions[rowA].index(segmentA)]
                ruleB = layers[rowB][divisions[rowB].index(segmentB)]
                for a in ruleA:
                    for b in ruleB:
                        if type(a) is str and type(b) is str:
                            try:
                                layers[count][count_col].remove(None)
                            except ValueError:
                                pass
                            layers[count][count_col].append(grammar_reverse.get(a + b))
                        else:
                            if len(layers[count][count_col]) == 0:
                                layers[count][count_col].append(None)
        count_col += 1
    count += 1

layers.reverse()
for layer in layers:
    print(layer)
if grammar_reverse.get(layers[0][0][0]) == "S'":
    print("Syntax is correct")
else:
    print("Syntax is incorrect")
