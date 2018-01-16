input = input("Enter string: ")

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

terminals = {
    "c": "func",
    "g": "func",
    "r": "func",
    "l": "func",
    "0": "param",
    "1": "param",
    "2": "param",
    "3": "param",
    "4": "param",
    "5": "param",
    "6": "param",
    "7": "param",
    "8": "param",
    "9": "param",
    "VY": "param",
    "VV": "param",
    # other terminals
    "(": "others",
    ")": "others",
    ",": "param"
}

def analyze_syntax(string):
    input = string
    # ex input: c(3)
    layers = []
    divisions = []
    correct = False
    # create input divisions
    for i in range(0, len(input)):
        divisions.append([])
        for x in range(0, len(input) - i):
            segment = input[x:x+i+1]
            divisions[i].append(segment)

    # print(divisions)
    original = divisions[0]
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
    divisions.reverse()
    # for div in divisions:
    #     print(div)
    # for layer in layers:
    #     print(layer)

    if grammar_reverse.get(layers[0][0][0]) == "S'":
        print("Syntax is correct")
        correct = True
    else:
        print("Syntax is incorrect")
        return [False]

    func = ""
    params = []

    if correct:
        queue = []
        history = []
        row = 0
        col = 0
        start = layers[row][col][0]
        queue.append([start, row, col])
        while len(queue) != 0:
            # print()
            # print(queue)
            curr = queue.pop()
            history.append(curr)
            curr_row = curr[1]
            curr_col = curr[2]
            possible = grammar.get(curr[0])
            # print(curr_row)
            if curr_row == count - 1:
                context = terminals.get(str(grammar.get(curr[0])[0]))
                # print("{} {}".format(str(grammar.get(curr[0])[0]), context))
                if context is "func":
                    func = grammar.get(curr[0])
                elif context is "param":
                    params.append(original[curr_col])
                continue

            for a in range(1, count - curr_row):
                x1 = curr_col + a
                y1 = curr_row + a
                x2 = curr_col
                y2 = count - a
                # print("{},{}".format(curr_col, curr_row))
                # print("{},{}|{},{}".format(x1, y1, x2, y2))
                content1 = layers[y1][x1]
                content2 = layers[y2][x2]
                found = False
                for first in content1:
                    if type(first) is not str:
                        continue
                    for second in content2:
                        if type(second) is not str:
                            continue
                        find = second+first
                        # print(find)
                        if find in possible:
                            queue.append([first, y1, x1])
                            queue.append([second, y2, x2])
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
    return [True, func, params]
    # print(history)
    # print(func)
    # print(params)

print(analyze_syntax(input))
