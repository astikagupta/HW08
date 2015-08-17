import sys
import random

def random_with_N_digits(n):
    range_start = 0
    range_end = 10**int(n)-1
    return random.randint(range_start, range_end)



def func1():
	if len(sys.argv) == 2 :
		length = sys.argv[1]
	else:
		length = 3
	rand = random_with_N_digits(length)
	print rand
	i = 0
	j=0
	cow=0
	bull=0
	while(i<((2^int(length))+int(length))):
		try:
			guess = int(raw_input("Guess a {0}-digit number: ".format(length)))

			# if len(str(x)) == length:

			for i in str(guess):
				for j in str(rand):
					if guess[i] == rand[j]:
						if i == j:
							bull+= 1
						else:
							cow+= 1
					j+= 1
				i+= 1
			print cow
			print bull

			
				
			# limit to 3 chances 
			# else:
				# print "Enter correct no of digits"
				# continue


				

		except ValueError:
			print "Wrong input. Try again."





		







def main():
	func1()

main()