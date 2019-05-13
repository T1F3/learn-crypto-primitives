import random

def findPrimes(lower,upper):
	primArr = []
	for num in range(lower,upper + 1):
		if num > 1:
			for i in range(2,num):
				if (num % i) == 0:
					break
			else:
				primArr.append(num)
	return(primArr)

primes = findPrimes(10,100)

# def Euclid(a,b):
# 	count = 0
# 	carry = max(a,b)
# 	div = min(a,b)
# 	rem = carry%div
# 	remArr = [carry,carry]
# 	while(rem!=0):
# 		carry = div
# 		div = rem
# 		rem = carry%rem
# 		remArr[count%2] = rem
# 		count+=1
# 	return(max(remArr))

def Euclid(a, b):  
    if a == 0 : 
        return b  
    return Euclid(b%a, a)

def genPubKey():
	p = primes[random.randint(0,len(primes)-1)]
	q = primes[random.randint(0,len(primes)-1)]
	n = p*q
	pq1 = (p-1)*(q-1)	
	e = random.randint(2, pq1-1)
	while( Euclid(e,pq1) !=1 ):
		e = random.randint(2, pq1-1)
	pubKey = (n,e)
	return(p,q,pubKey)


def genPriKey(p,q,e,r):
	n = p*q
	pq1 = (p-1)*(q-1)
	params = filter(lambda d:((d*e)%pq1)==1,range(1,r))
	d = params[0]
	return(n,d)

params = genPubKey()


PriKey = genPriKey(params[0],params[1],params[2][1],10000)
PubKey = (params[2])

print(PubKey,'--',PriKey)
