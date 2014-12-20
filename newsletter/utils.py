import random

def salt(n):
	alp = "0123456789abcdefgijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
	mysalt = []
	for i in range(n):
		mysalt.append(random.choice(alp))

	return "".join(mysalt)
