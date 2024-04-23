def create_stack():
    return []

def is_empty(stack):
    return len(stack) == 0

def is_full(stack):
    return len(stack) == 8

def push(stack, item):
    if not is_full(stack):
        stack.append(item)
        print(f"Pushed {item} onto the stack")
    else:
        print("Stack is full, cannot push.")

def pop(stack):
    if not is_empty(stack):
        popped_item = stack.pop()
        print(f"Popped {popped_item} from the stack")
        return popped_item
    else:
        print("Stack is empty, cannot pop.")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Stack is empty, cannot peek.")

# Example usage:
my_stack = create_stack()

push(my_stack, 1)
push(my_stack, 2)
push(my_stack, 3)
push(my_stack, 4)
push(my_stack, 5)
push(my_stack, 6)
push(my_stack, 7)
push(my_stack, 8)
push(my_stack, 9)  # Attempting to push when the stack is full

peek_value = peek(my_stack)
print(f"Peeked value: {peek_value}")

pop_value = pop(my_stack)
print(f"Popped value: {pop_value}")

pop_value = pop(my_stack)
pop_value = pop(my_stack)
pop_value = pop(my_stack)
pop_value = pop(my_stack)
pop_value = pop(my_stack)
pop_value = pop(my_stack)
pop_value = pop(my_stack)  # Attempting to pop when the stack is empty
