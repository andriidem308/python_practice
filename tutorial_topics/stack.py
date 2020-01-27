class Stack:
    # creating a <Stack> object as a empty list
    def __init__(self):
        self.stack = []

    # output stack
    def __str__(self):
        return str(self.stack[::-1])

    # add element <data> to the <Stack> (to the top of it)
    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    # remove element from the top of the stack
    def remove(self):
        if len(self.stack) <= 0:
            return "No elements in the stack!"
        return self.stack.pop()

    # look what is at the top (return this element)
    def peek(self):
        return self.stack[-1]


# creating new Stack
my_stack = Stack()

# adding elements to the <my_stack>
print("\n\t\t***** Adding some elements to the <my_stack> *****")
print("Stack <my_stack> BEFORE adding elements\t:\t", my_stack)
my_stack.add(4)
my_stack.add(3)
my_stack.add(1)
my_stack.add(7)
my_stack.add(9)
my_stack.add(-2)
my_stack.add(14)
my_stack.add(0)
print("Stack <my_stack> AFTER adding elements\t:\t", my_stack)

# visualisation of removing elements from <my_stack>
print("\n\t\t***** Removing some elements from the <my_stack> *****")
print("Stack <my_stack> BEFORE removing some elements\t:\t", my_stack)
print("-- remove element <", my_stack.remove(), ">\t\t# [14, -2, 9, 7, 1, 3, 4]", sep='')
print("-- remove element <", my_stack.remove(), ">\t\t# [-2, 9, 7, 1, 3, 4]", sep='')
print("-- remove element <", my_stack.remove(), ">\t\t# [9, 7, 1, 3, 4]", sep='')
print("-- remove element <", my_stack.remove(), ">\t\t# [7, 1, 3, 4]", sep='')
print("Stack <my_stack> AFTER removing some elements\t:\t", my_stack)


