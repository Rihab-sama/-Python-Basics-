while True:
    nbr1=float(input("enter the ferst nember:"))
    nbr2=float(input("enter the second nember:"))
    oper=input("choose your operation :") 

    if oper == '+':
         result = nbr1 + nbr2
    elif oper == '-':
         result = nbr1 - nbr2
    elif oper == '*':
        result = nbr1 * nbr2
    elif oper == '**':
        result =nbr1 ** nbr2    
    elif oper == '/':
        if nbr2 == 0:
             result = "Dividing by 0 is not possible"
        else:
            result = nbr1 / nbr2
    else:
         result= "the operation is Invalid. Please try again."     
    print(f"the resulta is {result}") 
    
    pause=input("do you wante to continu yes or no")
    
    if pause == 'no' :
        break


          
     
     
     
     
     
     


