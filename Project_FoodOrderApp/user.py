
import admin as ad
import json
from datetime import datetime
class User:
    login_info = {}
    profile = {}
    myorders={}

    def __init__(self, usrname, fullname, phoneno, email, address, password):
        self.usrname = usrname
        self.fullname = fullname
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.usrname] = self.password
        User.profile[self.usrname] = {"Name":self.fullname,"Phone Number":self.number,"Email":self.email,"Address":self.address,"Password":self.password}
        self.order_history = {}
        self.orders=1

    def login(username, password):
        with open("userlogininfo.txt","r",encoding='utf-8') as userlogininfo:
            login_info=json.load(userlogininfo)
        if login_info.get(username) == password:
            return True
        else:
            return False


    def place_order(self):
        print("What you want to order here in the MENU")
        print(ad.show_usrmenu())
        user_choice = int(input("If you want to order then select 1.YES 2.NO - "))
        if user_choice == 1:
            l1 = input("Enter the Food ID here: ")
            foodid=[]
            quan=[]
            price=[]
            total=[]
            x=0
            for word in l1:
                if word.isdigit():
                    foodid.append(int(word))
            for id in foodid:
                l2 = int(input(f"Enter the Quantity of item for Food ID-{id} here: "))
                quan.append(l2)           
            again_ask = input("Are you still want to order this Enter YES or NO:-  ")
            if again_ask.upper() == "YES":
                print("\n**********Your Cart is***********")
                for k in range(len(foodid)):
                    print(f'''{ad.menu[foodid[k]]["Name"]} ({ad.menu[foodid[k]]["Quantity"]}) [{ad.menu[foodid[k]]["Price"]}] x {(quan[k])} = {quan[k]*ad.menu[foodid[k]]["Price"]}''')
                    total.append((ad.menu[foodid[k]]["Price"]*quan[k])-(ad.menu[foodid[k]]["Discount"]*ad.menu[foodid[k]]["Price"]*100))   
                print(f"It costs you {sum(total)}INR in total")
                for l in range(len(foodid)):
                    self.order_history[self.orders] = {
                                    "Item Name":ad.menu[foodid[l]]["Name"],
                                    "Price": ad.menu[foodid[l]]["Price"],
                                    "Quantity": quan[l]
                                    }
                    self.orders+=1
                for m in range(len(foodid)):      
                    final_stock = ad.menu[foodid[m]]["Stock"] - quan[m]
                    ad.menu[foodid[m]]["Stock"] = final_stock
                print("You're order is successfully placed\n")

            elif again_ask.upper() == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")
        User.myorders={}
        for i in self.order_history:
            now=datetime.now()
            time=str(now)
            User.myorders[time]=self.order_history[i]
            for j in range(1000000):
                pass
        self.order_history={}


    def update_profile(self):
        onm = input("Enter your Username:- ")
        print("*****Your Profile*******")
        print(User.profile[onm])
        nm = input("Enter your Name here: ")
        pn = int(input("Enter your Phone number here: "))
        em = input("Enter your Email here: ")
        ad = input("Enter your Address here: ")
        pd = input("Enter your Password here: ")
        User.profile[onm]["Name"] = nm
        User.profile[onm]["Phone Number"] = pn
        User.profile[onm]["Email"] = em
        User.profile[onm]["Address"] = ad
        User.profile[onm]["Password"] = pd
        print("*****Edited Profile successfully*****")
        print(User.profile[onm])
        User.login_info[onm]=pd
        


        


       

