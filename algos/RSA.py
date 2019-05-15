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
#       count = 0
#       carry = max(a,b)
#       div = min(a,b)
#       rem = carry%div
#       remArr = [carry,carry]
#       while(rem!=0):
#               carry = div
#               div = rem
#               rem = carry%rem
#               remArr[count%2] = rem
#               count+=1
#       return(max(remArr))
#

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
        pubKey =  {'n':n, 'e':e} 
        return(p,q,pubKey)


def genPriKey(p,q,e,r):
        n = p*q
        pq1 = (p-1)*(q-1)
        params = filter(lambda d:((d*e)%pq1)==1,range(1,r))
        d = params[0]
        return( {'n':n, 'd':d} )


params = genPubKey()


rawPriKey = genPriKey(params[0],params[1],params[2]['e'],10000)
rawPubKey = (params[2])

PriKey = 

e = rawPubKey['e']
d = rawPriKey['d']
n = rawPriKey['n']


text = 5

print(text)

def encrypt(text,e,n):
	code = (text**e)%n
	return code



print(code)

def decrypt(code,d,n):
	text = (code**d)%n
	return text

print(decrypt(code,d,n))
