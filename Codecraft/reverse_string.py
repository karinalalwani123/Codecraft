def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(temp)

def reverse_stack(stack):
    if len(stack) > 0:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)