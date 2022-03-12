print('insert your card')
atm_pin='9999'
balance=10000
transcation='balance enquiry','withdraw money', 'deposite', 'change atm_pin','transfer_money','quit'
"""if pin is correct then it will go to transcation otherwise it will go to the else condition"""
print('choose your transaction')
print('1. balance enquiry')
print('2. withdraw money')
print('3. deposite')
print('4. change atm_pin')
print('5. transfer_money')
print('6. quit')
trans=input('transaction')
if trans=='balance enquiry':
    print(balance)
elif trans=='withdraw money':
    pin=int(input("Enter Your Pin"))
    if pin==atm_pin:
        amt=int(input('enter your amount'))
        if amt>0:
            print('Collect Your Cash, Thanks For Using PNB Bank!')
        else:
            print('please enter valid amount' )
elif trans=='deposite':
    deposite=input ('enter your amount to deposite')
    if deposite>0:
        print('your cash has been successfully deposited')
    else:
        print('enter valid amount')

elif trans=='change your pin':
    change_pin=int(input("enter your pin"))
    if change_pin>0:
        print('your pin has successfully change')
    else:
        print('enter valid pin')
elif trans=='transfer_money':
    transfer_money=input('enter your amount to transfer')
    if transfer_money>0:
        print('your amount transfer successfully')
    else:
        print('enter valid amount')
elif trans =='quit':
    quit_1=input('press yes to quit')
    if quit_1=='yes':
        print('quit')
else:
    print('choose any other transaction')
    
