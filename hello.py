# STRING
#Ask user name
name = input("What is your name? ")

#Say hello to user
print("hello! " + name)
#print(*object, sep='', end='\' , file=sys.stdout, flush=False)

#overwrite defaults parameter: end & sep
print("Hello, ", end="")#overwrite end='\' value
print(name)

#overwrite sep='\' value
print("Hello;", name, sep='')

# special format string
print(f"Hello..! {name}")
