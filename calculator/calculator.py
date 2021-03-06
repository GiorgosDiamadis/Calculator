from stack import Stack
import math

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

    stack_num = Stack()
    postfix = ""
    i = 0

    while i < len(expression):
        if not in_pre.__contains__(expression[i]):
            postfix += expression[i]
            i += 1
        else:
            if stack_num.is_empty():
                stack_num.push(expression[i])
                i += 1
            else:
                if out_pre[expression[i]] > in_pre[stack_num.peek()]:
                    stack_num.push(expression[i])
                    i += 1
                elif out_pre[expression[i]] == in_pre[stack_num.peek()]:
                    stack_num.pop()
                else:
                    postfix += stack_num.pop()

    while not stack_num.is_empty() and stack_num.peek() != ')':
        postfix += stack_num.pop()

    return postfix


def find_numbers(expression):
    numbers = []
    i = 0
    for char in expression:
        if not in_pre.__contains__(char):
            i += 1
        else:
            if i > 0:
                numbers.append(i)
                i = 0

    if i > 0:
        numbers.append(i)

    return numbers


def evaluate(posfix, numbers):
    stack_num = Stack()

    k = 0
    i = 0

    num = ""
    result = 0

    while i < len(posfix):
        if not in_pre.__contains__(posfix[i]):

            if k == 0:
                for j in range(numbers[k]):
                    num += posfix[j]
            else:
                for j in range(i, i + numbers[k]):
                    num += posfix[j]

            stack_num.push(float(num))

            i += numbers[k]
            k += 1
            num = ""
        else:
            x2 = stack_num.pop()
            x1 = stack_num.pop()

            result = operation[posfix[i]](x1, x2)

            stack_num.push(result)
            i += 1
    return result


def calc(expression, func):
    x = ""
    i = expression.index(func.__name__)
    i += len(func.__name__) + 1
    while expression[i] != ")":
        x += expression[i]
        i += 1
    expression = expression.replace(
        func.__name__ + "("+x+")", str(func(math.radians(float(x)))))

    return expression


def calc_math_functions(expression):
    if "sinh" in expression:
        expression = calc(expression, math.sinh)
    if "cosh" in expression:
        expression = calc(expression, math.cosh)
    if "tanh" in expression:
        expression = calc(expression, math.tanh)
    if "sin" in expression:
        expression = calc(expression, math.sin)
    if "cos" in expression:
        expression = calc(expression, math.cos)
    if "tan" in expression:
        expression = calc(expression, math.tan)

    return expression


def main():
    while 1:
        expression = input("Enter expression\n")
        expression = calc_math_functions(expression)
        posfix = infix_to_posfix(expression)
        numbers = find_numbers(expression)
        res = evaluate(posfix, numbers)
        print(res)


if __name__ == "__main__":
    main()
