a = 23
b = 22

bin_con = lambda x : bin(x)[2:].zfill(16)
#converting to binary:

bin1 = (bin(a)[2:].zfill(16))
print(bin(a)[2:].zfill(16))

## Left hift 

print(b << 1)
b = b << 1
print(bin_con(b))


## Setting a bit at nth position:

def set(num, pos):
    num = 1 << pos
    print(num)

def unset(num, pos):
    temp = 1 << pos
    print(bin(temp))
    temp = ~temp
    print(bin(temp))

    print("temp is: ",~temp)
    num &= temp
    return num

#print(unset(7,1)) 

def toggle(num, pos):
    temp = 1 << pos
    num = num ^ temp
    return num

print(f"Toggle is : {toggle(4,2)}")
