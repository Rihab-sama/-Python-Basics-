nbr = int(input("Entrer a number :"))

for nbr in range(1,nbr + 1):
    if  nbr % 15==0 :
        print("FizzBuzz")
    elif nbr % 5==0:
        print("Buzz")
    elif nbr % 3==0:
        print("Fizz")
    else:
        print(nbr)    
                    


    