from copy import deepcopy


# Preconditions
# rules = initial nonaugmented grammar and type: list of Rule
# each rule only contains one option ( no | ) and no Epsilon
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

# Preconditions
# rules = initial nonaugmented grammar and type: list of Rule
# each rule only contains one option ( no | ) and no Epsilon
def FOLLOW(rules, target, nonterminals, terminals, start):
    followChars = []

    for rule in rules:
        pos = rule.rhs.find(target)
        if pos != -1:
            if rule.rhs.endswith(rule.rhs[pos]):
                # last charater so follow of lhs
                followChars = deepcopy(FOLLOW(rules, rule.lhs, nonterminals, terminals, start))
            elif rule.rhs[pos+1] in nonterminals:
                # nonterminal in front so take first of that
                followChars = deepcopy(FIRST(rules, rule.rhs[pos+1], nonterminals, terminals))
            elif rule.rhs[pos+1] in terminals:
                # terminal so add to follow
                followChars.append(rule.rhs[pos+1])
            else:
                print("error in follow")

    if target is start:
        followChars.append('$')

    return followChars


def generate_follow_table(rules, nonterminals, terminals):
    # plus one for $ symbol
    startTerminals = deepcopy(terminals)
    startTerminals.append('$')
    follow_table = [['- ' for x in range(len(startTerminals))] for y in range(len(nonterminals))]

    follow = []
    for nt in nonterminals:
        follow.append(FOLLOW(rules, nt, nonterminals, terminals, nonterminals[0]))


    print(' ', end='')
    for term in startTerminals:
        print("{0} ".format(term), end='')

    print("\n")

    for y_index, y in enumerate(follow_table):
        print("{0} ".format(nonterminals[y_index]), end='')
        for x_index, x in enumerate(y):
            if startTerminals[x_index] in follow[y_index]:
                x = 'X '
            print(x, end='')
        print("\n")

    return follow
