
def printList(list):
    for item in list:
        print(item)


if __name__ == "__main__":

    file = open("example-input", "r")
    terminals = file.readline().split(",")
    nonterminals = file.readline().split(",")

    printList(terminals)
    printList(nonterminals)