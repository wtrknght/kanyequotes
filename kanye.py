import random
def printquote():
	g = open('quotes.txt', 'r')
	f = g.readlines()
	t = []
	for line in f:
		t.append(line)
	j = random.choice(t)
	print(j)
	g.close()
