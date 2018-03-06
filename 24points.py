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
    c=random.randint(1,10)
    d=random.randint(1,10)
    
    numlist=[a,b,c,d]
    print(numlist)
    first_guess(numlist)
    """
    num1=int(a)
    num2=int(b)
    num3=int(c)
    num4=int(d)
    print(num1,num2,num3,num4)
    """
    
   
    ope3=input("What's your next operator?")
    n4=int(input("What's your fourth number?"))
    if ope3=="+":
        result3=result2+n4
    elif ope3=="-":
        result3=result2-n4
    elif ope3=="*":
        result3=result2*n4
    elif ope3=="/":
        result3=result2*n4    
    
    print("Your result is", result3)
    if result3==24:
        print("Right,next one")
        twenty_four_points()
    else:
        print("Not True")
        twenty_four_points()
    
def first_guess(list1):
    n1=int(input("What's your first number?"))
    isgood=False
    for i in list1:
        if i == n1:
            isgood=True
    if isgood == False:
        first_guess(list1)
    
    ope1=input("What's your operator?")
    n2=int(input("What's your second number?"))
    for i in list1:
        if i == n2:
            isgood=True
    if isgood == False:
        first_guess(list1)
    
    if ope1=="+":
        result1=n1+n2
    elif ope1=="-":
        result1=n1-n2
    elif ope1=="*":
        result1=n1*n2
    elif ope1=="/":
        result1=n1*n2
        
    print("Then you will get", result1)
    second_guess(numlist,result1)        ##问题是这里没numlist
    
def second_guess(list2,result1):
    ope2=input("What's your next operator?")
    n3=int(input("What's your third number?"))
    isgood=False
    for i in list2:
        if i == n3:
            isgood=True
    if isgood == False:
        first_guess(list1)
    
    if ope2=="+":
        result2=result1+n3
    elif ope2=="-":
        result2=result1-n3
    elif ope2=="*":
        result2=result1*n3
    elif ope2=="/":
        result2=result1*n3    
    
    print("Then you will get", result2)
    
twenty_four_points()
#test_suite()