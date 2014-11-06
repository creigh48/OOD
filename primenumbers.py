#Jeffrey Creighton
#Updated by Anand Patel

#Looks through each number within the range and prints it if prime.
def primenumbers(i):
	for j in range(2, i+1):
		if checkPrime(j): #find out if j is prime
			print j

#Checks to see if a number is prime. Returns false if any number less than sqrt+1 divides evenly, true otherwise.
def checkPrime(k):
	for i in range(2, int(k**.5 + 1)):
		if i < k:
			if (k % i) == 0:
				return False
	return True

primenumbers(input("Enter a number: "))
