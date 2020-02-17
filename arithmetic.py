"""The evaluate method will return a representation of evaluating the subtree
rooted at this tree node. Subtrees that are arithmetic expressions will
return a number, but note that some of the subtrees aren't arithmetic
expressions (e.g. a subtree might just be a "(" or an operator like "+")

note: currently this code is incomplete, it will not execute successfully.
You will need to implement the sections marked TODO"""



class TerminalNode():
    """This is a terminal symbol"""
    def __init__(self, element):
        self.element = element
    def evaluate(self):
        """This simply evaluates as the contained string (i.e. the terminal)"""
        return self.element
    def __str__(self):
        return self.element
    def __repr__(self):
        return "TM[{}]".format(self.element)

class IntegerNode():
    """This corresponds to the rules D -> an integer"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        #IntegerNodes link to TerminalNodes, so they simply evaluate as the string
        #contained in that TerminalNode (i.e. the terminal)
        return int(self.child.evaluate())
    def __str__(self):
        return str(self.child)
    def __repr__(self):
        return "IN[{}]".format(self.child)

class VariableNode():
    """This corresponds to the rules V -> x | y | z"""
    def __init__(self, name):
        self.name = name
        self.value = None
    def updateValue(self, value):
        self.value = value
    def evaluate(self):
        if self.value:
            return int(self.value)
        else:
            return self.name
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return "VN[{}]".format(self.name)

class OperationNode():
    """This corresponds to the rules B -> + | - | * | >"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        #TODO: Operation nodes have a Terminal as a child, so what should it evaluate as?
        return str(self.child.evaluate())
    def __str__(self):
        return str(self.child)
    def __repr__(self):
        return "ON[{}]".format(self.child)

class BinaryExpressionNode():
    """This corresponds to the rule E -> (EBE)"""
    def __init__(self, left_bracket, e1, operation, e2, right_bracket):
        self.left_bracket = left_bracket
        self.e1 = e1
        self.operation = operation
        self.e2 = e2
        self.right_bracket = right_bracket
    def evaluate(self):
        #apply the appropriate operation to the two evaluated expressions
        operation = self.operation.evaluate()
        lhs = self.e1.evaluate()
        rhs = self.e2.evaluate()
        if operation == "+":
            return lhs + rhs
        elif operation == "-":
            return lhs - rhs
        elif operation == "*":
            return lhs * rhs 
        elif operation == ">":
            if lhs > rhs:
                return 1
            else:
                return 0
        else:
            return None #it would be better to raise an exception
    def __str__(self):
        return "{}{}{}{}{}".format(str(self.left_bracket), str(self.e1), str(self.operation), str(self.e2), str(self.right_bracket))
    def __repr__(self):
        return "BEN[{}{}{}{}{}]".format(self.left_bracket, self.e1, self.operation, self.e2, self.right_bracket)

class IntegerExpressionNode():
    """This corresponds to the rule N -> DM"""
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def evaluate(self):
        if self.number2:
            return self.number1.evaluate() * 10 + self.number2.evaluate()
        else:
            return self.number1.evaluate()
    def __str__(self):
        if self.number2:
            return str(self.number1) + str(self.number2)
        else:
            return str(self.number1)
    def __repr__(self):
        if self.number2:
            return "IEN[{}{}]".format(self.number1, self.number2)
        else:
            return "IEN[{}]".format(self.number1)

class IntegerContinueExpressionNode():
    """This corresponds to the rule M -> DM | 0M"""
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def evaluate(self):
        if self.number2:
            return self.number1.evaluate * 10 + self.number2.evaluate
        else:
            return self.number1.evaluate()
    def __str__(self):
        if self.number2:
            return str(self.number1) + str(self.number2)
        else:
            return str(self.number1)
    def __repr__(self):
        if self.number2:
            return "ICEN[{}{}]".format(self.number1, self.number2)
        else:
            return "ICEN[{}]".format(self.number1)
        

