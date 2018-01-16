# ABCDEFGHIJKLPQRVYZ
sentence = input("insert string: ")
grammar = {
    "S'": ["S"],
    "S": ["RA", "LA", "QB", "GC"],
    "A": ["ZH"],
    "B": ["ZJ"],
    "C": ["ZM"],
    "H": ["DI"],
    "I": ["WJ"],
    "J": ["DY"],
    "M": ["EN"],
    "N": ["WO"],
    "O": ["EY"],
    "E": [0, "VD", "XD", 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "D": [0, "XD", 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "X": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Z": ["("],
    "Y": [")"],
    "W": [","],
    "V": ["-"],
    "R": ["r"],
    "L": ["l"],
    "Q": ["c"],
    "G": ["g"]
}

grammar_reverse = {
    "S": ["S'"],
    # goto
    "GC": ["S"],
    # rectangle
    "RA": ["S"],
    # line
    "LA": ["S"],
    # circle
    "QB": ["S"],

    "ZH": ["A"],
    "ZJ": ["B"],
    "ZM": ["C"],
    "DI": ["H"],
    "WJ": ["I"],
    "DY": ["J"],
    "EN": ["M"],
    "WO": ["N"],
    "EY": ["O"],
    # number
    "VD": ["E"],
    "XD": ["E", "D"],
    "0": ["E", "D", "X"],
    "1": ["E", "D", "X"],
    "2": ["E", "D", "X"],
    "3": ["E", "D", "X"],
    "4": ["E", "D", "X"],
    "5": ["E", "D", "X"],
    "6": ["E", "D", "X"],
    "7": ["E", "D", "X"],
    "8": ["E", "D", "X"],
    "9": ["E", "D", "X"],
    # other terminals
    "(": ["Z"],
    ")": ["Y"],
    ",": ["W"],
    "-": ["V"],
    "c": ["Q"],
    "g": ["G"],
    "r": ["R"],
    "l": ["L"]
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
    "-": "param",
    # other terminals
    "(": "others",
    ")": "others",
    ",": "param"
}

def analyze_syntax(sentence):
    string = sentence
    # ex input: c(3)
    layers = []
    divisions = []
    correct = False
    # create input divisions
    for i in range(0, len(string)):
        divisions.append([])
        for x in range(0, len(string) - i):
            segment = string[x:x+i+1]
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
                if type(grammar_reverse.get(j)) is list:
                    layers[count][count_col] = layers[count][count_col] + grammar_reverse.get(j)
                else:
                    if len(layers[count][count_col]) == 0:
                        layers[count][count_col].append(None)
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
                                if type(grammar_reverse.get(a + b)) is list:
                                    # print(a+b)
                                    # print(grammar_reverse.get(a + b))
                                    layers[count][count_col] = layers[count][count_col] + grammar_reverse.get(a + b)
                                else:
                                    if len(layers[count][count_col]) == 0:
                                        layers[count][count_col].append(None)
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

    if type(layers[0][0][0]) is not list and type(layers[0][0][0]) is not str:
        print("Syntax is incorrect")
        return [False]

    if "S" in layers[0][0][0]:
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

            possible = []
            for i in curr[0]:
                possible = possible + grammar.get(i)
                # print(curr_row)
                if curr_row == count - 1:
                    context = terminals.get(str(grammar.get(i)[0]))
                    # print("{} {}".format(str(grammar.get(curr[0])[0]), context))
                    if context is "func":
                        func = grammar.get(i)
                    elif context is "param":
                        params.append(original[curr_col])
                        continue
            for a in range(1, count - curr_row):
                x1 = curr_col + a
                y1 = curr_row + a
                x2 = curr_col
                y2 = count - a

                #comment
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

    # comment
    # print(history)
    # print(func)
    # print(params)

print(analyze_syntax(sentence))
