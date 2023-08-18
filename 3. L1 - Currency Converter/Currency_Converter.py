def print_menu():
    print('Enter one of the following currency :')
    print('* Euro')
    print('$ Dollar')
    print('+ British Pound')
    print('Y yen')
    print('R Riyal')
    print('c close')
    print()

def currency_conv(choice):
    if choice in ('*','$','+','Y','R'):
        
        selling_price=eval(input('Enter the selling price:'))
        buying_price=eval(input('Enter the buying price:'))
        choice2=eval(input('Would you like to buy or sell (0 for buy, 1 for sell)\n'))
        if choice2 in (0,1):
            amount=eval(input( 'Please enter the amount\n'))
            if amount==0:
                print(f'Your output number is ',amount * selling_price)
            else:
                print(f'Your output number is ',amount * buying_price)

        else:
            print('wrong choice try again\n')  

    else:
        print('wrong choice try again\n')  


while True:
    print_menu()
    choice=input()
    currency_conv(choice)
    if choice=='c':
        print('Thank you')
        break

    


