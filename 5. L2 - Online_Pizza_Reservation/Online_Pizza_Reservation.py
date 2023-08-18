#print welcome menu of resturant
def print_menu ():
    print('Welcome to our Pizza restaurant!!!')
    print('Please select one of items')
    print('1- SUPER SUPREME - S=50 /M=75.5/ L=100')
    print('2- CHICKEN SUPREME - S=45/ M=73.88/ L=97.99')
    print('3- MARGHERITA - S=35/ M=70/ L=95')
    print('4- CHEESE LOVERS - S=60.96/ M=87.75/ L=113.16')
    print('5- SEAFOOD LOVERS - S= 64.47/ M=94.30/ L=123.25')

# get bill of order get type of pizza and quantity and size of it
def calc_bill(choice,q,size):
    bill=(pizza[choice-1].get(size))*q
    return bill


# list of dictionary for all pizza types and sizes
pizza=[{'S':50,'M':75.5,'L':100 },
       {'S':45,'M':73.88,'L':97.99 },
       {'S':35,'M':70,'L':95 },
       {'S':60.96,'M':87.75,'L':113.16 },
       {'S':64.47,'M':94.30,'L':123.25 },]

# final order for user after finish ordering
final_bill=0

# main loop of code
while True:
  
    print_menu()

    choice=eval(input('What is your choice? \n'))

    # check choice of pizza type
    if choice in (1,2,3,4,5):
        print ('You select',end=" ")

        if choice==1:
            print('SUPER SUPREME')
        elif choice==2:
            print('CHICKEN SUPREME')
        elif choice==3:
            print('MARGHERITA')
        elif choice==4:
            print('CHEESE LOVERS')
        else:
            print('SEAFOOD LOVERS')
        
        # get quantity of pizza number
        q=int(input('Enter your quantity \n'))
        
        # get size
        size=input('Enter Size \n')
        
        # check size of pizza
        if size not in ('S','M','L'):
            print('\nwrong choice try again\n')
            continue
            
        else:
            final_bill+=calc_bill(choice,q,size)
            
            
        
        # check if you want another item
        newOrder=input('Do you want another item? (yes/no) \n')

        if newOrder=='no' or newOrder == 'NO':
            print('Thank you for using our application your bill = ',final_bill)
            break

    else:
        print('\nwrong number choose again\n')