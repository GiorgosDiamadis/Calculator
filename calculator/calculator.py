from stack import Stack

precedence_in = {
    '+': 2,
    '-': 2,
    '*': 4,
    '/': 4,
    '^': 5,
    '(': 0,
    ')': 0
}

precedence_out = {
    '+': 1,
    '-': 1,
    '*': 3,
    '/': 3,
    '^': 6,
    '(': 7,
    ')': 0
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
        if not precedence_in.__contains__(expression[i]):
            postfix += expression[i]
            i += 1
        else:
            if stack.is_empty():
                stack.push(expression[i])
                i += 1
            else:
                if precedence_out[expression[i]] > precedence_in[stack.peek()]:
                    stack.push(expression[i])
                    i += 1
                elif precedence_out[expression[i]] == precedence_in[stack.peek()]:
                    stack.pop()
                else:
                    postfix += stack.pop()

    while not stack.is_empty() and stack.peek() != ')':
        postfix += stack.pop()
    return postfix


def main():
    while 1:
        expression = input("Enter expression\n")
        expression = infix_to_posfix(expression)
        print(expression)


if __name__ == "__main__":
    main()
