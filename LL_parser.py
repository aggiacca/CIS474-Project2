from copy import deepcopy

class State:
    def __init__(self, num, targetRs, stat = []):
        self.number = num

        # rules to check / interested in (underlined ones in example)
        # list of Rule
        self.targetRules = targetRs

        # compute closure of target and then add
        # list of Rule
        # self.closureExtras = dependency


        # add next character its checking for transition diagram later?
        # keep track of previous or next state?
        # list of State
        self.states = stat

class Rule:
    def __init__(self, num, nonterminal, dependency):
        self.order = num
        self.lhs = nonterminal
        self.rhs = dependency

    def print_rule(self):
        print("Order {0}, Left-hand side: {1}, Right-hand-side: {2}".format(self.order, self.lhs, self.rhs))


def addDotToStart(rule):
    rule.rhs = "." + rule.rhs
    return rule


# rules = original grammar and list of Rule
def closure(targetNT, rules, nonterminals):
    # first take any rules where targetChar is on the left hand side
    #   then add dot to beginning of rhs

    # to avoid modifying rules outside of scope
    tempRules = deepcopy(rules)
    finalClosure = [addDotToStart(i) for i in tempRules if i.lhs is targetNT]


    queue = []

    for rule in finalClosure:
        dotPos = rule.rhs.find(".")
        nextChar = rule.rhs[dotPos+1]
        if nextChar not in queue and nextChar in nonterminals and nextChar is not targetNT:
            queue.append(nextChar)

    # check sub rules
    while not len(queue) == 0:
        target = queue.pop()
        # consider removing rules already checked in case of possible edge cases
        subClosure = [addDotToStart(i) for i in tempRules if i.lhs is target]
        for rule in subClosure:
            dotPos = rule.rhs.find(".")
            nextChar = rule.rhs[dotPos + 1]
            finalClosure.append(rule)
            if nextChar not in queue and nextChar in nonterminals and nextChar is not target:
                queue.append(nextChar)

    return finalClosure

    # check subclosure
    # option 1 to recursivly take closure of chars to the right of dots
    # option 2 use stack to avoid duplicates


def checkItems(items, rhs):
    for state in items:
        for rule in state.targetRules:
            if rule.rhs == rhs:
                return True
    return False


# curState : State
# X : terminal or nonterminal char
def goto(curState, originalRules, X, nonterminals, terminals):
    J = []

    closuresAdded = []
    for rule in curState.targetRules:
        pos = rule.rhs.find("." + X)
        if pos != -1:
            # 1 for start a 0 and 1 for checking if X is last in list
            if pos+2 >= len(rule.rhs):
                # .X is last so just move over and add. no closure
                temp = rule.rhs[1:] + "."

                # can't just do rule.rhs = temp as it will update original since its just reference
                J.append(Rule(rule.order, rule.lhs, temp))
            else:
                # grab char in front of dot after wouldbe move
                nextChar = rule.rhs[pos+2:pos+3]

                # move dot over
                temp = rule.rhs[:pos] + rule.rhs[pos+1:pos+2] + "." + rule.rhs[pos+2:]
                # can't just do rule.rhs = temp as it will update original since its just reference
                J.append(Rule(rule.order, rule.lhs, temp))
                if nextChar in nonterminals and nextChar not in closuresAdded:
                    # copy of orginal rules since closure modifies original rules
                    tempList = deepcopy(closure(nextChar, originalRules, nonterminals))
                    J.extend(tempList)
                    closuresAdded.append(nextChar)
    # TODO: consider returning a object that seprates the closure rules and rules that had the dot moved over
    return J


def compareStateRules(state1, state2):
    if len(state1.targetRules) != len(state2.targetRules):
        return False

    isEqual = True
    # TODO: fix this to continue. It wasn't actually checking the rhs of each so it always passed and caused infinite loop above
    for rule1 in state1.targetRules:
        for rule2 in state2.targetRules:
            if rule1.rhs == rule2.rhs
        if rule not in state2.targetRules:
            return False

    return True

# goes through states and checks if state already exists
def checkIfStateExists(states, targetState):
    for state in states:
        if compareStateRules(state, targetState):
            return True
    return False


def generate_items(rules, nonterminals, terminals):
    augmentedRule = rules[0]

    allSymbols = nonterminals + terminals

    items = []

    queue = []

    # double check augmented rule
    stateCounter = 0
    if augmentedRule.lhs.find("'") != -1:
        # TODO: first augmented rule is not being added into first state
        initialState = State(stateCounter, closure(augmentedRule.rhs, rules, nonterminals))
        items.append(initialState)
        queue.append(initialState)
        stateCounter += 1

        # TODO: infinite loop currently
        while not len(queue) == 0:
            # remove first
            curState = queue.pop(0)

            for symbol in allSymbols:
                newState = State(stateCounter, goto(curState, rules, symbol, nonterminals, terminals))
                if newState is not None and len(newState.targetRules) != 0 and not checkIfStateExists(items, newState):
                    items.append(newState)
                    queue.append(newState)
                    stateCounter += 1
    else:
        print("augmented grammar start issue")

    return items

    # goto for each unique char both terminals and nonterminals