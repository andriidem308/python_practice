class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data, end=" ")
            print_val = print_val.next
        print()

    def at_beginning(self, new_data):
        new_node = Node(new_data)
        # Update the new nodes next_val to existing node
        new_node.next = self.head
        self.head = new_node

    def at_end(self, new_data):
        new_node = Node(new_data)

        # if LinkedList is Empty
        if self.head is None:
            self.head = new_node
            return
        last = self.head

        # while not reached the last one
        while last.next:
            last = last.next

        # for last -> next_val - it is new_node
        last.next = new_node

    def in_between(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is absent!")
            return

        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    def remove_node(self, remove_key):
        # our checking element to delete. default: head of LL
        check_element = self.head

        # if element (in this case - head of LL) we have to remove
        if check_element is not None:
            if check_element.data == remove_key:
                self.head = check_element.next
                del check_element
                return

        # setting previous element for checking element
        prev = check_element
        while check_element is not None:
            if check_element.data == remove_key:
                break
            prev = check_element
            check_element = check_element.next

        if check_element is None: return

        # ex: a-b-c-d-e. we want to remove <c>
        # b.next = c; c.next = d;
        # so, after this we'll have:
        # b.next = c.next -> b.next = d; => a-b-d-e
        prev.next = check_element.next

        # delete trash
        del check_element


linked_lst = LinkedList()
linked_lst.head = Node("Mon")

node_2 = Node("Tue")
linked_lst.head.next = node_2

linked_lst.at_end("Wed")
linked_lst.at_end("Thu")
linked_lst.at_end("Fri")
linked_lst.at_end("Sat")
linked_lst.at_end("Sun")

linked_lst.remove_node("Fri")
linked_lst.list_print()

