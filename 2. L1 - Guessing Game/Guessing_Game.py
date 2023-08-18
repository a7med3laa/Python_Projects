import random


number = random.randint(1, 100)

guess = 0



while True:
   
    guess = int(input("Enter your guess number : "))
      
    if guess == number:
        
        print ('congratulation !! ',guess, "is the right number")
        break
    
        
    elif guess > number :
        
        print ("you have enter number greater than our number")
    
    else :
        
        print ("you have enter a smaller number than our number")
