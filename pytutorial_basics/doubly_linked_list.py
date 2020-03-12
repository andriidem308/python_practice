class DNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data, end=" ")
            print_val = print_val.next
        print()

    # def node_print(self, node):
    #     while node is not None:
    #         print(node.data, end=" ")
    #         node = node.next
    #     print()

    def at_beginning(self, new_data):
        new_node = DNode(new_data)
        # Update the new nodes next_val to existing node
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def at_end(self, new_data):
        new_node = DNode(new_data)
        new_node.next = None

        # if DLinkedList is Empty
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node  # for last -> next_val - it is new_node
        new_node.prev = last
        return

    def in_between(self, middle_node, new_data):
        if middle_node is None:
            print("The mentioned node is absent!")
            return
        new_node = DNode(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node
        new_node.prev = middle_node
        if new_node.next is not None:
            new_node.next.prev = None

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


dl_lst = DLinkedList()
dl_lst.head = DNode("Mon")

node_2 = DNode("Tue")
dl_lst.head.next = node_2

dl_lst.at_beginning("1")
dl_lst.at_end("2")
dl_lst.at_end("3")
dl_lst.at_end("8")
dl_lst.at_end("4")

dl_lst.list_print()
dl_lst.in_between(dl_lst.head.next.next.next, '7')
dl_lst.list_print()

