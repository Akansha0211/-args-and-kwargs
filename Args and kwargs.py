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
