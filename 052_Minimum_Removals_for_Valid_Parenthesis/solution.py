def count_invalid_parenthesis(string):
    result = list(string)
    count = 0

    for i in invalid_indexes(string):
        count += 1
        result[i] = None

    result = filter(lambda el: el is not None, result)
    print(''.join(result))

    return count


def invalid_indexes(string):
    '''
    Zero balance: equal number '(' and ')'
    Negative balance: more ')' than '('
    Positive balance: more '(' than ')'
    If at any point of processing we got negative balance,
    we mark current ')' as invalid
    :param string:
    :return:
    '''
    balance = 0
    for i, c in enumerate(string):
        if c == '(':
            # increase balance
            balance += 1
        elif c == ')':
            # found ')'
            if balance == 0:
                # if balanced so far, thus ')' is not allowed
                # yield an index of the invalid parenthesis
                yield i
            else:
                # decrease balance on ')'
                balance -= 1

    if balance > 0:
        # positive balance means we've extra '('
        # rightmost '(' are those extra '('
        for i in range(len(string) - 1, -1, -1):
            c = string[i]
            if c == '(':
                # find extra '(', yield it and decrease balance
                yield i
                balance -= 1

                # until balance is 0
                if balance == 0:
                    return


s = '()())()'
print(count_invalid_parenthesis(s))
# (())()

s = 'lee(t(c)o)de)'
print(count_invalid_parenthesis(s))
# lee(t(c)o)de

s = 'a)b(c)d'
print(count_invalid_parenthesis(s))
# ab(c)d

s = '))(('
print(count_invalid_parenthesis(s))
# ""

s = '(a(b(c)d)'
print(count_invalid_parenthesis(s))
# a(b(c)d)
