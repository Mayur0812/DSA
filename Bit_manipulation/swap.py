a  = 7
b  = 9
print(bin(a))
print(bin(b))
a ^= b

print(bin(a))
b ^= a
a ^= b

print(a,b)
