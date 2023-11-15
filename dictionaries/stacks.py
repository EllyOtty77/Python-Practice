MyStack = []
StackSize = 3
def DisplayStack():
    print("Stack currently contains:")
    for Item in MyStack:
        print(Item)
def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is full!")
def Pop():
    if len(MyStack) > 0:
        MyStack.pop()
    else:

        print("Stack is empty.")
Push(1)
Push(2)
Push(3)
DisplayStack()
input("Press any key when ready...")
Push(4)
DisplayStack()
input("Press any key when ready...")
Pop()
DisplayStack()
input("Press any key when ready...")
Pop()
Pop()
Pop()
DisplayStack()


# In this example, the application creates a list and a variable to determine the
# maximum stack size. Stacks normally have a specific size range. This is
# admittedly a really small stack, but it serves well for the example’s needs.
# Stacks work by pushing a value onto the top of the stack and popping values
# back off the top of the stack. The Push() and Pop() functions perform these
# two tasks. The code adds DisplayStack() to make it easier to see the stack
# content as needed.
# The remaining code exercises the stack (demonstrates its functionality) by
# pushing values onto it and then removing them. Four main exercise sections
# test stack functionality
