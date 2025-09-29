#variables and strings
name = input("whats your name? ")
print("HELLO,", name, sep="MR ")#we use sep to separate the strings

name = input("whats your name? ")
print("hello," + name)


#print(*obj3ect, sep=' ', end='\n', file=sys.stdout, flush=False)
name = input("whats your name? ")
print("hello,", end="")#we use end to end the string
print(name)

name = input("whats your name? ")
print(f"hello, {name}")