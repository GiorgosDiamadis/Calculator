from stack import Stack

in_pre = {
    '+': 2,
    '-': 2,
    '*': 4,
    '/': 4,
    '^': 5,
    '(': 0,
    ')': 0
}

out_pre = {
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
    '/': lambda a, b: a/b,
    '^': lambda a, b: a**b
}


def infix_to_posfix(expression):

    stack = Stack()
    postfix = ""
    i = 0

    while i < len(expression):
        if not in_pre.__contains__(expression[i]):
            postfix += expression[i]
            i += 1
        else:
            if stack.is_empty():
                stack.push(expression[i])
                i += 1
            else:
                if out_pre[expression[i]] > in_pre[stack.peek()]:
                    stack.push(expression[i])
                    i += 1
                elif out_pre[expression[i]] == in_pre[stack.peek()]:
                    stack.pop()
                else:
                    postfix += stack.pop()

    while not stack.is_empty() and stack.peek() != ')':
        postfix += stack.pop()

    return postfix


def find_numbers(expression):
    numbers = []
    st = ""
    for char in expression:
        if char.isdigit():
            st += char
        else:
            if len(st) > 0:
                numbers.append(st)
                st = ""

    if len(st) > 0:
        numbers.append(st)

    return numbers


def main():
    while 1:
        expression = input("Enter expression\n")
        posfix = infix_to_posfix(expression)
        numbers = find_numbers(expression)
        print(numbers)
        print(posfix)


if __name__ == "__main__":
    main()
