#Jeffrey Creighton

#look through each number within the range
def primenumbers(i):
	for j in range(2, i+1):
		if checkPrime(j): #find out if j is prime
			print j

#check to see if a number is prime 
def checkPrime(k):
	for i in range(2, k):
		if i < k:
			if (k % i) == 0:
				return False
	return True

primenumbers(input("Enter a number: "))
