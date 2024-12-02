# Manasyu Chaudhari             9-16-2024
# Assingment 2

# This basic calculator can do 7 different operations,
# and even generate a lucky number!

import random

print('Lucky Calculator!\n')
print('By: Manasyu Chaudhari')
print('[COM S 1270 2]\n')
print(f'What would you like to do?')

first_input = str(input('[c]alculator, [l]ucky number, [q]uit: '))
operations = ['+', '-', '*', '/', '//', '%', '**']
# This still needs work
if(first_input == 'c'):
    cal_input = input('Please Choose A Calculation [+], [-], [*], [/], [//], [%], [**]: ')
    my_str = cal_input
    if(my_str not in operations):
        print(f'ERROR: Your must enter either "+", "-", "*", "/", "//", "%", or "**"')
    else:
        int1 = int(input('Please Enter An Integer: '))
        int2 = int(input('Please Enter An Integer: '))
        int_result = 0
        if(cal_input == '+'):
            int_result = int1 + int2
            
        elif(cal_input == '-'):
            int_result = int1 - int2
            
        elif(cal_input =='*'):
            if((int1 == 0) or (int2 == 0)):
                int_result = 0
            else:
                int_result = int1 * int2
        elif(cal_input == '/'): 
            if((int2 == 0) or (int1 == 0)):
                int_result == 0
            else:
                int_result = int1 / int2
            #ask question about this
        elif(cal_input =='//'):
            if(int2 == 0):
                print(f'ERROR in {cal_input} Function: b = {int2}')
                int_result = int1
            else:
                int_result = int1 // int2
            
        elif(cal_input == '%'):
            int_result = int1 % int2
            
        elif(cal_input == '**'):
            if(int1 == 0):
                print(f'ERROR in {cal_input} Function: a = {int1}')
                int_result = 0
            elif(int2 == 0):
                int_result = 1
            else:
                int_result = int1 ** int2
            
        print(f'The Result of your calculation was: {int_result}')
    
#Below finsihed
elif(first_input == 'l'):
    int1 = int(input('Please Enter An Integer: '))
    int2 = int(input('Please Enter An Integer: '))
    print(int1)
    print(int2)
    int_result = 0
    if(int1 > int2):
        int_result = random.randint(int2, int1)
    else:
        int_result = random.randint(int1, int2)
    print(f'Your lucky number is: {int_result}')
# Below finished
elif(first_input == 'q'):
    print(f'Goodbye!')
#below finished
else:
    print('ERROR: I did not understand your input... Please try again...')