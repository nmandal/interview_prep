# O(n) time | O(1) space
def evaluate(RPN_expression):
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
        "+": lambda y, x: x + y,
        "-": lambda y, x: x - y,
        "*": lambda y, x: x * y,
        "/": lambda y, x: int(x / y)
    }
    
    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))
    return intermediate_results[-1]
