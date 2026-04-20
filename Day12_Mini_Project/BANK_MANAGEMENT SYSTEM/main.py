import json
import random
import string
from pathlib import Path


class Bank:
    database = 'database.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("File does not exist.")
            
    except Exception as error:
        print(f"An error occured as {error}")
        
        
    @classmethod
    def __udate(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountnogenerate(cls): #A class method to generate an account number.
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=5)
        spchar = random.choices("!@#$%^&*",k=1)
        ac_num = alpha + num + spchar
        random.shuffle(ac_num)
        return ''.join(ac_num)
    
# '''-----------------------------------------------------------------------'''

    def CreateAccount(self):
        user_details = {
            "Name": input("Your name: "),
            "Age": int(input("Your age: ")),
            "Email": input("Your email: "),
            "Pin": int(input("Create pin (Pin length between 4 to 6): ")),
            "AccountNo": Bank.__accountnogenerate(),
            "Balance": 0            
        }
        try:
            if user_details["Age"] < 18:
                print("Sorry! To create an account you must be 18.")
            if len(str(user_details["Pin"])) < 4 or len(str(user_details["Pin"])) > 6:
                print("Pin length must be between 4 and 6")
            else:
                print("Account created successfully.")
                for i in user_details:
                    print(f"{i}: {user_details[i]}")
                print("Note down your account number for future purpose.") 
        except Exception as error:
            print(f"An error occured as {error}")
            
        else:    
            Bank.data.append(user_details)
            
            Bank.__udate()

        
        
    def deposite(self):
        accountNo = input("Enter your account number: ")
        pin = int(input("Enter pin: "))
        user_details = [i for i in Bank.data if i["AccountNo"] == accountNo and i["Pin"] == pin]
        
        if user_details:
            deposite_ammount = int(input("Enter ammount to deposite: "))
            if deposite_ammount > 10000 or deposite_ammount <= 0:
                print("Sorry! deposite ammount is too much or too low.(Ammount must be between 1 to 10000)")
            else:
                user_details[0]['Balance'] += deposite_ammount
                
                Bank.__udate()
                
                print(f"Rs.{deposite_ammount} credited to your account successfully.\nYour updated balance: Rs.{user_details[0]["Balance"]}/-")
        else:
            print("Please, check your Account number or Pin!")
            
            
    def withdraw(self):
        accountNo = input("Enter your account no. : ")
        pin = int(input("Enter pin: "))
        
        details = [i for i in Bank.data if i["AccountNo"] == accountNo and i["Pin"] == pin]
        
        if details:
            withdrawal_ammount = int(input("Enter ammount for withdrawal: "))
            if withdrawal_ammount > details[0]["Balance"]:
                print(f"Sorry! Insufficient balance.\nCurrent balance: Rs.{details[0]["Balance"]}/-")
            else: 
                details[0]["Balance"] -= withdrawal_ammount
                
                Bank.__udate()
                
                print(f"Rs.{withdrawal_ammount} debited from your account.\nYour updated balance: Rs.{details[0]["Balance"]}/-")
        
        else:
            print("Check your Account number or Pin!")        
    
    
    def accountDetails(self):
        accountNo = input("Enter your account number: ")
        pin = int(input("Enter pin: "))
        
        details = [i for i in Bank.data if i["AccountNo"] == accountNo and i["Pin"] == pin]
        
        if details:
            print("Your details: ")
            for i in details[0]:
                print(f"{i}: {details[0][i]}")

        else:
            print("Check your Account number or Pin!")
    
    
    def Update(self):
        accountNo = input("Enter your account: ")
        pin = int(input("Enter pin: "))
        
        details = [i for i in Bank.data if i["AccountNo"] == accountNo and i["Pin"] == pin]
        
        if details:
            print("Note: You can update Name, Emailid and Pin only.")
            
            print("Enter details to update and leave empty to skip")
            newData = {
                "Name": input("Enter your new name: "),
                "Email":input("Enter new email: "),
                "Pin": input("Enter new pin: ")
            }
            if newData["Name"] == "":
                newData["Name"] = details[0]["Name"]
            if newData["Email"] == "":
                newData["Email"] = details[0]["Email"]
            if newData["Pin"] == "":
                newData["Pin"] = details[0]["Pin"]
                
            if type(newData["Pin"]) == str:
                newData["Pin"] = int(newData["Pin"])
            
            for i in newData:
                if newData[i] == details[0][i]:
                    continue
                else:
                    details[0][i] = newData[i]
            
            Bank.__udate()
            print("Details updated successfully.")
        else:
            print("Check your Account number or Pin!")
    
    def deletAccount(self):
        accountNo = input("Enter your account no.: ")
        pin = int(input("Enter pin: "))
        
        details = [i for i in Bank.data if i["AccountNo"] == accountNo and i["Pin"] == pin]
        
        if details:
            confirm = str(input("Confirm to delete account,Y for 'Yes' or N for 'No' : "))
            if confirm.casefold() == 'n':
                print("Account not deleted!")
            elif confirm.casefold() == 'y':
                index = Bank.data.index(details[0])
                Bank.data.pop(index)
                
                print("Account deleted successfully!")
                
                Bank.__udate()
            
            else:
                print("Invalid input!!")
        
        else:
            print("Check your Account number or Pin!")
                
        
       
    
user = Bank()

print("Press 1 to Create an account")
print("Press 2 to Deposite money")
print("Press 3 to Withdraw money")
print("Press 4 to See Account Details")
print("Press 5 to Update Account Details")
print("Press 6 to Delete Account")

user_chioce = int(input("Your choice?? : "))

if user_chioce == 1:
    user.CreateAccount()

if user_chioce == 2:
    user.deposite()

if user_chioce == 3:
    user.withdraw()

if user_chioce == 4:
    user.accountDetails()

if user_chioce == 5:
    user.Update()

if user_chioce == 6:
    user.deletAccount()