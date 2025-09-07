from stack_queue import Stack

# def remove_duplicates(stack):
#     dup = set()
#     temp = []
#     while not stack.is_empty():
#         temp.append(stack.pop())
#     new_stack = Stack()
#     for item in temp:
#         if item not in dup:
#             dup.add(item)
#             new_stack.push(item)
#     return new_stack
#
#
# s1 = Stack()
# for i in [1,2,2,3,4,5,6,7,8,8,9,10]:
#     s1.push(i)
#
# q1 = remove_duplicates(s1)
# while not q1.is_empty():
#     print(q1.pop())


def find_unmatch(string):
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return ')'
            stack.pop()
    if not stack.is_empty():
        return '('
    return None


print(find_unmatch('((())'))











