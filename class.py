class Mylist1():
    def __init__(self):
        self.data = []
    def add_element(self , element):
        self.data.append(element)
    def remove_element(self , element):
        if element in self.data:
            self.data.remove(element)
        else:
            print("Element not found")
    def display(self):
        if self.data:
            print("Elements are : " , end = " ")
            for element in self.data:
                print(element)
        else:
            print("List is empty")

list1 = Mylist1()
while(1):
    choice = int(input("1.Append\n2.Delete\n3.Display\n4Exit\nEnter your choice = "))
    if(choice == 1):
        element = int(input("Enter the value = "))
        list1.add_element(element)
    elif(choice == 2):
        element = int(input("Enter the element to be deleted : "))
        list1.remove_element(element)
    elif(choice == 3):
        list1.display()
    elif(choice == 4):
        break
    else:
        print("Enter the valid choice !!!!")