from LL_parser import Rule, generate_items

def print_list(list):
    for item in list:
        print(item)


def fileInputFiltering(str):
    return str.strip().replace(" ", "").replace("\n", "")


if __name__ == "__main__":
    file = open("example-input", "r")
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

    for rule in rules:
        rule.print_rule()

    print_list(nonterminals)
    print_list(terminals)

    items = generate_items(rules, nonterminals, terminals)



