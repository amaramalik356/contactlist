
def main():
	process_file_to_list

def process_file_to_list():
	contacts = open ("contactlist.txt","r")
	contact_list = contacts.readlines()
	contacts.close()
	firstname=raw_input ("Enter First Name")
	for line in contact_list:
		if record [0] == firstname:
			firstname = True
		else:
			firstname = False
	if firstname == False:
		print ("Name not on contact list")
	else:
		print "record[0]\n,record[1]\n,record[2]\n,record[3]\n" in contact_list


if __name__ == '__main__':
	main()

# 	# def main():
# contactlist = open("contactlist.txt","r")
# # with open("contactlist.txt") as my_file:
# contactlist.read()
# # print my_file
# firstname = raw_input("Enter First Name").lower()
# for firstname in my_file:
# 	if record [0] == firstname:
# 		firstname = True
# 	else:
# 		firstname = False
# if firstname == False:
# 	print ("Name not on contact list")
# else:
# 	print "record[0]\n,record[1]\n,record[2]\n,record[3]\n" in my_file

contactlist.close()

# if __name__ == '__main__':
# 	main()