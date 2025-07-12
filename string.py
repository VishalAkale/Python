v = str(input("Enter Any String: "))
print (v)
result=' '.join([char for char in v if char not in "AEIOUaeiou"])
print(result)