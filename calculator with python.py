def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2

dic = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
4

def calculator():
    print("""
     _____________________
    |  Pythonista   0.   |
    | ------------------ |
    | [7] [8] [9] [/]   |
    | [4] [5] [6] [*]   |
    | [1] [2] [3] [-]   |
    | [0] [.] [=] [+]   |
     --------------------
    """)
    num1 = int(input("What is your first number ?: "))
    should_continue = True
    while should_continue:

        for i in dic:
            print(i)

        operator_chosen = input("Pick an operation: ")
        num2 = int(input("What is your next number ?: "))
        answer = dic[operator_chosen](num1, num2)
        print(f"{num1} {operator_chosen} {num2} = {answer}")
        choice = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ")

        # should_continue = True
        # while should_continue:
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
