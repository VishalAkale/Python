v = str(input("Enter Any String: "))
print (v)

a=''
n=''
s=''

for g in v:
    if g.isalpha():
        a=a+g
    elif g.isdigit():
        n=n+g
    else:
        s+=g

print("Alphabets: ",a)
print("Numbers Are: ",n)
print("Special Characters: ",s)