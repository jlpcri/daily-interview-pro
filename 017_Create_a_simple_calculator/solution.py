def precedence(op):
    value = 0
    if op == '+' or op == '-':
        value = 1
    elif op == '*' or op == '/':
        value = 2

    return value


def applyOp(a, b, op):
    result = 0
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a // b

    return result


def eval(expression):
    # value stack to store integer values
    values = []

    # operator stack to store operators
    ops = []

    i = 0
    while i < len(expression):
        if expression[i] == ' ':        # current token is white space
            i += 1
            continue
        elif expression[i] == '(':   # current token is opening brace, push it to op stack
            ops.append(expression[i])
        elif expression[i].isdigit():  # current token is a number, push it to value stack
            tmp = 0
            while i < len(expression) and expression[i].isdigit():  # current token is multiple digits number
                tmp = (tmp * 10) + int(expression[i])
                i += 1

            values.append(tmp)
        elif expression[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()     # pop second value first
                val1 = values.pop()
                op = ops.pop()
                tmp = applyOp(val1, val2, op)
                values.append(tmp)

            ops.pop()   # op stack pop opening brace
        else:    # current token is operator
            # if top of ops stack has same or greater precedence to current token, pop op from ops stack and calculate
            while len(ops) != 0 and precedence(ops[-1]) >= precedence(expression[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                tmp = applyOp(val1, val2, op)
                values.append(tmp)
            # else push current token to ops stack
            ops.append(expression[i])

        i += 1

    # entire expression has been parsed, final step is to
    # apply remaining ops to remaining values
    print('ops: ', ops)
    print('values: ', values)
    while len(ops) != 0 and len(values) > 1:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        tmp = applyOp(val1, val2, op)
        values.append(tmp)

    # now values stack only remain one value
    # we need check if first operator is '-'
    while len(ops) != 0:
        op = ops.pop()
        if op == '-':
            values[0] *= -1

    print('ops: ', ops)
    print('values: ', values)
    return values[-1]


ex = "- (3 + (2 - 1) )"
print(eval(ex))
