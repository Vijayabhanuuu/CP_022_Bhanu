# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	
	a=[]
	a1=[]
	while(hand>0):
		rem=hand%10
		hand=hand//10
		a.append(rem)
	a1=a[::-1]
	return tuple(a1)
	return a1


	
