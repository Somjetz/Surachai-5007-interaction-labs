def calculator():
    while True:
        op1 = ("Enter the first operand ('q' to quit):")
        op2 = ("Enter the second operand ('q' to quit):")
        operator = get_operator()
        if operator is None:
            continue
        requested_format = get_format()
        output = robust_calculator(op1, op2, operator, requested_format)
        if output is not None:
            if operator == "":
                operator = ADD
            print("{} {} {} = {}".format(op1, operator, op2, output))
        else:
            print("We cannot perform your requested calculation")

if __name__ == "__main__":
    calculator()