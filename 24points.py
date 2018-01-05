import random
def twenty_four_points():
    a=random.randint(1,13)
    b=random.randint(1,13)
    c=random.randint(1,13)
    d=random.randint(1,13)
    num1=int(a)
    num2=int(b)
    num3=int(c)
    num4=int(d)
    print(num1,num2,num3,num4)
    a1=input("The first number represents num1, the second number represents num2... Use numx to calculate 24!")
    
    if a1==24:
        return True
    else:
        twenty_four_points()
    
    
twenty_four_points()