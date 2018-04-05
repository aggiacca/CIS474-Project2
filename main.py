from LL_parser import Rule, generate_items, generate_transition_diagram, generate_parsing_table
from FF import FIRST, generate_follow_table
from copy import deepcopy

def print_list(list):
    for item in list:
        print(item)


def fileInputFiltering(str):
    return str.strip().replace(" ", "").replace("\n", "")


if __name__ == "__main__":
    file = open("example-input", "r")

    # first nonterminal should be part of augmented so E and E' -> E
    # option: remove from input and create augmented grammar
    nonterminals = fileInputFiltering(file.readline()).split(",")
    terminals = fileInputFiltering(file.readline()).split(",")

    rules = []

    ruleCount = 0
    inputRule = file.readline()
    while inputRule is not '':
        splitList = inputRule.split("->")

        rules.append(Rule(ruleCount, fileInputFiltering(splitList[0]), fileInputFiltering(splitList[1])))

        inputRule = file.readline()
        ruleCount += 1

    # need deepcopy as individual rules keep their original references even if new list
    nonaugRules = deepcopy(rules)
    nonaugRules.pop(0)



    # pass in shallow copy of rules
    items = generate_items(rules, nonterminals, terminals)
    print("Set of Items: ")
    for item in items:
        print("Set #: {0}".format(item.number))
        for rule in item.targetRules:
            rule.print_rule()

    print("Follow Table:")
    follow_table = generate_follow_table(rules, nonterminals, terminals)

    print("Transition Diagram:")
    generate_transition_diagram(items, follow_table, rules, nonterminals, terminals)

    print(" ")

    generate_parsing_table(items, follow_table, rules, nonterminals, terminals)








