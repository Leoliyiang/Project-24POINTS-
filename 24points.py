import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(twenty_four_points()==True)

import random
def twenty_four_points():
    a=random.randint(1,10)
    b=random.randint(1,10)
    #c=random.randint(1,13)
    #d=random.randint(1,13)
    num1=int(a)
    num2=int(b)
    num3=int(c)
    #num4=int(d)
    print(num1,num2,num3) #,num4)
    
    n1=int(input("What's your first number?"))
    ope1=input("What's your operator?")
    n2=int(input("What's your second number?"))
    ope2=input("What's your operator?")
    n3=int(input("What's your third number?"))
    if ope1=="+":
        result1=n1+n2
    elif ope1=="-":
        result1=n1-n2
    elif ope1=="*":
        result1=n1*n2
    elif ope1=="/":
        result1=n1*n2
        
    
    
    print("Your result is", result)
    if result==24:
        print("Right,next one")
        twenty_four_points()
    else:
        print("Not True")
        twenty_four_points()
    
    
twenty_four_points()
#test_suite()