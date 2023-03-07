class User:
    def __init__(self,name,roll,password):
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=[]
        self.returned_books=[]


class Library:
    def __init__(self,book_list):
        self.book_list=book_list
   
    def check_availablity(self):
        for book in self.book_list:
            if self.book_list[book]>0:
               print(book,self.book_list[book])


    def borrow_book(self,book_name,user):
        for book in self.book_list:
            if book==book_name:
                if book_name in user.borrow_books:
                    print("Age ferot dao")
                    return
                if self.book_list[book]==0:
                    print("Book shes hoye geche")  
                    return
                self.book_list[book] -= 1
                user.borrow_books.append(book_name)
                print("You have borrowed a book")  
                return
        print("Your book is not available")




    def return_book(self,book_name,user):
        for book in self.book_list:
            if book==book_name:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(book_name)
                    user.returned_books.append(book_name)
                    print("Returned book successfully")
                    return
                else:
                    print("Thanks but this book is not our")
                    return
        print("This book does not exist in out library")  


   
    def donate_book(self,book_name,amount):
        for book in self.book_list:
            if book==book_name:
                self.book_list[book] += amount
                print("Thanks for donating")
                return
        self.book_list[book_name] = amount
        print("Thanks for donating")




library=Library({"English":1, "Bangla":5, "Math":3})
#print(library.book_list)
   
allUsers=[]
currentUsers=None


while True:
    if currentUsers==None:
        print("Not logged in\nPlease log in or Create account\n\n")
        print("Choose Log in or Create option")
        print("Log in (Press L)")
        print("Creat an account (Press C)")
        option=input()
       
        if option=='L':
           roll=int(input("Roll: "))
           password=int(input("Password: "))
           match=False
           for user in allUsers:
              print(user)
              if user.roll==roll and user.password==password:
                currentUsers=user
                match=True
           if match==False:
               print("No user found")
        else:
            name=input("Name: ")
            roll=int(input("Roll: "))
            password=int(input("Password: "))
            found=False
            for user in allUsers:
                if user.roll==roll:
                   found=True
            if found:
                print("This user has already exist")
                continue
            user=User(name,roll,password)
            currentUsers=user
            allUsers.append(user)
    else:
        print("Option")
        print("_________")
        print("1. Borrow books")
        print("2. Return books")
        print("3. Check book availability")
        print("4. Borrow booklist")
        print("5. Return booklist")
        print("6. Donate books")
        print("7. Log out")


        x=int(input("Give Option: "))
        if x==1:
            book_name=input("Give book name: ")
            library.borrow_book(book_name,currentUsers)
        elif x==2:
            book_name=input("Give book name: ")
            library.return_book(book_name,currentUsers)
        elif x==3:
            library.check_availablity()
        elif x==4:
            print(currentUsers.borrow_books)
        elif x==5:
            print(currentUsers.returned_books)
        elif x==6:
            book_name=input("Give book name: ")
            amount=int(input("Give book amount: "))
            library.donate_book(book_name,amount)
        elif x==7:
            currentUsers=None
        print("\n\n\n")
