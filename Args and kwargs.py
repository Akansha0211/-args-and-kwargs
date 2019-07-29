# def func(a,b,c):
#     print(a,b,c)
# #Akansha Aastha Vivek
# func("Akansha","Aastha","Vivek")  #everytime we add anew name we need to add a parameter

# def func(*args):
#     print(type(args))
#     print(args[0])
# a=["Akansha","Aastha","Vivek"]
# func(*a)
# <class 'tuple'>
# Akansha

# def func(*args):
#     for i in args:
#         print(i)
# a=["Akansha","Aastha","Ankita","Vivek"]
# func(*a)

# def func(normal,*args,**kwargs):
#     print(normal)
#     for i in args:
#         print(i)
# a=["Akansha","Aastha","Ankita","Vivek"]
# normal="Students :"
# func(normal,*a)

# def func(*args,normal):
#     print(normal)
#     for i in args:
#         print(i)
# a=["Akansha","Aastha","Ankita","Vivek"]
# normal="Students :"
# func(*a,normal)
#TypeError: func() missing 1 required keyword-only argument: 'normal'
#order of passing arguments is : normal argument,arg,kwarg

def func(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"{key} roll no {value}")
a=["Akansha","Aastha","Ankita","Vivek"]
normal="Students"
kw={"Akansha":"4 ","Aastha":"7","Vivek": "57 "}
func(normal,*a,**kw)

# def func(*args):
#     for i in args:
#         print(i)
# func("abc","def","ghi","jkl")

# def func(l):
#     for i in l:
#         print(i)
# list=["abc","def","ghi","jkl"]
# func(list)
# for i in range(1,3):
#     x=input("Enter a string")
#     list.append(x)
# func(list)

# def func(normal,*args):
#     print("First argument",normal)
#     for i in args:
#         print("next:",i)
# func("ab","cv","ad")

# def func(**kwargs):
#     for key,value in kwargs.items():
#         #print(f"{key}=={value}")
#         print("%s==%s"%(key,value))
# func(ab="ba",cd="dc",ef="fe")
#output:
# ab==ba
# cd==dc
# ef==fe

"""def func(arg1,arg2,arg3):
    print("1:",arg1)
    print("2:",arg2)
    print("3:",arg3)
n=("ab","ac","ad")
func(*n)"""
"""def func(*args):
   for i in args:
       print(i)
n=("ab","ac","ad")
func(*n)"""

# def func(*args):
#    for i in args:
#        print(i)
# func("ab","ac","ad")

# def func(a,b,c):
#    print(a)
#    print(b)
#    print(c)
# func("ab","ac","ad")

# def func(a,b,c):
#    print(a)
#    print(b)
#    print(c)
# n=("ab","ac","ad")
# func(n)
#TypeError: func() missing 2 required positional arguments: 'b' and 'c'

# def func(a,b,c):
#    print(a)
#    print(b)
#    print(c)
# n=("ab","ac","ad")
# func(*n)

def func(a,b,c):
   print(a)
   print(b)
   print(c)
n=("ab","ac","ad")
kw={"a" : "Geeks", "b" : "for", "c" : "Geeks"}
func(*n)
func(**kw)
# ab
# ac
# ad
# Geeks
# for
# Geeks

func(*n)
func(*kw)
# ab
# ac
# ad
# a
# b
# c
