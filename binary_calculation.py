def makeEqualLength(a, b): 
	len_a = len(a) 
	len_b = len(b) 
	num_zeros = abs(len_a - len_b) 
	if (len_a < len_b): 
		for i in range(num_zeros): 
			a = '0' + a 
		return len_b, a, b 
	else: 
		for i in range(num_zeros): 
			b = '0' + b 
	return len_a, a, b

def bitwiseRightShift(A):
    n = len(A)
    res=""
    
    if (A[n-1]=="1"):
        res = res + str(1)
    else:
        res = res + str(0)
    for i in range(n-1):
        if (A[i]=="1"):
            res = res + str(1)
        else:
            res = res + str(0)
    return str(int(res))

def conver(A):
    if(A=="0000"):
        return "0"
    elif(A=="0001"):
        return "1"
    elif(A=="0010"):
        return "2"
    elif(A=="0011"):
        return "3"
    elif(A=="0100"):
        return "4"
    elif(A=="0101"):
        return "5"
    elif(A=="0110"):
        return "6"
    elif(A=="0111"):
        return "7"
    elif(A=="1000"):
        return "8"
    elif(A=="1001"):
        return "9"
    elif(A=="1010"):
        return "A"
    elif(A=="1011"):
        return "B"
    elif(A=="1100"):
        return "C"
    elif(A=="1101"):
        return "D"
    elif(A=="1110"):
        return "E"
    elif(A=="1111"):
        return "F"

def bin2Hex(A):
    temp = ""
    res =""
    while (len(str(A))%4!=0):
        A = '0' + A 
    for i in range(1,len(A)+1):
        temp += str(A[i-1])
        if(i%4==0):
            res = res + str(conver(temp))
            temp = ""
    return str(res)

def sum( A, B ): 
	result = ''
	length, A, B = makeEqualLength(A, B) 
	carry = 0
	for i in range(length - 1, -1, -1): 
		firstBit = int(A[i]) 
		secondBit = int(B[i]) 
		sum = (firstBit ^ secondBit ^ carry) + 48
		result = chr(sum) + result 
		carry = (firstBit & secondBit) | (secondBit & carry) | (firstBit & carry) 
	if carry == 1: 
		result = '1' + result 
	return result 

def dif(a, b):
    if len(a)< len(b):
        res = "error"
        return str(res)
    length, a, b = makeEqualLength(a, b) 
    for ch in a: assert ch in {'0','1'}, 'bad digit: ' + ch    
    for ch in b: assert ch in {'0','1'}, 'bad digit: ' + ch    
    sumx = int(a, 2) - int(b, 2)    
    return str(int(bin(sumx)[2:]))

def prod(a, b):
    length, a, b = makeEqualLength(a, b)
    for ch in a: 
        assert ch in {'0','1'}, 'bad digit: ' + ch    
    for ch in b: 
        assert ch in {'0','1'}, 'bad digit: ' + ch    
    sumx = int(a, 2) * int(b, 2)    
    return str(int(bin(sumx)[2:]))

def bitwiseAnd(s1, s2): 
	length, s1, s2 = makeEqualLength(s1, s2) 
	res = "" 
	for i in range(length):  
		res = res + str(int(s1[i]) & int(s2[i]))
	return str(int(res))

def bitwiseOr(s1, s2): 
	length, s1, s2 = makeEqualLength(s1, s2) 
	res = "" 
	for i in range(length):  
		res = res + str(int(s1[i]) | int(s2[i]))
	return str(int(res))

def bitwiseXor(s1, s2): 
	length, s1, s2 = makeEqualLength(s1, s2) 
	res = "" 
	for i in range(length):  
		res = res + str(int(s1[i]) ^ int(s2[i]))
	return str(int(res))
    
def bitwiseNot(s1):
	length, s1, s2 = makeEqualLength(s1, "0")
	res = ""
	for i in range(len(str(s1))):
		if(s1[i]=="1"):
			res = res + str(0)
		else:
			res = res + str(1)
	return str(int(res))
	
def bitwiseLeftShift(A):
    n = len(A)
    res=""
    for i in range(n-1):
        if (A[i+1]=="1"):
            res = res + str(1)
        else:
            res = res + str(0)
    if (A[0]=="1"):
        res = res + str(1)
    else:
        res = res + str(0)
    return str(int(res))

def bitwiseRightShift(A):
    n = len(A)
    res=""
    
    if (A[n-1]=="1"):
        res = res + str(1)
    else:
        res = res + str(0)
    for i in range(n-1):
        if (A[i]=="1"):
            res = res + str(1)
        else:
            res = res + str(0)
    return str(int(res))
