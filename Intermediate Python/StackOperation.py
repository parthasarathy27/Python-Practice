# stack - LIFO(Last In First Out)

stack = [2, 5, 6, 8, 1, 9]
print("Original stack is :", stack)
stack.append(7)
print("Stack after push operation is :", stack)
stack.pop()
print("stack after pop operation is :", stack)
last_element_index = len(stack) - 1
print("Value obtained after peep operation is :", stack[last_element_index])
