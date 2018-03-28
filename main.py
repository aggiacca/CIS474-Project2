
def printList(list):
    for item in list:
        print(item)


class Rule:
    def __init__(self, nonterminal, dependency):
        self.lhs = nonterminal
        self.rhs = dependency


def closure(targetNT, rules):
    # first take any rules where targetChar is on the left hand side
    #   then add dot to beginning of rhs


    # check subclosure
    # option 1 to recursivly take closure of chars to the right of dots
    # option 2 use stack to avoid duplicates

    # create stack with nonterminals to check



if __name__ == "__main__":

    file = open("example-input", "r")
    terminals = file.readline().split(",")
    nonterminals = file.readline().split(",")

    printList(terminals)
    printList(nonterminals)

