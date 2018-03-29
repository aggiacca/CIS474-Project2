class State:
    def __init__(self, targetRs, dependency):

        # rules to check / interested in (underlined ones in example)
        self.targetRules = targetRs
        self.closureExtras = dependency
        # add next character its checking for transition diagram later?
        # keep track of previous or next state?


class Rule:
    def __init__(self, num, nonterminal, dependency):
        self.order = num
        self.lhs = nonterminal
        self.rhs = dependency

    def printRule(self):
        print("Order {0}, Left-hand side: {1}, Right-hand-side: {2}".format(self.order, self.lhs, self.rhs))

def addDotToStart(rule):
    rule.rhs = "." + rule.rhs

def closure(targetNT, rules):
    print("hello")
    # first take any rules where targetChar is on the left hand side
    #   then add dot to beginning of rhs
    startList = [addDotToStart(i) for i in rules if i.lhs is targetNT]

    queue = []

    for rule in startList:
        dotPos = rule.rhs.find(".")
        nextChar = rule.rhs[dotPos+1]
        if nextChar not in queue:
            queue.append(nextChar)

    while not queue:
        


    # check subclosure
    # option 1 to recursivly take closure of chars to the right of dots
    # option 2 use stack to avoid duplicates

    # create stack with nonterminals to check


def generateItems(rules, nonterminals):
    augmentedRule = rules[0]

    if augmentedRule[0] in nonterminals:
        closure(augmentedRule[0], rules)

def printList(list):
    for item in list:
        print(item)



if __name__ == "__main__":

    file = open("example-input", "r")
    terminals = file.readline().split(",")
    nonterminals = file.readline().split(",")

    rules = []

    ruleCount = 0
    inputRule = file.readline()
    while inputRule is not '':
        splitList = inputRule.split("->")

        rules.append(Rule(ruleCount, splitList[0].strip(), splitList[1].strip()))

        inputRule = file.readline()
        ruleCount += 1

    for rule in rules:
        rule.printRule()

    printList(terminals)
    printList(nonterminals)

