from parse_table import *
from arithmetic import *
import sys

class ActionToken():
    def __init__(self, transition):
        self.type = transition
    def __repr__(self):
        return "Action[{}]".format("".join(self.type))
    def makeNode(self, exp_stack):
        next = "".join(self.type)
        if next == "R":
            return exp_stack.pop(0)
        elif next == "LR":
            next_exp = exp_stack.pop(0)
            exp = exp_stack.pop(0)
            return SequenceNode(exp, next_exp)
        elif next == "E;":
            semicolon = exp_stack.pop(0)
            child = EvaluateExpressionNode(exp_stack.pop(0))
            return ExpressionNode(child, semicolon)
        elif next == "A;" or next == "C;":
            semicolon = exp_stack.pop(0)
            child = exp_stack.pop(0)
            return ExpressionNode(child, semicolon)
        elif next == "(EBE)":
            right_bracket = exp_stack.pop(0)
            e2 = EvaluateExpressionNode(exp_stack.pop(0))
            op = OperationNode(exp_stack.pop(0))
            e1 = EvaluateExpressionNode(exp_stack.pop(0))
            left_bracket = exp_stack.pop(0)
            return BinaryExpressionNode(left_bracket, e1, op, e2, right_bracket)
        elif next == "V":
            child = exp_stack.pop(0)
            return VariableExpressionNode(child)
        elif next == "N":
            child = exp_stack.pop(0)
            return child
        elif next == "letV=E":
            e = EvaluateExpressionNode(exp_stack.pop(0))
            equal = exp_stack.pop(0)
            v = exp_stack.pop(0)
            let = exp_stack.pop(0)
            return AssignmentExpressionNode(let, v, equal, e)
        elif next == "whileEdoSH":
            h = exp_stack.pop(0)
            sequence = exp_stack.pop(0)
            do = exp_stack.pop(0)
            e = EvaluateExpressionNode(exp_stack.pop(0))
            w = exp_stack.pop(0)
            return LoopExpressionNode(w, e, do, sequence, h)
        elif next == "elseS":
            sequence = exp_stack.pop(0)
            e = exp_stack.pop(0)
            return ElseExpressionNode(e, sequence)
        elif next == "DM":
            number2 = exp_stack.pop(0)
            number1 = IntegerNode(exp_stack.pop(0))
            if number2:
                number2 = IntegerNode(number2)
            return IntegerExpressionNode(number1, number2)
        elif next == "0M":
            number2 = exp_stack.pop(0)
            number1 = IntegerNode(exp_stack.pop(0))
            if number2:
                number2 = IntegerNode(number2)
            return IntegerExpressionNode(number1, number2)
        elif next == "":
            return exp_stack.pop(0)
        else:
            return    

def parse(input_stack):
    parse_stack = ["S", "$"]
    while True:
        print("".join(input_stack) + "\t" + "".join(parse_stack))
        right = parse_stack[0]
        left = input_stack[0]
        if right == left and left == "$":
            print("ACCEPTED")
            return 
        elif right in terminals or right == "$":
            if right == left:
                parse_stack.pop(0)
                input_stack.pop(0)
            else:
                print("REJECTED")
                return
        elif left in terminals and parseTable.get(right)[index.get(left)]:
            parse_stack.pop(0)
            new_stack = parseTable.get(right)[index.get(left)]
            if new_stack[0] != "":
                parse_stack = new_stack + parse_stack
        else:
            print("REJECTED")
            return


def evaluate_exp(input_stack):
    parse_stack = ["S", "$"]
    exp_stack = []
    variables = {}
    while True:
        right = parse_stack[0]
        left = input_stack[0]
        if isinstance(right, ActionToken):
            token = parse_stack.pop(0)
            node = token.makeNode(exp_stack)
            if node:
                exp_stack.insert(0, node)
        elif right == left and left == "$":
            tree = exp_stack.pop(0)
            return tree.evaluate()
        elif right in terminals or right == "$":
            if right == left:
                terminal = parse_stack.pop(0)
                input_stack.pop(0)
                if (terminal == "x" or terminal == "y") or terminal == "z":
                    if terminal not in variables.keys():
                        node = VariableNode(TerminalNode(terminal))
                        variables[terminal] = node
                        terminal = node
                    else:
                        terminal = variables.get(terminal)
                else:
                    terminal = TerminalNode(terminal)
                exp_stack.insert(0, terminal)
            else:
                return "REJECTED"
        elif left in terminals and parseTable.get(right)[index.get(left)]:
            parse_stack.pop(0)
            new_stack = parseTable.get(right)[index.get(left)]
            if new_stack[0] != "":
                parse_stack.insert(0, ActionToken(new_stack))
                parse_stack = new_stack + parse_stack
            else:
                exp_stack.insert(0, None)
        else:
            return "REJECTED"



def clean(command):
    new_input = []
    i = 0
    while i < len(command):
        letter = command[i]
        if letter == "l":
            word = command[i] + command[i+1] + command[i+2]
            if word == "let":
                letter = word
                i+=2
            else:
                raise ValueError
        elif letter == "w":
            word = command[i] + command[i+1] + command[i+2] + command[i+3] + command[i+4]
            if word == "while":
                letter = word
                i+=4
            else:
                raise ValueError
        elif letter == "d":
            word = command[i] + command[i+1]
            if word == "do":
                letter = word
                i+=1
            else:
                raise ValueError
        elif letter == "e":
            word = command[i] + command[i+1] + command[i+2] + command[i+3]
            if word == "else":
                letter = word
                i+=3
            else:
                raise ValueError
        new_input.append(letter)
        i+=1
    new_input.append("$")
    return new_input


# start
evaluate = False
if len(sys.argv) < 2:
    sys.exit("No input file specified")

if len(sys.argv) == 3:
    if sys.argv[2] == "eval":
        evaluate = True
    else:
        sys.exit("Wrong command given")


file_name = sys.argv[1]
input = []

with open(file_name, "r") as f:
    for line in f:
        input.append(line.strip().replace(" ", ""))

input = list("".join(input))

try:
    input = clean(input)
except ValueError as e:
    sys.exit("String contains non terminals")

if evaluate:
    evaluate_exp(input)
else:
    parse(input)

