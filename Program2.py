#Program2.py
#Written By: Ryaan Ali and Charuhas Unni
#Under the GPL v3.0
#Comments Added By: Alexander Parsan

import random
LeNumber = 10
print "hey gueyz! Whats le number?"
guess = 0
tries = 0
while guess != LeNumber and tries < 5:
	LeNumber = random.randint (1,10)
	guess = input()
	if guess > LeNumber:
		print "HAAA! Nonononono! Too high"
		tries = tries + 1
	elif guess < LeNumber:
		print "HAAA! Nonononono! Too low"
		tries = tries + 1
if guess == LeNumber:
	print "Gud joooooooooob! U Actually beat the troll game!"
else:
	print "GG m8! u did it! How do you Feel?"
	ugotsiked = raw_input()
	print "SIKEEEEEEEE THATS THE WROOOOOOOOONG NUMBAAAAAAAAAA"
