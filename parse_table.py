

parseTable = {
    "S": [["R"], ["R"], None, ["R"], None, ["R"], None, ["R"], None, None, None, None, ["R"], ["R"], ["R"], None, ["R"], ["R"], ["R"], ["R"], ["R"], ["R"], ["R"], ["R"], ["R"], ["R"]],
    "R": [[""], ["L","R"], None, ["L","R"], None, ["L","R"], None, [""], None, None, None, None, ["L","R"], ["L","R"], ["L","R"], None, ["L","R"], ["L","R"], ["L","R"], ["L","R"], ["L","R"], ["L","R"], ["L","R"], ["L","R"], ["L","R"], [""]],
    "L": [None, ["E",";"], None, ["A",";"], None, ["C",";"], None, None, None, None, None, None, ["E",";"], ["E",";"], ["E",";"], None, ["E",";"], ["E",";"], ["E",";"], ["E",";"], ["E",";"], ["E",";"], ["E",";"], ["E",";"], ["E",";"], None],
    "E": [None, ["(","E","B","E",")"], None, None, None, None, None, None, None, None, None, None, ["V"], ["V"], ["V"], None, ["N"], ["N"], ["N"], ["N"], ["N"], ["N"], ["N"], ["N"], ["N"], None],
    "A": [None, None, None, ["let","V","=","E"], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    "C": [None, None, None, None, None, ["while","E","do","S","H"], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    "H": [[""], None, None, None, None, None, None, ["else","S"], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    "B": [None, None, None, None, None, None, None, None, ["+"], ["-"], ["*"], [">"], None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    "V": [None, None, None, None, None, None, None, None, None, None, None, None, ["x"], ["y"], ["z"], None, None, None, None, None, None, None, None, None, None, None],
    "N": [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], None],
    "M": [[""], None, [""], None, None, None, [""], None, [""], [""], [""], [""], None, None, None, ["0","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], ["D","M"], None],
    "D": [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"], None]
}

index = {
    ";": 0,
    "(": 1,
    ")": 2,
    "let": 3,
    "=": 4,
    "while": 5,
    "do": 6,
    "else": 7,
    "+": 8,
    "-": 9,
    "*": 10,
    ">": 11,
    "x": 12,
    "y": 13,
    "z": 14,
    "0": 15,
    "1": 16,
    "2": 17,
    "3": 18,
    "4": 19,
    "5": 20,
    "6": 21,
    "7": 22,
    "8": 23,
    "9": 24,
    "$": 25,
    "": 26
}

terminals = index.keys()
variables = parseTable.keys()
