class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def sort(self):
        sorted_list = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_list = self.insert_sorted(sorted_list, cur)
            cur = next_node
        self.head = sorted_list

    def insert_sorted(self, head, node):
        if not head or node.data < head.data:
            node.next = head
            return node

        cur = head
        while cur.next and cur.next.data < node.data:
            cur = next
        node.next = cur.next
        cur.next = node
        return head

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        l1 = list1.head
        l2 = list2.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


if __name__ == "__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    # llist.print_list()
    llist2 = LinkedList()

    # Вставляємо вузли в початок
    llist2.insert_at_beginning(1)
    llist2.insert_at_beginning(12)
    llist2.insert_at_beginning(19)
    LinkedList.print_list(LinkedList.merge_sorted_lists(llist, llist2))
    # llist.sort()
    # llist.reverse_list()
    # llist.print_list()

    # # Вставляємо вузли в кінець
    # llist.insert_at_end(20)
    # llist.insert_at_end(25)

    # # Друк зв'язного списку
    # print("Зв'язний список:")
    # llist.print_list()

    # # Видаляємо вузол
    # llist.delete_node(10)

    # print("\nЗв'язний список після видалення вузла з даними 10:")
    # llist.print_list()

    # # Пошук елемента у зв'язному списку
    # print("\nШукаємо елемент 15:")
    # element = llist.search_element(15)
    # if element:
    #     print(element.data)
