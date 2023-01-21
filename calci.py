def calci():
    print("Say hello to calci it's a beta version calculator that can perform some famous calculations on Numbers.calci was created on 03-08-2022 and it's the first program of its creator")
    y=1
    op=input(f"Enter Operation to perform press \n'+' for Addition,'*' for Multiplication,'/' for Division,'-' for Subtraction,\n's' for square,'sr' for squareroot,\n'c' for cube,'cr' for cube root,\n'f' for factorial\n")
    if op=='c':
        z=int(input("Enter Your No.:"))
        r=z**3
        print(f"Cube of Number is:{r}")

    elif op=="cr":
        z=int(input("Enter Your No.:"))
        r=z**(1/3)
        pritn(f"Cube Root of No. is:{r}")

    elif op=="s":
        z=int(input("Enter Your No.:"))
        r=z**2
        print(f"Square of Number is:{r}")

    elif op=="sr":
        z=int(input("Enter Your No.:"))
        r=z**(1/2)
        print(f"Square_root of Number is:{r}")

    elif op=="f":
        z=int(input("Enter Your No.:"))
        for i in range(1,z+1):
            y*=i
        print(f"Factorial of No. is:{y}")

    elif op=="+":
        a=int(input("Enter Your first No.:"))
        b=int(input("Enter your Second No.:"))
        print(f"Addition of NO. is:{a+b}")
    elif op=="*":
        a=int(input("Enter Your first No.:"))
        b=int(input("Enter your Second No.:"))
        print(f"Multiplication of NO. is:{a*b}")
    elif op=="/":
        a=int(input("Enter Your first No.:"))
        b=int(input("Enter your Second No.:"))
        print(f"Division of NO. is:{a/b}")
    elif op=="-":
        a=int(input("Enter Your first No.:"))
        b=int(input("Enter your Second No.:"))
        print(f"Subtract of NO. is:{a-b}")
        
calci()