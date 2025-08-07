class Library:
    def __init__(self):
        self.a=["Great Expectations","Oliver Twist","To Kill a Mockingbird","Treasure Island","The Alchemist","The Zahir","The Room on the Roof","My India","The Wings of Fire","Ignited Minds","The Living Vedanta","Around the World in Eighty Days", "Jataka Tales"]
        self.c=[]

    def Borrow(self):
        a=self.a
        c=self.c
        j=0
        for i in a:
            print(j+1,i)
            j+=1
        name=int(input("Choose the book you want to borrow: "))
        if name<len(a):
            c.append(a[name])
            print("Book borrowed successfully.")
        else:
            print("Sorry, Book not found.")

    def Return(self):
        c=self.c
        name=input("Enter name of the book to be returned: ")
        if name in c:
            c.remove(name)
            print("Book returned successfully.")
        else:
            print("Name of the book mentioned not borrowed.")


class Student(Library):
    def details(self):
        self.nameStudent=input("Enter your name: ")
        self.classof=int(input("Enter your class: "))
        self.roll=int(input("Enter your roll number: "))
    
    def Show(self):
        c=self.c
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Details:\nName: {self.nameStudent}\nClass: {self.classof}\nRoll No.: {self.roll}\nBooks borrowed: ")
        if c==[]:
            print(0)
        else:
            for i in c:
                print(i)
        
        
if __name__ =="__main__":
    obj=Student()
    obj.details()
    c=-1
    while c!=0:
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
        ch=int(input("Choose from the following:\n 1.Borrow a book.\n 2.Return the borrowed book.\n 3.Show Details.\n 4.Quit.\nChoice: "))
        match ch:
            case 1: 
                obj.Borrow()
            case 2: 
                obj.Return()
            case 3: 
                obj.Show()
            case 4: 
                c=0
            case _:
                print("Wrong choice. Try again.")
