import sys
import random

def random_with_N_digits(n):
    range_start = 10**(int(n)-1)
    range_end = 10**int(n)-1
    return random.randint(range_start, range_end)

def func1():
	if len(sys.argv) == 2 :
		length = sys.argv[1]
	else:
		length = 1
	y = random_with_N_digits(length)
	print y
	i = 0
	while(i<4):
		try:
			x = int(raw_input("Guess a {0}-digit number: ".format(length)))

			# if len(str(x)) == length:

			if x<y:
				print "Your guess is low. Try again."
				continue
			elif x>y:
				print "your guess is high. Try again."
				continue
			else:
				print "you guessed correctly! Bye!"
				break
				
			# limit to 3 chances 
			# else:
				# print "Enter correct no of digits"
				# continue


				

		except ValueError:
			print "Wrong input. Try again."





		







def main():
	func1()

main()