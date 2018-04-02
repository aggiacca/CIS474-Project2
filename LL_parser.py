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
    finalClosure = [addDotToStart(i) for i in rules if i.lhs is targetNT]

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
        subClosure = [addDotToStart(i) for i in rules if i.lhs is target]
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
            if pos+2 == len(rule.rhs):
                # .X is last so just move over and add. no closure
                temp = rule.rhs.remove(".")
                temp.append(".")
                rule.rhs = temp
                J.append(rule)
            else:
                # grab char in front of dot after wouldbe move
                nextChar = rule.rhs[pos+2:pos+3]

                # move dot over
                temp = rule.rhs[:pos] + rule.rhs[pos+1:pos+2] + "." + rule.rhs[pos+2:]
                rule.rhs = temp
                J.append(rule)
                if nextChar in nonterminals and nextChar not in closuresAdded:
                    tempList = deepcopy(closure(nextChar, originalRules, nonterminals))
                    J.append(tempList)
                    closuresAdded.append(nextChar)
    # TODO: consider returning a object that seprates the closure rules and rules that had the dot moved over
    return J




def generate_items(rules, nonterminals, terminals):
    augmentedRule = rules[0]

    items = []
    # double check augmented rule
    stateCounter = 0
    if augmentedRule.lhs.find("'") != -1:
        items.append(State(stateCounter, closure(augmentedRule.rhs, rules, nonterminals)))
        stateCounter += 1
        

        print("hello world")

    else:
        print("augmented grammar start issue")

    return items

    # goto for each unique char both terminals and nonterminals