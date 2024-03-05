import os
os.system("cls")
os.chdir("C:\\Codes\\Py_Codes\\Files")

try:
    file = open("Users.txt", "r+")

except FileNotFoundError:
    print("404 Not Found")
    exit(1)

else:
    data = file.readlines()
    data = list(map(lambda i: i[:-1].split(","), data))

class User:
    def ask(self):
        answer = int(input("Are you already signed up?\n1.Yes\n2.No\n"))
        if answer == 1:
            self.signIn(data)
        elif answer == 2:
            self.signUp()

    def signUp(self):
        os.system("cls")
        print("Sign Up")
        self.__name = input("F.I.SH -> ")
        self.__age = input("Age -> ")
        self.__gender = input("Gender -> ")
        self.__pnumber = input("Phone number -> ")
        self.__email = input("Email -> ")
        self.__password = input("Password -> ")
        self.__address = input("Address -> ")
        self.__idcard = input("Your ID-card -> ")
        self.__postcode = input("Postcode -> ")
        file.writelines(f"{self.__name}, {self.__age}, {self.__gender}, {self.__pnumber}, {self.__email}, {self.__password}, {self.__address}, {self.__idcard}, {self.__postcode}")
        file.seek(0)
        data = file.readlines()
        data = list(map(lambda i: i[:-1].split(","), data))
        input("You're signed up :)\nPress Enter to continue\n")
        self.signIn(data)

    def signIn(self, data):
        os.system("cls")
        print("Sign In")
        email = input("Email -> ")
        password = input("Password -> ")
        for i in data:
            if i[4].strip() == email and i[5].strip() == password:
                userData = i
                input("You're signed in :)\nPress Enter to continue\n")
                self.menu(userData)
        print("You're not signed up!")
        self.signUp()

    def menu(self, userData):
        os.system("cls")
        n = int(input("1.Take a loan\n2.Loan calculator\n3.Change password\n4.Exit\n"))
        
        if n == 1:
            os.system("cls")
            choice = input("Loan amount 115 million with 15% collateral for 2 years\nPress Enter to accept the agreement\n")
            if choice == "":
                print("Accepted ;)")
                exit(1)
            else:
                self.menu(userData)
        
        elif n == 2:
            os.system("cls")
            amount = int(input("Enter the amount of loan you want to take -> "))
            input(f"{(amount*15)//100} with 15% collateral for 2 years\nPress Enter to return to menu\n")
            self.menu(userData)

        elif n == 3:
            os.system("cls")
            new = input("Create a new password -> ")
            for i in data:
                if i[5].strip() == userData[5].strip():
                    i[5] = new
                    break
            file = open("Users.txt", "w+")
            file.write("".join(data))
            input("Changed ;)\nPress Enter to continue\n")
            self.menu(userData)

        elif n == 4:
            os.system("cls")
            print("Good Bye ;)")
            exit(1)


user1 = User()
user1.ask()