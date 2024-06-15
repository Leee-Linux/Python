#define function  hello
def hello(to = "world"):
    print("Hello,", to)

hello()

name = input("What is your name ?")
name = name.strip().title()
hello(name)

#print("hello,", name)
