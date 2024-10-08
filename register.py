# User Register Signin Signup
from database import *
from customer import *
from bank import Bank
import random
def SignUp():
    username = input ("Create Username: ")
    cursor.execute (f"SELECT username FROM customers where username = '{username}'; ")
    temp = cursor.fetchall()
    if temp: 
        print("Username Already Exists")
        SignUp()
    else:
        print ("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter your Name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")

        # Generate account number and check if it's unique
        while True:
            account_number = int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number= '{account_number}';")
            if temp:
                continue   # If account number exists, generate again
            else:
                print ("Your Account Number",account_number)  
                break # Exit the loop if account number is unique

    cobj1 = Customer ( username, password, name, age, city, account_number)
    cobj1.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()




def SignIn():
        username = input ("Enter Username: ")
        temp = db_query(f"SELECT username FROM customers WHERE username= '{username}';")
        if temp:
            while True:
                password = input(f"Welcome {username.capitalize()}Enter Password: ")
                temp = db_query(f"SELECT password FROM customers WHERE username= '{username}';")
                # print(temp[0][0])
                if temp[0][0] == password:
                    print ("Sign In successfully")
                    return username
                else:
                    print("Wrong password Try again")
                    continue



        else:
            print("Enter Correct Usernamee:")
            SignIn()


