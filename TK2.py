class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def count_even(self):
        count = 0
        current = self.head
        while current is not None:
            if current.data % 2 == 0:
                count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Hàm đọc file và khởi tạo danh sách liên kết
def create_linked_list_from_file(filename):
    linked_list = LinkedList()
    with open(filename, 'r') as file:
        for line in file:
            data = int(line.strip())
            linked_list.insert_at_beginning(data)
    return linked_list

# Main function
def main():
    # Khởi tạo danh sách liên kết từ file "data.txt"
    filename = "data.txt"
    linked_list = create_linked_list_from_file(filename)

    print("Danh sách liên kết ban đầu:")
    linked_list.display()

    # Thêm Node vào giữa danh sách liên kết
    data_to_insert = int(input("Nhập giá trị Node cần chèn vào giữa danh sách liên kết: "))
    position_to_insert = int(input("Nhập vị trí cần chèn (tính từ 0): "))
    linked_list.insert_at_middle(data_to_insert, position_to_insert)

    print("Danh sách liên kết sau khi chèn Node:")
    linked_list.display()

    # Xóa Node ở cuối danh sách liên kết
    linked_list.delete_at_end()
    print("Danh sách liên kết sau khi xóa Node ở cuối:")
    linked_list.display()

    # Đếm số lượng phần tử là số chẵn trong danh sách liên kết
    count_even = linked_list.count_even()
    print("Số lượng phần tử chẵn trong danh sách liên kết:", count_even)

if __name__ == "__main__":
    main()
