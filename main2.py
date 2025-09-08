class Stack:
    def __init__(self):
        self.items = []

    def push(self, obj):
        self.items.append(obj)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)



def remove_duplicates(stack):
    dup = set()
    temp = []
    while not stack.is_empty():
        temp.append(stack.pop())
    new_stack = Stack()
    for item in temp:
        if item not in dup:
            dup.add(item)
            new_stack.push(item)
    return new_stack


s1 = Stack()
for i in [1,2,2,3,4,5,6,7,8,8,9,10]:
    s1.push(i)

q1 = remove_duplicates(s1)
while not q1.is_empty():
    print(q1.pop())


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


def equal_stacks(s1, s2):
    if s1.size() != s2.size():
        return False
    s1_lst = []
    s2_lst = []
    while not s1.is_empty():
        s1_lst.append(s1.pop())
    while not s2.is_empty():
        s2_lst.append(s2.pop())
    return sorted(s1_lst) == sorted(s2_lst)

stack1 = Stack()
for i in [1,3,5,7,9]:
    stack1.push(i)

stack2 = Stack()
for j in [9,7,5,1,3]:
    stack2.push(j)

print(equal_stacks(stack1, stack2))


def compress_str(string):
    if not string:
        return ''
    input_stack = Stack()
    for char in string:
        input_stack.push(char)
    result_stack = Stack()
    prev_char = None
    count = 0
    while not input_stack.is_empty():
        char = input_stack.pop()
        if char == prev_char:
            count += 1
        else:
            if prev_char is not None:
                if count == 1:
                    count = ''
                result_stack.push(f"{prev_char}{count}")
            prev_char = char
            count = 1
    if count == 1:
        count = ''
    result_stack.push(f"{prev_char}{count}")
    res = ''
    while not result_stack.is_empty():
        res = res + result_stack.pop()
    return res


print(compress_str('aabbbcc'))


def reverse_sentence(string):
    if not string:
        return ''
    stack = Stack()
    lst = string.split()
    res = []
    for word in lst:
        for char in word:
            stack.push(char)
        rev_word = ''
        while not stack.is_empty():
            rev_word += stack.pop()
        res.append(rev_word)
    return ' '.join(res)

print(reverse_sentence('hello world!'))




