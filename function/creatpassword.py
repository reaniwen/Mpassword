import random

def creatpassword(len,diff):
	book = creatbook(diff)
	seq = []
	for _ in range(len):
		seq.append(random.choice(book))
	#print seq
	p = ''
	for _ in seq:
		p += chr(_)
	print p
	return p


def creatbook(diff):
	#init book1
	book1 = []
	for i in range(48,58):
		book1.append(i)
	
	#init book2
	book2 = book1[:]
	#increase the possiblity of number
	for i in range(65,91):
		book2.append(i)
	for i in range(97,123):
		book2.append(i)
	#increase and control the possibility of number to 75%
	#fail
	#it works
	newBook2 = book2[:]
	for i in range(2):
		for _ in book1:
			newBook2.append(_)
	
	#init book3
	book3 = book2[:]
	for i in range(33,48):
		book3.append(i)
	for i in range(58,65):
		book3.append(i)
	for i in range(123,127):
		book3.append(i)
	#increase and control the possibility of number and letter to 75%
	#fail
	newBook3 = book3[:]
	for i in range(2):
		for _ in book2:
			newBook3.append(_)
	#repeat or not reapeat, that's the question
	#init the book
	if diff == 1:
		book = book1
		#book = book1[:]
	elif diff == 2:
		book = book2[:]
	else:
		book = book3[:]
	return book

	
if __name__ == "__main__":
	while True:
		len = int(raw_input("please input the length you wanna have:"))
		print "please input the difficulty you wanna create"
		diff = 0
		diff = int(raw_input("(1:number, 2:1+letter, 3:2+symbol):"))
		while diff <= 0 or diff > 3:
			print diff
			print 'wrong number'
			print "please input the difficulty you wanna creat"
			diff = int(raw_input("(1:only number, 2:1+letter, 3:2+symbol):"))
		book = creatbook(diff)
		#password = creatpassword(len,book)
		password = creatpassword(len,diff)