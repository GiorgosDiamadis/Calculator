from stack import Stack

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

operation = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b
}


def infix_to_posfix(expression):

    stack = Stack()
    postfix = ""
    i = 0

    while i < len(expression):
        if not precedence.__contains__(expression[i]):
            postfix += expression[i]
            i += 1
        else:
            if stack.is_empty():
                stack.push(expression[i])
                i += 1
            else:
                if precedence[expression[i]] > precedence[stack.peek()]:
                    stack.push(expression[i])
                    i += 1
                else:
                    postfix += stack.pop()

    while not stack.is_empty():
        postfix += stack.pop()
    return postfix


def main():
    while 1:
        expression = input("Enter expression\n")
        expression = infix_to_posfix(expression)
        print(expression)


if __name__ == "__main__":
    main()