class VariableExpressionNode():
    """This corresponds to the rule E -> V"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        return self.child.evaluate()
    def __str__(self):
        return str(self.child)
    def __repr__(self):
        return "VEN[{}]".format(self.child)

class EvaluateExpressionNode():
    """This corresponds to the rule E -> (EBE) | V | N"""
    def __init__(self, child):
        self.child = child
    def evaluate(self):
        return self.child.evaluate()
    def __str__(self):
        return str(self.child)
    def __repr__(self):
        return "EEN[{}]".format(self.child)

class AssignmentExpressionNode():
    """This corresponds to the rule A -> letV=E"""
    def __init__(self, let, variable, equal_sign, operation):
        self.let = let
        self.variable = variable
        self.equal_sign = equal_sign
        self.operation = operation
    def evaluate(self):
        value = self.operation.evaluate()
        self.variable.updateValue(value)
        return self.variable.evaluate()
    def __str__(self):
        return "{}{}{}{}".format(str(self.let), str(self.variable), str(self.equal_sign), str(self.operation))
    def __repr__(self):
        return "AEN[{}{}{}{}]".format(str(self.let), str(self.variable), str(self.equal_sign), str(self.operation))

class LoopExpressionNode():
    """This corresponds to the rule C -> whileEdoSH"""
    def __init__(self, w, expression, do, sequence, e):
        self.w = w
        self.expression = expression
        self.do = do
        self.sequence = sequence
        self.e = e
    def evaluate(self):
        while self.expression.evaluate():
            self.sequence.evaluate()
        if self.e:
            self.e.evaluate()
        return
    def __str__(self):
        return "{}{}{}{}{}".format(str(self.w), str(self.expression), str(self.do), str(self.sequence), str(self.e))
    def __repr__(self):
        if self.e:
            return "LEN[{}{}{}{}{}]".format(str(self.w), str(self.expression), str(self.do), str(self.sequence), str(self.e))
        else:
            return "LEN[{}{}{}{}]".format(str(self.w), str(self.expression), str(self.do), str(self.sequence))


class ElseExpressionNode():
    """This corresponds to the rule H -> elseS"""
    def __init__(self, e, else_sequence):
        self.e = e
        self.else_sequence = else_sequence
    def evaluate(self):
        self.else_sequence.evaluate()
        return 
    def __str__(self):
        return "{}{}".format(str(self.e), str(self.else_sequence))
    def __repr__(self):
        return "ElseEN[{}{}]".format(self.e, self.else_sequence)

class SequenceNode():
    """This corresponds to the rule S -> LS"""
    def __init__(self, expression, next_expression):
        self.expression = expression
        self.next_expression = next_expression
    def evaluate(self):
        self.expression.evaluate()
        if self.next_expression:
            self.next_expression.evaluate()
        return
    def __str__(self):
        if self.next_expression:
            return "{}{}".format(str(self.expression), str(self.next_expression))
        else:
            return str(self.expression)
    def __repr__(self):
        if self.next_expression:
            return "S[{}{}]".format(self.expression, self.next_expression)
        else:
            return "S[{}]".format(self.expression)

class ExpressionNode():
    """This corresponds to the rule L -> A; | E; | C;"""
    def __init__(self, expression, semicolon):
        self.expression = expression
        self.semicolon = semicolon
    def evaluate(self):
        if isinstance(self.expression, EvaluateExpressionNode):
            print(self.expression.evaluate())
        return self.expression.evaluate()
    def __str__(self):
        return "{}{}".format(str(self.expression), str(self.semicolon))
    def __repr__(self):
        return "EN[{}{}]".format(self.expression, self.semicolon)
        


if __name__ == '__main__':

    """Example (1+(3-2))

         E
    / / |  \    \
  /  /  |    \    \
 (  E   B     E    )
    |   |     |
    Z   +     E
    |     / / | \ \
    1     ( E B E )
            | | |
            Z - Z
            |   |
            3   2
"""
    """
    tree = BinaryExpressionNode(
        TerminalNode("("),
        IntegerExpressionNode(IntegerNode(TerminalNode("1"))),
        OperationNode(TerminalNode("+")),
        BinaryExpressionNode(
            TerminalNode("("),
            IntegerExpressionNode(IntegerNode(TerminalNode("3"))),
            OperationNode(TerminalNode("-")),
            IntegerExpressionNode(IntegerNode(TerminalNode("2"))),
            TerminalNode(")")
        ),
        TerminalNode(")")
    )

    print(str(tree)) #this should output "(1+(3-2))"
    print(tree.evaluate()) #this should output "2"
    """





