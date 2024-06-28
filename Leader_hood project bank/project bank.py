def accounts(account):
    acc_numbers = input("Enter account number: ")
    name = input("Enter Your Bank Account Name: ")
    deposit = float(input("Enter Deposit: "))
    type = "normal, VIP, Golden VIP"
    print(type)
    account_type = input("enter your account type: ")
    account[acc_numbers] = [name, deposit, account_type]
    print("You registred succesfully!")
def perfom_transaction(accounts):
    #info about acc where we want wo transact
    acc_num = input("Enter account number: ")
    #main transaction
    if acc_num in accounts:
        print("1. Deposit")    #
        print("2. Withdraw")
        deposit_or_withdraw = input("You Want Deposit Or Withdraw?: ")
        amount = float(input("Enter amount: "))
        #if we choice deposir
        if deposit_or_withdraw == 1:
            accounts[acc_num][1] += amount #აქ ნებისმიერ შემთხვევაში შეგიძლია დაუმატო ამოუნთი ჩვვენს ბალანსს
            print("amount is deposited successfullly thank you for credit!")
        #if we choice withdraw
        elif deposit_or_withdraw == 2:
            if accounts[acc_num][1] >= amount:   #აქ თუ მეტია აქაუნთის ბალანსი ამოუნთზე მაშინ წარმატებით გამოაკლდება ამოუნთი და გამოიტანს ეკრანზე 27 ხაზის პრინტს
                accounts[acc_num][1] -= amount
                print("Amount Withdraw successfully Done!")
            #we have no balance thats why we cant withdraw
            else:
                print("0 balance")
        else:                            #აქ როდესაც ისეთ ტრანზაქციას ვაკეთებთ რაც აქაუნთზე არგვაქვს მაშინ დაპრინტავს 
            print("invalid choice")  
    #we choice account thats never existed  
    else:
        print("Account not found") #აქაუნთი თუ არ შექმნეს ზემოთ მაშინ გამოიტანდ ამას

def update_account(accounts):#account update
    acc_num = input("Enter account number: ") #აქ შეყავს მომხმარებერს თავისი აქაუნთის რიცხვი
    if acc_num in accounts: #იფ ფუნქციის მეშვეობით acc_num დავაკავშირეთ accounts
        name = input("please enter your new name: ") # აქ ვაცვლევინებ თავის სახელს, ახალი სახელი რაც უნდა ის უნდა დაწეროს და შეიცვლება 
        acc_type = input("Enter new account type: ") #აქ შევცვლით აქაუნთის ტიპს
        accounts[acc_num][0] = name #აქ 0 ინდექსზე შეეცვლება მნიშვნელობა და ჩაისმევა ის რასაც შეიყვანს მომხმარებელი name ში
        accounts[acc_num][2] = acc_type #აქ კი 2 ინდექსზე შეიცვლება იგივე ნაირად 
        print("Account information updated successfully")
    else:
        print("Account not found!!!") #ეს თუ აქაუნთი არ შეუქმნიათ ზევით მაშინ გამოიტანს ერორს
