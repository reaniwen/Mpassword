import random

def creatpassword():
	len = int(raw_input("please input the length you wanna have:"))
	print "please input the difficulty you wanna create"
	diff = 0
	diff = int(raw_input("(1:number, 2:1+letter, 3:2+symbol):"))
	while diff <= 0 or diff > 3:
		print diff
		print 'wrong number'
		print "please input the difficulty you wanna creat"
		diff = int(raw_input("(1:only number, 2:1+letter, 3:2+symbol):"))
	
	#init book1
	book1 = []
	for i in range(48,58):
		book1.append(i)
	
	#init book2
	book2 = book1[:]
	for i in range(65,91):
		book2.append(i)
	for i in range(97,123):
		book2.append(i)
	
	#init book3
	book3 = book2[:]
	for i in range(33,48):
		book3.append(i)
	for i in range(58,65):
		book3.append(i)
	for i in range(123,127):
		book3.append(i)
	#repeat or not reapeat, that's the question
	if diff == 1:
		book = book1[:]
		#seq = random.sample(book1,len)
	elif diff == 2:
		book = book2[:]
		#seq = random.sample(book2,len)
	else:
		book = book3[:]
		#seq = random.sample(book3,len)
	seq = []
	for _ in range(len):
		seq.append(random.choice(book))
	print seq
	p = ''
	for _ in seq:
		p += chr(_)
	print p
	return p

	
if __name__ == "__main__":
	while True:
		creatpassword()