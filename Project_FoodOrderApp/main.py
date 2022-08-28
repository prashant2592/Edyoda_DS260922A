import admin as aa
from user import User
import json

uhh=User("admin","Prashant",8220251591,"dp@gmail.com","4, Dharmapuri","admin")
ordhiss={}
with open("orderhistory.json","r",encoding='utf-8') as orderhist2:
    check5=json.load(orderhist2)
for i in User.login_info:
    ordhiss[i]={}
    if(not(check5.get(i))):
        with open("orderhistory.json","w",encoding='utf-8') as orderhist:
            json.dump(ordhiss,orderhist)

with open("userlogininfo.json","r",encoding='utf-8') as userlogininfo:
    check1=json.load(userlogininfo)
for i in User.login_info:
    if(not(check1.get(i))):
        with open("userlogininfo.json","w",encoding='utf-8') as userlogininfo:
            json.dump(User.login_info,userlogininfo)
with open("userprofileinfo.json","r",encoding='utf-8') as userprofileinfo:
    check2=json.load(userprofileinfo)
for i in User.profile:
        if(not(check2.get(i))):
            with open("userprofileinfo.json","w",encoding='utf-8') as userprofileinfo:
                json.dump(User.profile,userprofileinfo)

Loop=True
while Loop:
    inp = int(input("LOGIN AS Admin(press 1)\nLOGIN AS User(press2)\nExit(press 3) \t Enter your choice:- "))
    if inp == 1:
        print("Welcome to the user panel")
        signupp=True
        while signupp:
            optt=int(input("***ADMIN PANEL*** \nFor Sign in(press 1)\nExit(press 2) \t Enter your choice:- "))
            if optt == 1:
                Username = input("USERNAME: ")
                Password = input("PASSWORD: ")
                if aa.admin_keys[Username] == Password:
                    print("*****You have successfully logged in*****")
                    admin_crawler = True
                    while admin_crawler:
                        adm_choice = int(input("1.ADD NEW FOOD ITEM\n2.EDIT FOOD ITEM\n3.VIEW MENU\n4.REMOVE FOOD ITEM\n5.LOGOUT\t Choose the options: "))
                        if adm_choice == 1:
                            aa.add_new_item()
                        elif adm_choice == 2:
                            aa.edit_from_item()
                        elif adm_choice == 3:
                            aa.show_menu()
                        elif adm_choice == 4:
                            aa.show_menu()
                            aa.remove_item()
                        elif adm_choice == 5:
                            print("LOGGED OFF")
                            admin_crawler = False
                        else:
                            print("This is the wrong selection. Please select valid option")
                else:
                    print("Username or Password is invalid")
            else:
                signupp=False
                
    elif inp == 2:
        print("Welcome to the user panel")
        signup=True
        while signup:
            opt=int(input("***USER PANEL*** \n For Sign in(press 1)\n For Sign up(press 2) \nExit(press 3) \t Enter your choice:- "))
            if opt == 1:
                username = input("Enter the username here: ")
                password = input("Enter the password here: ")
                if User.login(username, password):
                    print(f"You are logged in successfully {username}")
                    user_crawler = True
                    while user_crawler:
                        usr_choice = int(input(f"1.Place new order \n2.Order history \n3.Update Profile \n4.Logout \t {username}, Enter the option:- "))
                        if usr_choice == 1:
                            uhh.place_order()
                        elif usr_choice == 2:
                            print(f"****Here is your order history, {username}****\n")
                            with open("orderhistory.json","r",encoding='utf-8') as orderhistory1:
                                orders=json.load(orderhistory1)
                            temporder={}
                            temporder[username]={}
                            oh=User.myorders                                                    
                            for i,j in oh.items():
                                temporder[username][i]=j
                            
                            orders[username].update(temporder[username])
                            with open("orderhistory.json","w",encoding='utf-8') as orderhistory3:
                               json.dump(orders,orderhistory3)  
                                                            
                            for i in orders[username]:
                                print("Item Name:- ",orders[username][i]["Item Name"])
                                print("Price:- ",orders[username][i]["Price"])
                                print("Quantity:- ",orders[username][i]["Quantity"])
                                print("Total Amount :- ",orders[username][i]["Price"]*orders[username][i]["Quantity"]," INR")
                                print("Order time:- ",i)
                                print("\n")
                        elif usr_choice == 3:
                            uhh.update_profile()
                        elif usr_choice == 4:
                            user_crawler = False
                            print("You're Successfully logged out")
                        else:
                            print("You choose the invalid option")
                else:
                    print("These are the wrong credentials! SORRY!!!")
            elif opt == 2:
                print("*****Please fill the Profile*******")
                usnm=input("Enter the username here: ")
                if(check1.get(usnm)):
                    print("****Username already exists, Please try another****")
                else:   
                    pwd=input("Enter the password here: ")
                    flnm=input("Enter the Full Name here: ")
                    phno=int(input("Enter the Phone Number here: "))
                    emid = input("Enter your Email here: ")
                    add = input("Enter your Address here: ")
                    print("*******Successfully signed up**********")
                    call=User(usnm,flnm,phno,emid,add,pwd)
                    with open("userlogininfo.json","w",encoding='utf-8') as userlogininfo:
                        json.dump(User.login_info,userlogininfo)
                    with open("userprofileinfo.json","w",encoding='utf-8') as userprofileinfo:
                        json.dump(User.profile,userprofileinfo)
                    with open("orderhistory.json","r",encoding='utf-8') as orderhistory4:
                        ordhis=json.load(orderhistory4)
                    ordhis[usnm]={}
                    with open("orderhistory.json","w",encoding='utf-8') as orderhistory5:
                        json.dump(ordhis,orderhistory5)
            else:
                signup=False
            
    else:
        Loop=False
        exit()




