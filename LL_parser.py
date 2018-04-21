class Stack_item:
    def __init__(self, let, num):
        self.letter = let
        self.stateNumber = num


class Stacktop:
    def __init__(self, stck, inp, act):
        self.stack = stck
        self.expressionInput = inp
        self.action = act


def stack_items_to_string(items):
    finalStr = ''
    for stack_item in items:
        finalStr += "{0} {1} ".format(stack_item.letter, stack_item.stateNumber)
    return finalStr

def print_stack_top(items):
    count = 1
    for stacktop in items:
        print("({0})  {1}    | {2}      |{3}".format(count, stacktop.stack, stacktop.expressionInput, stacktop.action))
        count += 1


def parse_expression(expression, original_rules, action_table, goto_table, terminals, nonterminals):
    stack = []
    outputStack = []

    # start
    stack.append(Stack_item("0", 0))

    expression_list = expression.split(" ")

    count = 0
    # left to right get next symbol
    currSymbol = expression_list.pop(0)

    acceptStateNotFound = True

    while acceptStateNotFound:
        # get current state
        currState = stack[-1]
        # check if symbol in state either in

        nextRule = '- '

        # check action table
        if currSymbol in terminals:
            nextRule = action_table[currState.stateNumber+1][action_table[0].index(currSymbol)+1]

        # check goto table
        if currSymbol in nonterminals:
            nextRule = goto_table[currState.stateNumber+1][goto_table[0].index(currSymbol)+1]

        if nextRule is '- ':
            print("Error parsing")

        # accept state
        if nextRule[0] is 'A':
            acceptStateNotFound = False
            outputStack.append(Stacktop(stack_items_to_string(stack), ''.join(expression_list),
                                        "Accept"))

        # s so shift
        elif nextRule[0] is 's' or nextRule[0] is '0':
            stack.append(Stack_item(currSymbol, int(nextRule[1:])))
            # shift so done with expression item. update expression item
            currSymbol = expression_list.pop(0)

            outputStack.append(Stacktop(stack_items_to_string(stack), currSymbol + ''.join(expression_list), "shift"))


        # s so reduce
        elif nextRule[0] is 'r':
            # remove current unreduced stack item
            currentRule = original_rules[int(nextRule[1])]
            charsToPop = list(currentRule.rhs)

            # multiple states to pop off
            if len(charsToPop) > 1:
                # pop off everything. can't just use original if entire thing is replaced
                while len(charsToPop) != 0:
                    charsToPop.pop()
                    stack.pop()

            # only one character to reduce so just pop it off and replace
            else:
                stack.pop()

            # find reduced nonterminal
            reducedNT = original_rules[int(nextRule[1])].lhs

            # previous state number for goto check
            previousState = stack[-1]

            # put reduced stack item
            stack.append(Stack_item(reducedNT, int(goto_table[previousState.stateNumber+1][goto_table[0].index(reducedNT)])))

            outputStack.append(Stacktop(stack_items_to_string(stack), ''.join(expression_list),
                                        "reduce by {0} -> {1}".format(original_rules[int(nextRule[1])].lhs, original_rules[int(nextRule[1])].rhs)))

            # if reduce don't update currSymbol

    return outputStack