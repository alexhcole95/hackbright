def reverse_in_place(a_list):
    list_copy = list(a_list)
    while a_list:
        a_list.pop()

    for item in list_copy:
        a_list[0:0] = [item]


def has_balanced_parens(phrase):
    """ Does a string have balances parentheses? """

    stack = []

    closers_to_openers = {
        ')': '(',
        '}': '{',
        ']': '[',
        '>': '<'
    }

    for char in phrase:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        elif char in closers_to_openers:
            if stack == [] or stack.pop() != closers_to_openers[char]:
                return False
        # elif char == ')':
        #     if stack == [] or stack.pop() != '(':
        #         return False
        # elif char == ']':
        #     if stack == [] or stack.pop() != '[':
        #         return False
        # elif char == '}':
        #     if stack == [] or stack.pop() != '{':
        #         return False
        # elif char == '>':
        #     if stack == [] or stack.pop() != '<':
        #         return False
    return stack == []


print(has_balanced_parens("()"))
print(has_balanced_parens("(Oh Noes!)("))
print(has_balanced_parens("((There's a bonus open paren here.)"))
print(has_balanced_parens(")"))
print(has_balanced_parens("("))
print(has_balanced_parens("(This has (too many closes.) ) )"))

# l1 = ['a', 'b', 'c', 'd']
# l2 = l1
# reverse_in_place(l1)
# print(l2)
