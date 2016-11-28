
def main():
	contacts = process_file_to_list()
	exit = False
	while not exit:	
		firstname = raw_input('What name are you looking for?').lower() # "Rose".lower() # eventually this will be raw_input
		print find_name_in_list(firstname, contacts)

def process_file_to_list():
	contacts = open ("contactlist.txt","r")
	contact_list = contacts.readlines()
	contacts.close()
	return contact_list

def find_name_in_list (firstname,contact_list):
	for contact in contact_list:
		striped_contact = contact.strip()
		record = striped_contact.split("|")
		# print striped_contact, record
		if record[0].lower() == firstname:
			return record



# firstname=raw_input ("Enter First Name")
	# for line in contact_list:
	# 	if record [0] == firstname:
	# 		firstname = True
	# 	else:
	# 		firstname = False
	# if firstname == False:
	# 	print ("Name not on contact list")
	# else:
	# 	print "record[0]\n,record[1]\n,record[2]\n,record[3]\n" in contact_list
	# print contact_list

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

# contactlist.close()

# if __name__ == '__main__':
# 	main()