print('''
      Salect operation :
    1 : addition 
    2 : Subtract
    3 : multiply 
    4 : Dividu
      ''')
while True:
    choice =int(input('Enter Choice :'))
    if choice in (1,2,3,4):
        num1= int(input('Enter frist num :'))
        num2= int(input('Enter secand num :'))
        if choice ==1:
            resulte = num1 + num2
            print(f'{num1} + {num2} = {resulte}' )
        elif choice ==2:
           resulte = num1 - num2
           print(f'{num1} - {num2} = {resulte}' )
        elif choice ==3:
           resulte = num1 * num2
           print(f' {num1} * {num2} = {resulte}' )
        elif choice ==4:
           resulte = num1 /  num2
           print(f' {num1} / {num2} = {resulte}' )
        else :
            print('''Error 
                      Enter ckoise (1 or 2 or 3 or 4)''')
        nextcalc = input ("let's do next calcuation (Yes or no )")
        if nextcalc== "no" :
            break
    else:
        print ("Eroor")
            
          