from re import X


def pat1(n):
    for i in range(1,n+1):
        print("*"*i)

def pat2(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"*"*i)
pat2(5)

def pat3(n):
    for i in range(1,n+1):
        print(" "*(n-i) + " *"*i)
pat3(5)

def pat4(n):
    for i in range(n+1,0,-1):
        print(" "*(n-i) + "*"*(2*i - 1))
pat4(5)

def pat5(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print()
pat5(5)
    

def pat6(n):
    x = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(x,end = " ")
            x += 1
        print()
pat6(5)

def pat7(n):
    x = 65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(x),end = " ")
        x += 1
        print()
pat7(5)

def pat8(n):
    x = 65
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(x),end = " ")
            x += 1
        print()
pat8(5)

def pat9(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("K",end = " ")
        print()
pat9(5)

def pat10(n):
    for i in range(1,n+1):
        x = 65
        for j in range(1,i+1):
            print(chr(x),end = " ")
            x += 1
        print()
pat10(5)

def pat11(s4):
    for i in range(0,len(s4)):
        for j in range(0,i+1):
            print(s4[j],end = " ")
        print()
pat11("Python")

def pat12(n):
    x = 1
    for i in range(n,0,-1):
        for j in range(i):
            print(x,end = " ")
        x += 1
        print()
pat12(5)

def pat13(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(i,end = " ")
        print()
pat13(6)

def pat14(n):
    for i in range(n+1,1,-1):
        x = 0
        for j in range(i):
            print(x,end = " ")
            x += 1
        print()
pat14(5)

def pat15(n):
    x = 1
    for i in range(1,n+1,2):
        for j in range(1,i+1):
            print(x,end = " ")
            x += 1
        print()
pat15(5)

def pat16(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end = " ")
        print()
pat16(6)

def pat17(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(2*i-1,end = " ")
        print()
pat17(5)

def pat18(n):
    for i in range(1,n+1):
        x = 1
        for j in range(n,0,-1):
            if j > i:
                print(" ",end = " ")
            else:
                print(x,end = " ")
                x += 1
        print() 
pat18(5)

def pat19(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ") if j > i else print(i,end = " ")
        print()
pat19(5)

def pat20(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j*i,end = " ")
        print()
pat20(7)

def pat21(n):
    for i in range(0,n+1):
        for j in range(i,-1,-1):
            print(2**j,end = " ")
        print()
pat21(7)

def pat22(n):
    for i in range(n+1):
        print("*"*i)
    for j in range(n-1,0,-1):
        print("*"*j)
pat22(5)

def pat23(n):
    for i in range(1,n+1):
        print("*"*i)
    print()
    for j in range(n,0,-1):
        print("*"*j)
pat23(5)

def pascal_triangle(n):
    for i in range(1,n+1):
        for  j in range(0,n-i+1):
            print(" ",end = " ")
        c = 1
        for j in range(1,i+1):
            print(" ",c,end = " ")
            c = c * (i-j) // j
        print()
pascal_triangle(5)