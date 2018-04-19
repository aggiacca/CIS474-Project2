class stack_item:
    def __init__(self, num, let):
        self.stateNumber = num

        self.letter = let


def parse_expression(expression, original_rules, action_table, goto_table):
    stack = []

    expression_list = expression.split(" ")

    
