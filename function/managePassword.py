import creatpassword
#from creatpassword import *

#chaxun
	#load from file
	#select name to load
	#type your password
	#run AES with pin
def querypass():
	file_object = open('data.txt')
	try:
		all_the_text = file_object.read( )
		print(all_the_text)
	finally:
		file_object.close( )

#baocun
	#choose name to save
	#whether run create function?
	#type your password
	#run AES with pin
	#save to file as dict
def saveNewPass():
	file_object = open('data.txt',"w+")
	try:
		passdict = file_object.read( )
		if passdict == False:
			passdict = {}
		else:
			passKey = raw_input("input your password site: ")
			passWord = input("input your password of "+passKey+" :")
			passdict[passKey] = str(passWord)
			file_object.write(passKey)	
	finally:
		file_object.close( )



if __name__ == "__main__":
	while True:
		saveNewPass()
		querypass()