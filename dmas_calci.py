def add(a,b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def factorial(a):
    return 1 if (a==1 or a==0) else a * factorial(a - 1)

def main():
    d=int(input('Tell me your choice (1/2/3/4/5) '))
    if d == 1:
        x=float(input('Tell me your 1st number: '))
        y=float(input('Tell me your 2nd number: '))
        z=add(x,y)
        print('After adding '+str(x)+' and '+str(y)+', We get '+ str(z))
    elif d==2:
        x=float(input('Tell me your 1st number: '))
        y=float(input('Tell me your 2nd number: '))
        z=substract(x,y)
        print('After substracting '+ str(x)+' and'+str(y)+', We get '+str(z))
    elif d==3:
        x=float(input('Tell me your 1st number: '))
        y=float(input('Tell me your 2nd number: '))
        z= multiply(x,y)
        print('After multiplying '+str(x)+' and '+str(y)+', We get:'+ str(z))
    elif d==4:
        x=float(input('Tell me your 1st number: '))
        y=float(input('With whom you wanna divide : '))
        z= divide(x,y)
        print('After dividing '+str(x)+' and '+str(y)+', We get '+ str(z))
    elif d==5:
        x=int(input('Factorial of which number you want: '))
        z=factorial(x)
        print('After doing factorial of '+str(x)+', We get '+ str(z))
    else:
        print(' Please provide a valid input.Thank You.')

if __name__=='__main__':
    c=(input('Tell me your name! '))
    print('Hello '+ str(c))
    print('Please select an operetion ')
    c='''    1. Add
    2. Substract
    3. Multiply
    4. Divide
    5. Factorial'''
    print(c)
    to_continue='Y'
    while to_continue=='Y':
        main()
        to_continue=input('Do you want to continue for another operation: Pres Y else N: ')

