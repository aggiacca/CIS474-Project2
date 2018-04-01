# Preconditions
# rules = initial nonaugmented grammar and list of Rule
# each rule only contains one option and no Epsilon
def FIRST(rules, target, nonterminals, terminals):
    initialRules = [i for i in rules if i.lhs is target]

    firstChars = []

    queue = []

    for rule in initialRules:
        nextChar = rule.rhs[0]
        if nextChar in terminals:
            firstChars.append(nextChar)
        if nextChar not in queue and nextChar in nonterminals and nextChar is not target:
            queue.append(nextChar)

    while not len(queue) == 0:
        target = queue.pop()
        # consider removing rules already checked in case of possible edge cases
        subRules = [i for i in rules if i.lhs is target]
        for rule in subRules:
            nextChar = rule.rhs[0]
            if nextChar in terminals:
                firstChars.append(nextChar)
            if nextChar not in queue and nextChar in nonterminals and nextChar is not target:
                queue.append(nextChar)

    return firstChars


def FOLLOW(rules, target):
    followChars = []

    for rule in rules:
        pos = rule.rhs.find(target)
        if pos != -1:
            if rule.rhs.endswith(rule.rhs[pos]):
                # last charater
            else:
                # not last so grab next character



    print("hello")


def generate_follow_table():
    print("hello")