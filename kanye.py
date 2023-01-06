import random
g = open('quotes.txt', 'r')
f = g.readlines()
t = []
for line in f:
	t.append(line)
j = random.choice(t)
print(j)
