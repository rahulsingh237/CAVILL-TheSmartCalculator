print{'''
1. addition
2. subtraction
3. multiplication
4. division
'''
}

x=int(input("Enter your choice : "))

y=int(input("Enter first number : "))
z=int(input("Enter second number : "))

if x==1:
    a=y+z
    print("answer = ",a)
elif x==2:
    a=y-z
    print("answer = ",a)
elif x==3:
    a=y*z
    print("answer = ",a)
else :
    if z==0 or y==0 :
        print("Zero division error")
    else :
        a=y/z
        print("answer = ",a)