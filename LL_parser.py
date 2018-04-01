class State:
    def __init__(self, targetRs, dependency):

        # rules to check / interested in (underlined ones in example)
        self.targetRules = targetRs

        # compute closure of target and then add
        self.closureExtras = dependency
        # add next character its checking for transition diagram later?
        # keep track of previous or next state?


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



def generate_items(rules, nonterminals, terminals):
    augmentedRule = rules[0]

    if augmentedRule[0] in nonterminals:
        closure(augmentedRule[0], rules, nonterminals)